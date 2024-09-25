import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/llm-websocket/test-call-id"
    
    async with websockets.connect(uri) as websocket:
        # Receive the first message from the server
        first_response = await websocket.recv()
        print(f"Received from server: {first_response}")
        
        # Simulate sending a request message with response_id
        request_data = {
            "message": "Hello LLM",
            "response_id": 1
        }
        await websocket.send(json.dumps(request_data))

        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received from server: {response}")

# Run the test
asyncio.run(test_websocket())