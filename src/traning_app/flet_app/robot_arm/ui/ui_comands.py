from .robot_arm import RobotArm


def init_arm():    
    pass
    #robot.connection()    

# Pinzas
def gripper(position: int):
    #print("Gripper", position)    
    robot.move_arm_gripper(position=position)


# Muñeca
def wrist(position: int):
    #print("Wrist", position)
    robot.move_arm_wrist(position=position)


# Brazo arriba
def arm_top(position: int):
    #print("Arms", position)
    robot.move_arm_top(position=position)


# Brazo abajo
def arm_bottom(position: int):
    #print("Arms", position)
    robot.move_arm_botton(position=position)


# Hombros
def shoulders(position: int):
    #print("Shoulders", position)    
    robot.move_shoulders(position=position)


# Base
def base(position: int):
    #print("Base ui command", position)
    robot.move_base(position=position)


robot = RobotArm()
