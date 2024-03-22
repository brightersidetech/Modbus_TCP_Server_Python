from pyModbusTCP.server import ModbusServer, DataBank
import random
import time
import logging

logging.basicConfig()
logging.getLogger('pyModbusTCP.server').setLevel(logging.DEBUG)

# server parameters
host = '0.0.0.0'
port = 502

# Initialize random generator
random.seed()

# Generate some random sensor data
def sensor_data():
    temp = random.randint(0,200)
    # temp = -100
    himid = random.randint(50,200)
    air_qual = random.randint(0,100)
    return temp, himid, air_qual

class piDataBank(DataBank):
    def __init__(self):
        super().__init__()

    def get_holding_registers(self, address, number=1, srv_info=None):
        # get sensor data
        temp, humid, air_qual = sensor_data()

        # set holding registers
        self._h_regs[0] = temp
        self._h_regs[1] = humid
        self._h_regs[2] = air_qual

        try:
            return[self._h_regs[i] for i in range(address, address+number)]
        except KeyError:
            return

if __name__ == '__main__':
    # create server
    Server = ModbusServer(host=host, port=port, data_bank=piDataBank())

    # run server
    Server.start()
