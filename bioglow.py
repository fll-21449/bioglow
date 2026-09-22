from hub import light_matrix, port, motion_sensor
import motor
import motor_pair
import runloop

async def main():
    robot = Biofish()
    await robot.drive_forward(50)

WHEEL = 18 # circumference in cm

class Biofish:

    def __init__(self):
        motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
 
    async def drive_forward(self, cm):
        degrees = 360 * cm / WHEEL
        sp = motor.relative_position(port.E)
        print("start {}".format(self.yaw()))
        y = self.yaw()
        gp = sp + degrees
        while sp < gp:
            twist = self.yaw() - y
            twist = twist / 2
            if twist < -50:
                twist = -50
            if twist > 50:
                twist = 50
            motor_pair.move(motor_pair.PAIR_1,int(twist),velocity=300)
            sp = motor.relative_position(port.E)
            print("xxx {}".format(self.yaw()))
        motor_pair.stop(motor_pair.PAIR_1)

    def yaw(self):
        x = motion_sensor.tilt_angles()
        return x[0]

runloop.run(main())
