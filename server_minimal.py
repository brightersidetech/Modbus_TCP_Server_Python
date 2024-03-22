from pyModbusTCP.server import ModbusServer
import logging

logging.basicConfig()
logging.getLogger('pyModbusTCP.server').setLevel(logging.INFO)

# server parameters
host = '0.0.0.0'
port = 502

if __name__ == '__main__':
    # create server
    Server = ModbusServer(host=host, port=port)

    # run server
    Server.start()



