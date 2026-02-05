#TempConvert.py
#Name: Emma Barnes
#Date: 02/05/2026
#Assignment: Temperature Conversion


def main():
  #Prompt the user for a Fahrenheit temperature
  
  #Convert that temperature to celsius, rounding to 1 decimal percision
 
  #Output converted temperature.
  tempF = int(input("Enter a temperature in Fahrenheit: "))

  tempC = (tempF - 32)/1.8
  tempC = round(tempC, 1)

  print(tempF, "degrees fahrenheit is", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
