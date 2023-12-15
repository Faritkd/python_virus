# Do not test it in your computer.

from rand_string.rand_string import RandString
import os

while True:
    try:
        os.mkdir(RandString("uppercase", 6))
    except FileExistsError:
        pass
