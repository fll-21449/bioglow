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
 
    PROGRAM_NUMBER = 1
    if PROGRAM_NUMBER == 1:
        await lidar_scan(robot)
    elif PROGRAM_NUMBER == 2:
        await tractor(robot)

async def newmain():
    print("hi")
    program_number = 0
    # wait until left or right button is pressed
    # if right, program_number is program_number + 1
    # update display to show symbol for program_number


async def lidar_scan(robot):
    await robot.drive_backward(67.6, speed = 40)
    await robot.turn_left(35, speed = 40)
    await robot.turn_right(33)
    await robot.drive_forward(70)

async def tractor(robot):
    await robot.drive_forward(41, speed = 40)
    await motor.run_for_time(LEFT_ATTACHMENT, 500, -1110)

async def forklift(robot):
    await robot.drive_forward(1)
    await robot.turn_right(45)
    await robot.drive_forward(1)
    await robot.drive_backward(1)
    # todo

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
