#from hub import port
#import color_sensor
#lightness = color_sensor.reflection(port.F)
#print(lightness)

# from hub import port
# import motor_pair
# import runloop
# async def main():
#     distance = 200
#     velocity = -1000
#     steering = -50
#     motor_pair. pair(motor_pair.PAIR_1, port.E, port.A)
#     await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance, steering, velocity = velocity)
# runloop.run(main())

from hub import port
import runloop
import color_sensor
import motor_pair
async def main():
        mid = 71 # change this to be halfway between white and black.
        motor_pair.pair(motor_pair. PAIR_1, port.A, port.E)
        for i in range(100):
            lightness = color_sensor.reflection(port.F)
            if lightness > mid:
                 motor_pair.move(motor_pair.PAIR_1, -25, velocity = 100)
                #return
            else:
                motor_pair.move(motor_pair.PAIR_1, 25, velocity = 100)
                print("keep going!")
            await runloop.sleep_ms(100)
            #await motor_pair.move_for_degrees(motor_pair.PAIR_1, 45, 0, velocity = 300)
runloop.run(main())
