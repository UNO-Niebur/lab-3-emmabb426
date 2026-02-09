#ApproxPi.py
#Name: Emma Barnes
#Date: 02/08/2026
#Assignment: Approximate Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  DecPrec = int(input("To what decimal precision do you want me to round Pi? (1-10): "))
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, DecPrec) != round(realPi, DecPrec):
    print(approxPi)
    approxPi = approxPi +(sign * 4/denom)

    sign = sign * -1
    denom = denom +2

  
  end = time.time()

  elapsedTime = end - start
  print("Time elapsed:", elapsedTime)

if __name__ == '__main__':
  main()
