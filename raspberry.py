from logger import logger


def turn_on_classroom_light():
    """
    將教室的電燈打開
    """
    logger.info("Turn on the light in the classroom")
    return {"succeed": True}


def turn_on_lab_light():
    """
    將實驗室的電燈打開
    """
    logger.info("Turn on the light in the lab")
    return {"succeed": True}


def turn_off_classroom_light():
    """
    將教室的電燈關閉
    """
    logger.info("Turn off the light in the classroom")
    return {"succeed": True}


def turn_off_lab_light():
    """
    將實驗室的電燈關閉
    """
    logger.info("Turn off the light in the lab")
    return {"succeed": True}
