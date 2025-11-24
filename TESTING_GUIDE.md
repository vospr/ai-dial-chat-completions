# Testing Guide

## Setup

1. Activate virtual environment:
```bash
source .venv/bin/activate
```

## Running the Application

### Test with DialClient (using aidial-client library)
```bash
python -m task.app
```

### Test with CustomDialClient (using raw HTTP requests)
```bash
python test_custom_client.py
```

## Test Scenarios

### Scenario 1: Calculator

**System Prompt:**
```
You are a calculator. Your role is to perform mathematical computations and output the result as a number. Do NOT include any words, explanations, or units in your responses. Only provide the numeric result of the calculation.
```

**Test Conversation:**
1. Input: `Hi, what can u do?`
   - Expected: `0` or minimal response

2. Input: `3*8`
   - Expected: `24`

3. Input: `/2`
   - Expected: `12`

4. Input: `-3`
   - Expected: `9`

5. Input: `^2`
   - Expected: `81`

### Scenario 2: Technical Troubleshooting

**System Prompt:**
```
You are a Python expert and troubleshooting specialist. Your role is to assist in diagnosing and resolving technical issues related to Python programming. Provide clear, concise, and step-by-step solutions, ensuring the user understands the reasoning behind each step. When applicable, include example code, best practices, or alternative approaches. If the issue involves debugging, highlight the root cause and suggest efficient ways to fix or optimize the code. Always prioritize clarity, accuracy, and actionable advice.
```

**Test Conversation:**
1. Input: `Hi, what can u do?`
   - Expected: Professional introduction about Python troubleshooting capabilities

2. Input: `I'm getting an error while running my Python script.`
   - Expected: Request for error details

3. Input: `'ModuleNotFoundError: No module named requests'.`
   - Expected: Solution to install requests module

4. Input: `I tried that, but now it says 'Permission denied'.`
   - Expected: Solutions for permission issues (sudo, virtual environment)

5. Input: `I set up the virtual environment, and now it works. But another error came up: 'ConnectionError'.`
   - Expected: Explanation about ConnectionError and troubleshooting steps

## Features to Verify

✅ **Streaming in Console**: Output should appear character by character in real-time

✅ **Conversation History**: The AI should remember previous messages in the conversation

✅ **Exit Command**: Typing `exit` should gracefully close the application

## Switching Between Clients

- `task/app.py` uses `DialClient` by default
- `test_custom_client.py` uses `CustomDialClient` to show full request/response details
- CustomDialClient prints the raw JSON request and response for debugging

## Notes

- The API key is configured in `task/constants.py`
- Default deployment is `applications/public/gpt-4o`
- Streaming is enabled by default (stream=True)

