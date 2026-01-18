def is_armstrong_number(number):
    """
    Checks if a given number is an Armstrong number.
    """
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
        
    if sum_of_powers == number:
        return True
    else:
        return False

num_to_check = 12

if is_armstrong_number(num_to_check):
    print(f"{num_to_check} is an Armstrong number.")
else:
    print(f"{num_to_check} is not an Armstrong number.")