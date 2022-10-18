#Kevin Brinke R01423368
#Q1

#Convert from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):  
    fahrenheit = (9 / 5) * celsius + 32
    #print(fahrenheit,"F")
    return fahrenheit

#Convert from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    #print(celsius,"C")
    return celsius


#wasn't sure just did this instead of user prompting, didnt call for it
cToF1 = celsiusToFahrenheit(40.0)
cToF2 = celsiusToFahrenheit(39.0)
cToF3 = celsiusToFahrenheit(32.0)
cToF4 = celsiusToFahrenheit(31.0)

fToC1=fahrenheitToCelsius(120.0)
fToC2=fahrenheitToCelsius(110.0)
fToC3=fahrenheitToCelsius(40.0)
fToC4=fahrenheitToCelsius(30.0)


#wasnt sure, but i did it exactly as displayed
print("Celsius     Fahrenheit  |   Fahrenheit    Celcius\n")
print("40.0       ",format(cToF1,".1f"),"      |   120.0        ",format(fToC1,".2f"))
print("39.0       ",format(cToF2,".1f"),"      |   110.0        ",format(fToC2,".2f"),"\n...")
print("32.0       ",format(cToF3,".1f"),"       |   40.0         ",format(fToC3,".2f"))
print("31.0       ",format(cToF4,".1f"),"       |   30.0         ",format(fToC4,".2f"))
