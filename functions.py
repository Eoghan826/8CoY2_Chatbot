# functions
# functions hide complexity
# functions abstraction
from time import sleep

def sigma(message):
    for letter in message:
        sleep(uniform(0.03,0.1))
        print(letter, end="")
    print()

sigma("jsdhvgjka")
