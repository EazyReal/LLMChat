# LLM Conversation with Retell

## How it works
- The frontend call the backend API `/start_call` to trigger a new call with an agent prompt
- The backend handle the request by setting the agent prompt for the LLM agent, requesting a call from Retell and return the call information to the client
- The client connect to the call
- During conversation, the backend will handle requests from the websocket

## Quick Start

### Frontend
- install dependencies `npm install`
- `npm start`
  - the frontend will call the backend API, make sure to have the right url to the backend endpoint

### Backend
- create a Retell account
- fill in the `.env` file
- starting the server `uvicorn backend.server:app --reload --port=<port>`
- exposing the backend from localhost to public address by using `ngrok`
- create a Retell agent handler with the ngrok public url