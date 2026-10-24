from hub import light_matrix, motion_sensor, port
import motor_pair
import runloop
import math
import motor

SPEED = 70

PROGRAM_NUMBER = 3

async def main():
    robot = jones()
    robot.reset_angle()
    front_motor = port.A
    back_motor = port.D

    if PROGRAM_NUMBER == 1:
        await the_flyswatter(robot, back_motor)
    elif PROGRAM_NUMBER == 2:
        #await millstone(robot, front_motor)
        await gold_digger(robot, back_motor)
        #await flyswater2(robot,front_motor)
    elif PROGRAM_NUMBER == 3:
        await the_hammer_thing(robot,front_motor,back_motor)
    elif PROGRAM_NUMBER == 4:
        await shipwreck(robot, back_motor)
    elif PROGRAM_NUMBER == 5:
        await earthmover(robot,front_motor, back_motor)
    elif PROGRAM_NUMBER == 6:
        await delivery(robot)
    elif PROGRAM_NUMBER == 7:
        await bulldozer(robot)



async def the_flyswatter(robot, back_motor): # yellow thing on the back left wheel on the 2nd thick line
    await robot.drive_forward(13)
    await robot.turn_left(50)
    await robot.drive_forward(20)
    await robot.turn_right(60)
    await robot.drive_forward(42)

    await robot.turn_left(102)
    # await motor.run_for_degrees(port.B,-360,100)

    await robot.drive_forward(4)
    await robot.turn_right(90)
    await robot.drive_backward(15) #drives straight back thing
    await robot.turn_right(22)
    await robot.drive_backward(13)
    await robot.turn_right(19)
    await robot.drive_backward(17.4,speed=100)
    await robot.turn_right(80)
    await motor.run_for_degrees(back_motor, 400, 1000)
    #await robot.turn_left(40)
    #await robot.turn_right(40)
    # await motor.run_for_degrees(port.B,-360,100)
    await motor.run_for_degrees(port.B,200,1000)
    await robot.drive_forward(30)
    await robot.turn_left(45)
    await robot.drive_forward(35)

async def the_hammer_thing (robot,front_motor,back_motor):
    await robot.drive_forward(20.5)
    await motor.run_for_degrees(front_motor, -155, 1000)
    await robot.drive_forward(14)#34.5
    await motor.run_for_degrees(front_motor, 155, 1000)
    await motor.run_for_degrees(front_motor, -155, 1000)
    await motor.run_for_degrees(front_motor, 155, 1000)
    await motor.run_for_degrees(front_motor, -155, 1000)
    #await motor.run_for_degrees(front_motor, 155, 1000)
    #await motor.run_for_degrees(front_motor, -155, 1000)
    await robot.drive_forward(3.5)
    await robot.turn_left(35)
    await robot.drive_forward(42.5)
    await robot.turn_left(55)
    await robot.drive_forward(12.8)
    await robot.turn_right(45)
    await robot.simple_drive_backward(14)
    await robot.drive_forward(12)
    await robot.turn_left(45)
    await robot.drive_forward(37.5)
    await robot.turn_left(4)# added to fix getting stuck
    await motor.run_for_time(front_motor, 1000, 300)
    await robot.turn_left(10)
    await robot.drive_forward(10)
    await robot.turn_right(13)
    await motor.run_for_degrees(front_motor, -140, 950)
    await robot.drive_backward(5)
    await motor.run_for_time(front_motor, 500, -950)
    await robot.drive_forward(5)
    await robot.turn_left(10)
    await robot.drive_forward(53, speed=105)
    await robot.turn_left(70)
    # await robot.drive_forward(17, speed=105)
    # await motor.run_for_degrees(back_motor, 105, 1100)
    # await motor.run_for_degrees(back_motor, -30, 1100)
    # await robot.turn_left(10)
    # await robot.turn_right(10)
    # await robot.drive_forward(33, speed=105)
    # await robot.turn_left(90)
    await robot.simple_drive_forward(58, speed = 105)

async def millstone(robot, front_motor):
    await robot.drive_forward(17.5)
    await robot.turn_right(45)
    await robot.drive_forward(29)
    await robot.turn_left(45)
    await robot.drive_forward(24)
    await motor.run_for_degrees(front_motor, -20, 500)
    await robot.drive_forward(10)
    await motor.run_for_degrees(front_motor, 150, 1000)
    
async def gold_digger(robot, back_motor):
    motor.run(back_motor, -10)
    await robot.drive_forward(57)
    motor.stop(back_motor)
    await motor.run_for_degrees(back_motor, 30, 700)
    for i in range(6):
        motor.run(back_motor, 10)
        await robot.simple_drive_backward(4)
        await robot.simple_drive_forward(4)
    await motor.run_for_degrees(back_motor, -60, 1000)
    motor.run(back_motor, -10)
    await robot.drive_backward(57)


async def flyswater2(robot,front_motor):
    await motor.run_for_time(front_motor, 1000, 950)

   





async def shipwreck(robot, back_motor): 
    await robot.drive_backward(40) 
    await robot.drive_forward(5) 
    await robot.drive_backward(13)
    await motor.run_for_degrees(back_motor, 100, 500)
    await robot.drive_forward(2)
    await robot.turn_right(2)
    await robot.drive_forward(11)
    await robot.turn_right(5)
    await robot.drive_forward(37, speed=100)

