import asyncio
import json
import websockets

async def hello():
    async with websockets.connect(
            'wss://ws.binaryws.com/websockets/v3?app_id=1089') as websocket:

        json_data = json.dumps({'ticks':'R_100'})
        await websocket.send(json_data)

        greeting = await websocket.recv()
        #print(f"< {greeting}")
        print(greeting)

asyncio.get_event_loop().run_until_complete(hello())
