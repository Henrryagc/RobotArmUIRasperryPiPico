from time import sleep

import serial


class RobotArm:

    def __init__(self) -> None:


        self.ROBOT_GRIPPER = 5

        self.ROBOT_WRIST = 4

        self.ROBOT_ARM_TOP = 3

        self.ROBOT_ARM_BOTTOM = 2

        self.ROBOT_SHOULDERS = 1

        self.ROBOT_BASE = 0

        # Arduino config

        try:

            print("Connect to Arduino One, Wait please...!")

            self.board = serial.Serial('COM3', 9800, timeout=.1)

            sleep(2)

            print("Connected...") 

        except:

            print("Connection error...")



    def connection(self):

        self.board.write(b'0')



    def move_base(self, position: int):        

        #self.board.digital[3].write(position)

        # self.board.write(position.encode('UTF-8'))

        self.board.write(self.__encode_data(self.ROBOT_BASE, position))
        #sleep(0.05)
        data = self.board.readline()
        print("DECODE DATA: ", data.decode("utf-8"))
        print(f"base {position}")



    def move_shoulders(self, position: int):

        #self.board.digital[4].write(position)        

        #self.board.digital[5].write(position)

        #self.board.write(position.encode('UTF-8'))                

        self.board.write(self.__encode_data(self.ROBOT_SHOULDERS, position))

        print(f"Shoulders {position}")



    def move_arm_botton(self, position: int):

        #self.board.digital[6].write(position)

        #self.board.write(position.encode('UTF-8'))

        self.board.write(self.__encode_data(self.ROBOT_ARM_BOTTOM, position))

        print(f"Arm bottom {position}")



    def move_arm_top(self, position: int):

        #self.board.digital[7].write(position)

        #self.board.write(position.encode('UTF-8'))

        self.board.write(self.__encode_data(self.ROBOT_ARM_TOP, position))

        print(f"Arm top {position}")



    def move_arm_wrist(self, position: int):

        #self.board.digital[8].write(position)

        #self.board.write(position.encode('UTF-8'))

        self.board.write(self.__encode_data(self.ROBOT_WRIST, position))

        print(f"Wrist  {position}")



    def move_arm_gripper(self, position):

        #self.board.digital[9].write(position)

        #self.board.write(self.__encode_data(2,2))

        self.board.write(self.__encode_data(self.ROBOT_GRIPPER, position))

        print(f"Gripper  {position}")



    def __encode_data(self, robot_part: int, position: int) -> bytes:
        print(f'ENCODE DATA {robot_part},{position}'.encode('UTF-8'))
        return f'{robot_part},{position}'.encode('UTF-8')

