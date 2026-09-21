from hub import light_matrix, port
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
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(degrees), 0)

runloop.run(main())
