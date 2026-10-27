from hub import light_matrix, port, motion_sensor, button
import motor
import motor_pair
import runloop


SPEED = 70

LEFT_ATTACHMENT = port.D
RIGHT_ATTACHMENT = port.C

async def main():
    # program_number = 0
    # wait until left or right button is pressed
    # if right, program_number is program_number + 1
    # update display to show symbol for program_number

    robot = Biofish()
    robot.reset_angle()

    # Make sure this matches the program number in the bottom right.
    PROGRAM_NUMBER = 4
    await runsel(PROGRAM_NUMBER, robot)

async def runsel(program_number, robot):
    if program_number == 1:
        await lidar_scan(robot)
    elif program_number == 2:
        await tractor(robot)
    elif program_number == 3:
        await keystone(robot)
    elif program_number == 4:
        await buzzcut(robot)
    elif program_number == 5:
        await forklift(robot)

async def newmain():
    print("hi")
    program_number = 0
    # wait until left or right button is pressed
    # if right, program_number is program_number + 1
    # update display to show symbol for program_number

async def lidar_scan(robot):
    await robot.drive_backward(66, speed = 40)# 67.6 #62
    await robot.turn_left(35, speed = 500, small_goal_diff=-10) # 35 degrees #40, speed = 500, small_goal_diff=-10
    await robot.turn_right(35)
    await robot.drive_forward(66)

async def tractor(robot):
    await motor.run_for_time(LEFT_ATTACHMENT, 200, 700)
    await robot.drive_forward(42, speed = 1100)
    #await robot.drive_backward(1.5, speed = 100)
    await motor.run_for_time(LEFT_ATTACHMENT, 800, -110)
    await runloop.sleep_ms(1000)
    await motor.run_for_time(LEFT_ATTACHMENT, 500, 200)
    await robot.drive_backward(39)

async def buzzcut(robot):
    await robot.drive_forward(29)
    await robot.turn_right(48)
    await robot.drive_forward(62)
    await robot.turn_left(46)
    await robot.drive_forward(2.5)
    await motor.run_for_time(RIGHT_ATTACHMENT, 500, -1100)
    #await motor.run_for_time(RIGHT_ATTACHMENT, 500, 1100)
    await robot.backwards(20)

async def keystone(robot):
    await robot.drive_forward(45)
    await robot.turn_left(40)
    await robot.drive_forward(25)
    await robot.turn_right(90)
    await robot.drive_forward(32)
    await motor.run_for_time(RIGHT_ATTACHMENT, 1000, -110)
    await robot.drive_backward(30)
    await robot.turn_right(45)
    motor.run_for_time(LEFT_ATTACHMENT, 2000, -110)
    await robot.drive_forward(30.2)
    await motor.run_for_time(LEFT_ATTACHMENT, 2000, 110)
    await motor.run_for_time(LEFT_ATTACHMENT, 1000, -110)
    await robot.drive_backward(21.5)
    await robot.turn_left(92)
    await motor.run_for_time(LEFT_ATTACHMENT, 150, 110)
    await robot.drive_forward(8)
    await motor.run_for_time(LEFT_ATTACHMENT, 2000, 110)
    await robot.drive_backward(12)
    await robot.turn_left(70)
    await robot.drive_forward(38)
    await robot.turn_right(120)
    await robot.drive_forward(23, speed = 20)
    await robot.drive_backward(20)
    motor.run_for_time(LEFT_ATTACHMENT, 2000, -110)
    await robot.turn_left(98)
    await robot.drive_backward(20)
    await robot.drive_forward(28)
    await robot.turn_left(45)
    await robot.drive_forward(31)
    await robot.turn_left(30)
    motor.run_for_time(LEFT_ATTACHMENT, 1000, 110)
    await robot.drive_forward(70)
    await robot.turn_left(30)
    await robot.drive_forward(40)

class Biofish:
    def __init__(self):
        self.wheel_circumference = 18 # cm
        # driving motors
        self.left_motor = port.A
        self.right_motor = port.E
        self.motor_pair = motor_pair.PAIR_1
        motor_pair.pair(self.motor_pair, self.left_motor, self.right_motor)

    def show_state(self):
        print("current angle: {} / angle goal: {}".format(self.get_yaw(), self.angle_goal))

    async def simple_drive_backward(self, distance, speed = SPEED):
        distance_in_degrees = int(distance * (360.0 / (self.wheel_circumference)))
        await motor_pair.move_for_degrees(self.motor_pair, -distance_in_degrees, 0, velocity = speed*10)

    # drive_forward tells the robot to drive in a
    # straight line "distance" centimeters forwards.
    async def drive_forward(self, distance, speed = SPEED):
        distance_in_degrees = distance * (360.0 / (self.wheel_circumference))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position + distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_circumference))
        while motor.relative_position(self.right_motor) < small_goal:
            motor_pair.move(self.motor_pair, self.correction(),velocity = speed*10)
        while motor.relative_position(self.right_motor) < goal_position:
            motor_pair.move(self.motor_pair, self.correction(),velocity = 100)
        motor_pair.stop(self.motor_pair)

    async def drive_backward(self, distance, speed = SPEED):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_circumference))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position - distance_in_degrees
        # plus sign before the seven used to be a minus sign
        small_goal = goal_position + 7 * (360.0 / (self.wheel_circumference))
        while motor.relative_position(self.right_motor) > small_goal:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -speed*10)
        while motor.relative_position(self.right_motor) > goal_position:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -100)
        motor_pair.stop(self.motor_pair)

    async def turn_left(self, degrees, speed = 25, small_goal_diff=20):
        if speed>50:
            speed = 50
        self.angle_goal = self.angle_goal + degrees
        small_goal = self.angle_goal - small_goal_diff
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
