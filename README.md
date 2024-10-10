# functions
# functions hide complexity
# functions abstraction
from time import sleep

def sigma(message):
    for letter in message:
        sleep(0.1)
        print(letter, end="")

sigma("jsdhvgjka")  
