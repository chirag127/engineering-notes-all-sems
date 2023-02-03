## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

Here is a sample code in Python for converting temperature from Centigrade to Fahrenheit:
```
def convert_to_fahrenheit(centigrade):
  fahrenheit = (9/5)*centigrade + 32
  return fahrenheit

centigrade = float(input("Enter temperature in Centigrade: "))
fahrenheit = convert_to_fahrenheit(centigrade)
print("Temperature in Fahrenheit:", fahrenheit)
```
