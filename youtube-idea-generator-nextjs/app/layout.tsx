import type { Metadata } from "next";
import { Lato } from "next/font/google";
import {
  ClerkProvider,
  SignInButton,
  SignedIn,
  SignedOut,
  UserButton
} from '@clerk/nextjs'
import Navbar from "@/components/Navbar";
import { Toaster } from "@/components/ui/toaster";
import './globals.css'

const lato = Lato({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-roboto",
});

export const metadata: Metadata = {
  title: "Youtube Idea Generator",
  description: "Generate fresh ideas for your YouTube content",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider afterSignOutUrl="/" dynamic>
      <html lang="en">
        <body className={`${lato.className} bg-gray-50`}>
          <div className="max-w-6xl mx-auto min-h-screen">
            <Navbar />
            {children}
            <Toaster />
          </div>
        </body>
      </html>
    </ClerkProvider>
  );
}
