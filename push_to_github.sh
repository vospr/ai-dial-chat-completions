#!/bin/bash

# This script will commit and push your completed work to GitHub

echo "Initializing git repository..."
git init

echo "Adding remote repository..."
git remote add origin https://github.com/vospr/ai-dial-chat-completions.git

echo "Adding all files..."
git add .

echo "Creating commit..."
git commit -m "Complete DIAL AI Chat Completion task

- Implemented DialClient using aidial-client library
- Implemented CustomDialClient using raw HTTP requests (requests & aiohttp)
- Completed main app.py with conversation management
- Added support for both streaming and non-streaming completions
- Conversation history is maintained throughout the session
- Added testing guide and custom client test script
- Configured API key in constants.py"

echo "Pushing to GitHub..."
git push -u origin main

echo "Done! Your code has been pushed to GitHub."

