
import string

def wave(people):

    wave = []

    if people is None:
        return people

    for idx, l in enumerate(people):
        upped = people[idx].upper()
        waved = people[:idx] + upped + people[idx+1:]
        wave.append(waved)

    return wave
