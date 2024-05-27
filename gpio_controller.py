import time

import serial

from logger import logger

arduino_port = "COM4"
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)


def send_command(command):
    ser.write(command.encode())


def turn_on_classroom_light():
    """
    將教室的電燈打開
    """
    send_command("0")
    logger.info("Turn on the light in the classroom")
    return {"succeed": True}


def turn_on_lab_light():
    """
    將實驗室的電燈打開
    """
    send_command("1")
    logger.info("Turn on the light in the lab")
    return {"succeed": True}


def turn_off_classroom_light():
    """
    將教室的電燈關閉
    """
    send_command("2")
    logger.info("Turn off the light in the classroom")
    return {"succeed": True}


def turn_off_lab_light():
    """
    將實驗室的電燈關閉
    """
    send_command("3")
    logger.info("Turn off the light in the lab")
    return {"succeed": True}
