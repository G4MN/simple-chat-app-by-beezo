from quart import Quart, websocket, render_template_string

app = Quart(__name__)
connected_sockets = set()

@app.route('/')
async def index():
    return await render_template_string('''
    <script>
        const ws = new WebSocket('ws://' + location.host + '/ws');
        ws.onmessage = (event) => { console.log(event.data); };
        ws.onopen = (event) => { ws.send('Hello, server!'); };
    </script>
    ''')

@app.websocket('/ws')
async def ws():
    global connected_sockets
    connected_sockets.add(websocket._get_current_object())
    try:
        while True:
            message = await websocket.receive()
            for socket in connected_sockets:
                await socket.send(f"{message}")
    finally:
        connected_sockets.remove(websocket._get_current_object())

if __name__ == '__main__':
    app.run(port=8000)