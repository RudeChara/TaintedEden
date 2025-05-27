from random import randint


def receive_4d6():
    values = [randint(1, 6) for _ in range(4)]
    return sum(values) - min(values)


def generate():
    characteristics = [receive_4d6() for _ in range(6)]
    while sum(characteristics) < 68 or sum(characteristics) > 76:
        characteristics = [receive_4d6() for _ in range(6)]
    return characteristics
