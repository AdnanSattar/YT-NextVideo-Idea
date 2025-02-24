#!/usr/bin/env python
import sys
from crew import YoutubeIdeaGeneratorCrew

# This main file is intended as a local entry point for testing the Crew workflow.
# It executes the Crew pipeline with predefined inputs.

def run():
    """
    Run the crew.
    """
    inputs = {
        "comments": '[{"video_title": "I Automated My YouTube Channel With CrewAI [Free Source Code Included]", "comment": "The BEST video really inspired me a lot and I can\'t wait to get started using crewAI to make some interesting work", "video_id": "95ab3e25-12bd-4611-b09a-4fea29846c3d", "comment_id": "8013f709-93af-4a06-b14a-612c988b504f"},'
                    '{"video_title": "I Automated My YouTube Channel With CrewAI [Free Source Code Included]", "comment": "576", "video_id": "95ab3e25-12bd-4611-b09a-4fea29846c3d", "comment_id": "2fa5ad42-74c1-463c-9ca3-751f2196955b"}]'
    }
    YoutubeIdeaGeneratorCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        YoutubeIdeaGeneratorCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        YoutubeIdeaGeneratorCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        YoutubeIdeaGeneratorCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    run()
