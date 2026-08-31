from hub import port
import motor_pair, color_sensor
import runloop

async def main():
    # Follow the green line.
    steering = 50
    velocity = 150
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    while True:
        while color_sensor.reflection(port.F) > 40:
            motor_pair.move(motor_pair.PAIR_1, steering, velocity = velocity)
        motor_pair.move(motor_pair.PAIR_1, -steering, velocity = velocity)
    motor_pair.stop(motor_pair.PAIR_1)


runloop.run(main()