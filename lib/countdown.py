# your code goes here!
import time 
def countdown(n):
    while n > 0:
        print(f'{n} SECONDS(S)!')
        n -= 1
    print("HAPPY NEW YEAR!")
    

def countdown_with_sleep(n):
    while n > 0:
        print(f'{n} SECONDS(S)!')
        n -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

