# Mac seems to only allow the asci bell to ring 5 times
# This function is so I can set the bell to sound in multiple sets of 5

import time

def alarm(n):
     i = 0
     while i < n:
             print("\a" * 5)
             time.sleep(4)
             i += 1
