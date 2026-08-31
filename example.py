import motor_pair
import runloop
import color_sensor
from hub import port, light_matrix, button
import motor

right_motor = port.A
left_motor = port.E
front = port.C
back = port.D

rightlight = port.B
leftlight = port.F

tile = 80
grout = 40

# reflectivity
black = 40
white = 100

mid = int((black + white) / 2)

drive_time = 15000 # milliseconds
interval = 50 # milliseconds
steps = int(drive_time / interval)

MODE_TWO_SENSORS = 1
MODE_ONE_SENSOR = 2

light_matrix.show_image(light_matrix.IMAGE_MEH)
mode = 0
while mode == 0:
    if button.pressed(button.LEFT):
        mode = MODE_TWO_SENSORS
    if button.pressed(button.RIGHT):
        mode = MODE_ONE_SENSOR
if mode == MODE_TWO_SENSORS:
    light_matrix.show([100,0,0,0,100]*5)
else:
    light_matrix.show([0,0,100,0,0]*5)

async def main():
    drive_pair = motor_pair.PAIR_1

    motor_pair.pair(drive_pair, left_motor, right_motor)

    # Note: the robot is going backwards, so it's using the left light sensor to follow the right edge of a black line.
    for i in range(steps):
        dir = 0
        if mode == MODE_TWO_SENSORS:
            l = int(color_sensor.reflection(leftlight))
            r = int(color_sensor.reflection(rightlight))
            if l < mid:
                dir -= (mid - l)
            if r < mid:
                dir += (mid - r)
        else:
            l = int(color_sensor.reflection(leftlight))
            dir = l - mid

        ad = abs(dir)
        speed = 150 - abs(dir)
        if speed < 50:
            speed = 50

        # Move straight at default velocity
        motor_pair.move(drive_pair, dir, velocity=-speed)

        await runloop.sleep_ms(interval)

    light_matrix.show([100,0,0,0,100, 0,100,0,100,0, 0,0,100,0,0, 0,100,0,100,0, 100,0,0,0,100])
    motor_pair.stop(drive_pair)

    for i in range(4):
        motor.run(front, 100)
        motor.run(back, 100)
        await runloop.sleep_ms(500)
        motor.run(front, -100)
        motor.run(back, -100)
        await runloop.sleep_ms(500)
    motor.stop(front)
    motor.stop(back)

runloop.run(main())