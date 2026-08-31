from hub import light_matrix, motion_sensor, port
import motor_pair
import runloop
import math 
import motor 

SPEED = 90

PROGRAM_NUMBER = 1

async def main():
    robot = Kraken()
    robot.reset_angle()
    front_motor = port.F
    back_motor = port.D 

    if PROGRAM_NUMBER == 1:
        await pickaxe(robot, front_motor)
    elif PROGRAM_NUMBER == 2:
        await whale_feeder(robot, back_motor, front_motor)
    elif PROGRAM_NUMBER == 3:
        await traverse_map(robot, back_motor)
    elif PROGRAM_NUMBER == 4:
        await top_left(robot, front_motor)
    elif PROGRAM_NUMBER == 5:
        await boat(robot)
    elif PROGRAM_NUMBER == 6:
        await shark_squid_express(robot, back_motor)
    elif PROGRAM_NUMBER == 0:
        await test_run(robot, back_motor)

async def test_run(robot, attachment_motor):
    await robot.drive_forward(30)
    await robot.turn_left(90)
    await robot.drive_backward(30)
    await robot.turn_right(90)
    await motor.run_for_degrees(attachment_motor, 180, 600)

async def pickaxe(robot, attachment_motor2):
    await robot.drive_forward(43)
    await motor.run_for_degrees(attachment_motor2, 70, 910)
    await wait_for_seconds(1)
    await robot.turn_left(30)
    await robot.drive_backward(17)
    await robot.turn_left(30)
    await motor_pair.move_for_degrees(robot.motor_pair, 300, 0, velocity = 1500)
    await robot.drive_backward(13)
    await robot.turn_left(10)
    await robot.drive_backward(13)
    await robot.turn_left(15)
    await robot.drive_backward(33)
    await robot.turn_left(50)

async def whale_feeder(robot, attachment_motor, soanar_motor):
    await robot.drive_forward(40)
    await robot.turn_left(45, speed=25)
    await robot.drive_forward(15)
    await robot.turn_right(90, speed=25)
    await robot.drive_forward(36,speed=70)
    # this is where it hits the whale
    #attachment_motor.run_for_seconds(2, 70)
    #added shipping lanes to whale feeder
    await robot.drive_backward(15)
    await robot.turn_left(90, speed=25)
    await motor.run_for_degrees(soanar_motor, 180, 1002)
    await robot.drive_forward(7)
    # lined up with shipping lanes
    await motor.run_for_degrees(attachment_motor, 180, 550)
    await robot.drive_backward(7, speed = 15)
    await motor.run_for_degrees(attachment_motor, -100, 1110)
    await robot.drive_forward(6)
    await robot.turn_right(45, speed=25)
    await robot.drive_backward(47)
    await robot.turn_left(45, speed=25)
    await robot.drive_backward(26)

async def traverse_map(robot, attachment_motor):
    await robot.drive_forward(25)
    await robot.turn_left(33)
    await robot.drive_forward(56)
    await motor.run_for_degrees(attachment_motor, 900, 1110)
    robot.reset_angle()
    await robot.drive_backward(11)
    await robot.turn_left(60, speed=25)
    await robot.drive_forward(56)
    await robot.turn_right(15, speed = 25)
    await robot.drive_forward(28)
    await robot.turn_left(47, speed=25)
    await robot.drive_forward(30)
    await robot.turn_left(40, speed=25)
    await robot.drive_forward(55)
    
async def top_left(robot, attachment_motor2):
    await robot.drive_forward(23)
    await robot.turn_right(30)
    await robot.drive_forward(35)
    await robot.turn_left(120)
    # get scuba diver :-)
    await motor.run_for_degrees(attachment_motor2, 100, 550) 
    await wait_for_seconds(1)
    await robot.drive_forward(11)
    await motor.run_for_degrees(attachment_motor2, -60, 1110)   
    # flip coral buds up
    await robot.drive_backward(27)
    #raise the mast
    await robot.drive_forward(20)
    await robot.turn_right(45)
    await robot.drive_forward(15)
    #hit the shark
    await robot.drive_backward(13)
    await robot.turn_right(45)
    await robot.drive_forward(22)
    #cora reef
    await robot.drive_backward(50)
    await robot.turn_right(45)
    await robot.drive_backward(57)

async def boat(robot):
    await robot.drive_forward(12,speed = 20)
    await wait_for_seconds(1)
    await robot.drive_backward(20)

async def shark_squid_express(robot, attachment_motor):
    await robot.drive_forward(80)
    await robot.drive_backward(16, speed = 10)
    await robot.turn_left(40)
    await robot.drive_forward(30)
    await robot.turn_left(20)
    await robot.drive_forward(13)
    await motor.run_for_degrees(attachment_motor, -150, 1110)         


async def wait_for_seconds(s):
    await runloop.sleep_ms(s*1000)

class Kraken:
    def __init__(self):
        self.wheel_diameter = 5.5 # cm
        self.left_motor = port.A
        self.right_motor = port.B 
        self.motor_pair = motor_pair.PAIR_1
        motor_pair.pair(self.motor_pair, self.left_motor, self.right_motor)

    def show_state(self):
        print("current angle: {} / angle goal: {}".format(self.get_yaw(), self.angle_goal))

        
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
