"""
How can we communicate the highs and lows of climate change with people who use a different temperature unit? 
Let's make a temperature converter based on the steps here: 
https://www.mathsisfun.com/temperature-conversion.html

Create a function called celsius_to_fahrenheit that:
* takes a single argument, the temperature in celsius
* calculates and returns the fahrenheit equivalent

Similarly, create another function called fahrenheiht_to_celsius that:
* takes a single argument, the temperature in fahrenheit
* calculates and returns the celsius equivalent
"""

# This def statement may be incomplete...
def celsius_to_fahrenheit(c):
    """
    c -- celsius temperatur
    f -- fahrenheit temperatur
    """
    f = (c // 5 * 9) + 32
    return f
    
# This def statement may be incomplete...
def fahrenheit_to_celsius(f):
    """
    f -- fahrenheit temperatur
    c -- celsius temperatur
    """
    c = (f - 32) * 5 // 9
    return c

help(celsius_to_fahrenheit)
help(fahrenheit_to_celsius)

