from threading import Thread
import time

def car(pilot, speed):
    space = 0
    while space <= 100:
        time.sleep(0.5)
        print(f'Pilot {pilot} is at position {space}.\n')
        space += speed


if __name__ == '__main__':
    thrdcar1 = Thread(target=car, args=['Pericles', 10])
    thrdcar2 = Thread(target=car, args=['Zapata', 20])
    thrdcar1.start()
    thrdcar2.start()
