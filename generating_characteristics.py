from random import randint


def value_4d6():
    values = [randint(1, 6) for _ in range(4)]
    return sum(values) - min(values)


def generate():
    characteristics = [value_4d6() for _ in range(6)]
    while not 68 <= sum(characteristics) <= 76 or len(list(filter(lambda x: x >= 15, characteristics))) == 0:
        characteristics = [value_4d6() for _ in range(6)]
    return characteristics
