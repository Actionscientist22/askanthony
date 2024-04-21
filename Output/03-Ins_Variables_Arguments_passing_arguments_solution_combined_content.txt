""" Passing Arguments"""

# 1a. Positional arguments.
def positional(x, y):
    """This function adds two positional arguments,
    adds them and prints the total"""
    total = x + y
    print(f"The total is: {total}")

if __name__ == "__main__":
    positional(5,12)

# 1b. Positional arguments.
def savings(balance, apr, days):
    """This function adds two positional arguments,
    adds them and prints the total"""
    interest_rate = (apr/100) * (days/365)
    interest_earned = balance * interest_rate
    balance += interest_earned
    print(f"The new balance is: {balance}")

if __name__ == "__main__":
    # Incorrect order.
    savings(5, 31, 50000)
    # Correct order
    # savings(50000, 3, 31)

# 2. Keyword arguments.
def keyword(a, b, c):
    """This function takes three keyword arguments,
    adds them, and prints the total"""
    total = a + b + c
    print(f"The total is: {total}")

if __name__ == "__main__":
    keyword(a=-3, c=10, b=5)

# 3. Keyword and positional arguments
def pos_key_args(a, b, c):
    """This function takes one positional argument
    and two keyword arguments, adds them, and prints the total"""
    total = a + b + c
    print(f"The total is: {total}")

if __name__ == "__main__":
    pos_key_args(42, b=-10, c=5)
    # pos_key_args(b=-10, c=5, 42) uncomment this line and run again.

# 4. Iterable unpacking arguments
def iterable(a, b, c):
    """This function takes an iterable (list of tuple)
    and adds the values in the iterable, and prints the total"""
    total = a + b + c
    print(f"The total is: {total}")

if __name__ == "__main__":
    tuple_values = (5, -10, 7)
    list_values = [7, 23, -11]
    iterable(*tuple_values)
    iterable(*list_values)

# 5. Dictionary unpacking arguments.
def dictionary(a, b, c):
    """This function takes an iterable (list of tuple)
    and adds the values in the iterable, and prints the total"""
    total = a + b + c
    print(f"The total is: {total}")

if __name__ == "__main__":
    dict_values = {'b': -4, 'c': 100, 'a':-42 }
    dictionary(*dict_values) # returns the keys
    dictionary(**dict_values) # returns the values
