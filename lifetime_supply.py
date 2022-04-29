"""
Ever wonder how much a "lifetime supply" of your favorite snack is? Wonder no more!

Write a function named calculate_supply that:
* takes 2 arguments: age, amount per day.
* calculates the amount consumed for rest of the life (based on a constant max age of 81).
* returns the result
"""

# This def statement may be incomplete...
def calculate_supply(age, amount_per_day):
    """
    >>> calculate_supply(80, 1)
    365
    >>> calculate_supply(80, 2)
    730
    >>> calculate_supply(36, 3)
    49275

    >>> calculate_supply(37, 2.17)
    34850
    """
    total_supply = 0
    amount_per_year = amount_per_day * 365
    max_age = 81
    while age < max_age:
        total_supply = total_supply + amount_per_year
        age = age + 1
    return round(total_supply)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# print(calculate_supply(36, 3))
# print(calculate_supply(37, 2.17))
# print(type(calculate_supply(36, 3)))