from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from pydantic import BaseModel
from typing import List, Optional
import json
import os
import requests
import logging
from dotenv import load_dotenv
from crew import YoutubeIdeaGeneratorCrew

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="YouTube Idea Generator API")

# Pydantic models
class Comment(BaseModel):
    video_title: str
    comment: str
    video_id: str
    comment_id: str

class CommentRequest(BaseModel):
    comments: List[Comment]

class JobStatus(BaseModel):
    state: str
    status: Optional[str] = None
    result: Optional[str] = None

class Idea(BaseModel):
    score: int
    video_title: str
    description: str
    video_id: str
    comment_id: str
    research: List[dict]

@app.get("/")
def read_root():
    logger.info("API root accessed")
    return {"message": "YouTube Video Idea Generator API is running"}

@app.post("/kickoff/")
def kickoff_idea_generation(request: CommentRequest, background_tasks: BackgroundTasks):
    """Initiates the idea generation process."""
    comments_json = json.dumps([comment.dict() for comment in request.comments])
    inputs = {"comments": comments_json}
    
    logger.info(f"Received request to kickoff idea generation with comments: {comments_json}")

    try:
        crew_instance = YoutubeIdeaGeneratorCrew().crew()
        
        kickoff_response = crew_instance.kickoff(inputs=inputs)

        # Log the full response for debugging
        logger.info(f"CrewAI kickoff response: {kickoff_response}")
        
        # Extract kickoff_id properly
        kickoff_id = getattr(kickoff_response, "kickoff_id", None)
        
        if not kickoff_id:
            logger.error(f"Failed to retrieve kickoff ID from CrewAI. Response: {kickoff_response}")
            raise HTTPException(status_code=500, detail="Failed to retrieve kickoff ID")
        
        logger.info(f"Successfully initiated CrewAI job with kickoff_id: {kickoff_id}")
        background_tasks.add_task(poll_job_status, kickoff_id)
        return {"kickoff_id": kickoff_id}
    
    except Exception as e:
        logger.error(f"Error initiating CrewAI job: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status/{kickoff_id}", response_model=JobStatus)
def check_job_status(kickoff_id: str):
    """Checks the status of a running job."""
    logger.info(f"Checking job status for kickoff_id: {kickoff_id}")

    try:
        status_url = f"{os.getenv('CREWAI_URL')}/status/{kickoff_id}"
        response = requests.get(status_url, headers={"Authorization": f"Bearer {os.getenv('CREWAI_BEARER_TOKEN')}"})
        response.raise_for_status()
        
        logger.info(f"Job status received: {response.json()}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching job status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/new-ideas/", response_model=List[Idea])
def get_new_ideas():
    """Retrieves newly generated video ideas."""
    logger.info("Fetching new ideas from CrewAI")

    try:
        ideas_url = f"{os.getenv('CREWAI_URL')}/ideas"
        response = requests.get(ideas_url, headers={"Authorization": f"Bearer {os.getenv('CREWAI_BEARER_TOKEN')}"})
        response.raise_for_status()
        
        logger.info(f"New ideas received: {response.json()}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching new ideas: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def poll_job_status(kickoff_id: str):
    """Background task to check job status until completion."""
    import time
    logger.info(f"Polling job status for kickoff_id: {kickoff_id}")

    while True:
        status = check_job_status(kickoff_id)
        if status.state in ["SUCCESS", "FAILED"]:
            logger.info(f"Job {kickoff_id} completed with status: {status.state}")
            break
        time.sleep(5)

@app.get("/idea-details/")
def get_idea_details(video_id: str, comment_id: str):
    """Fetches idea details by video and comment ID."""
    logger.info(f"Fetching idea details for video_id: {video_id}, comment_id: {comment_id}")

    try:
        idea_details_url = f"{os.getenv('CREWAI_URL')}/idea-details/{video_id}/{comment_id}"
        response = requests.get(idea_details_url, headers={"Authorization": f"Bearer {os.getenv('CREWAI_BEARER_TOKEN')}"})
        response.raise_for_status()
        
        logger.info(f"Idea details received: {response.json()}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching idea details: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
