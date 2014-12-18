from whereisgrant import application
from socketio.server import SocketIOServer
from gevent import monkey 

## Local Includes ## 
from whereisgrant import test_connect


if __name__ == '__main__':
	SocketIOServer(
		('', application.config['PORT']),
		application,
		resource="socket.io").serve_forever()