async def delivery(robot):
    await robot.drive_backward(21)
    await robot.turn_right(30)
    await robot.drive_backward(30)
    await robot.drive_forward(7)

    #await robot.drive_backward(41)
    #await robot.drive_forward(10)
    #await robot.drive_backward(17)
    #await robot.drive_forward(16)
    #await robot.turn_right(10)

    # await robot.drive_backward(35)
    # await robot.drive_forward(3)
    # await robot.drive_backward(18)
    # await robot.drive_forward(3)
    # await robot.turn_right(5)
    # await robot.drive_forward(43)

async def bulldozer(robot, front_motor):
    await robot.drive_forward(51)
    await robot.turn_right(50)
    await robot.drive_forward(30)
    await motor.run_for_time(front_motor, 15000, 1110)
    return
    await robot.drive_backward(9)
    await robot.turn_right(90)
    await robot.drive_forward(15)
    await robot.turn_left(5)

async def earthmover_motor (front_motor, back_motor):
    await motor.run_for_time(front_motor,1500,-500)
    await motor.run_for_degrees(back_motor, -70, 300)


async def earthmover (robot, front_motor, back_motor): #back right weel on 3rd bold line.
    a = earthmover_motor (front_motor, back_motor)
    b = robot.drive_forward(62.4)
    runloop.run(a,b)
    await robot.turn_left(46)
    await robot.drive_forward(13)
    await motor.run_for_degrees(front_motor, 50, 1100)
    await robot.drive_backward(8.5)
    await robot.turn_right(45)
    await motor.run_for_degrees(back_motor, 140, 300)
    await motor.run_for_degrees(back_motor, -80, 1025)
    #await robot.drive_backward(8.5)
    #await robot.turn_right(45)
    await robot.drive_backward(70)
    # await robot.turn_right(51)
    # await robot.drive_backward(18)
   # await motor.run_for_degrees(front_motor, -51, 100)
   # await robot.turn_left(12)
   # await robot.drive_backward(25)
   # await robot.turn_right(50)
   # await robot.drive_backward(30)

async def wait_for_seconds(s):
    await runloop.sleep_ms(s*1000)

class jones:
    def __init__(self):
        self.wheel_diameter = 5.5 # cm
        # driving motors
        self.left_motor = port.C
        self.right_motor = port.B
        self.motor_pair = motor_pair.PAIR_1
        motor_pair.pair(self.motor_pair, self.left_motor, self.right_motor)

    def show_state(self):
        print("current angle: {} / angle goal: {}".format(self.get_yaw(), self.angle_goal))

    async def simple_drive_backward(self, distance, speed = SPEED):
        distance_in_degrees = int(distance * (360.0 / (self.wheel_diameter * math.pi)))
        await motor_pair.move_for_degrees(self.motor_pair, -distance_in_degrees, 0, velocity = speed*10)
 
    async def simple_drive_forward(self, distance, speed = SPEED):
        distance_in_degrees = int(distance * (360.0 / (self.wheel_diameter * math.pi)))
        await motor_pair.move_for_degrees(self.motor_pair, distance_in_degrees, 0, velocity = speed*10)





    # drive_forward tells the robot to drive in a
    # straight line "distance" centimeters forwards.
    async def drive_forward(self, distance, speed = SPEED):
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position + distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_diameter * math.pi))
        while motor.relative_position(self.right_motor) < small_goal:
            motor_pair.move(self.motor_pair, self.correction(),velocity = speed*10)
        while motor.relative_position(self.right_motor) < goal_position:
            motor_pair.move(self.motor_pair, self.correction(),velocity = 100)
        motor_pair.stop(self.motor_pair)

    async def drive_backward(self, distance, speed = SPEED):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position - distance_in_degrees
        # plus sign before the seven used to be a minus sign
        small_goal = goal_position + 7 * (360.0 / (self.wheel_diameter * math.pi))
        while motor.relative_position(self.right_motor) > small_goal:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -speed*10)
        while motor.relative_position(self.right_motor) > goal_position:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -100)
        motor_pair.stop(self.motor_pair)

    async def turn_left(self, degrees, speed = 25):
        if speed>50:
            speed = 50
        self.angle_goal = self.angle_goal + degrees
        small_goal = self.angle_goal - 20
        motor_pair.move_tank(self.motor_pair, -speed*10, speed*10)
        while self.get_yaw()<small_goal:
            # wait
            True
        motor_pair.move_tank(self.motor_pair, -100, 100)
        while self.get_yaw()<self.angle_goal:
            True
        motor_pair.stop(self.motor_pair)

    async def turn_right(self, degrees, speed = 25):
        if speed>50:
            speed = 50
        self.angle_goal = self.angle_goal - degrees
        small_goal = self.angle_goal + 20
        motor_pair.move_tank(self.motor_pair, speed*10, -speed*10)
        while self.get_yaw()>small_goal:
            # wait
            True
        motor_pair.move_tank(self.motor_pair, 100, -100)
        while self.get_yaw()>self.angle_goal:
            True
        motor_pair.stop(self.motor_pair)

    def correction(self):
        correction = self.get_yaw() - self.angle_goal
        correction *= 5
        if correction < -50:
            correction = -50
        if correction > 50:
            correction = 50
        return int(correction)

    # reset_angle tells the robot that it is currently facing
    # the right direction. Call this at the beginning of each
    # program and after the robot squares itself up on an
    # object.
    def reset_angle(self):
        self.angle_goal = 0
        motion_sensor.reset_yaw(0)

    def get_yaw(self):
        yaw, _, _ = motion_sensor.tilt_angles()
        return yaw/10

runloop.run(main())
