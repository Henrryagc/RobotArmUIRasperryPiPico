from connect.connect_arduino import Connect
from typing import List

class ArduinoController(Connect):
    def __init__(self):
        super().__init__()
    

    def send_values(self, arm_data: List[int]):
        values_string = '-'.join(str(arm_value) for arm_value in arm_data)
        print(values_string.encode('utf-8'))
        # self.board.write(values_string.encode('utf-8'))
        