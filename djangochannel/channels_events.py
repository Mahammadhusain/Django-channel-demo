
"type":"websocket.connect" # called at when client open connection
"type":"websocket.accept" # called for accept incoming connection (u can pass hader with this event)
"type":"websocket.receive" # called at when server recived data(message) from client
"type":"websocket.send" # called at when client recived data(message) from server  
"type":"websocket.disconnect" # called at when connection lost form either client or server.   
"type":"websocket.close" # send by the application to tell the server to close connection.   


