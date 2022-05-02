import math
def beeramid(bonus, price):
    # Formula for the number of beer cans you can purchase
    number_of_cans = math.floor(bonus/price)
    
    # Calculate the number of levels given the number of beer cans  
    levels = 0
    preceeding_non_squared_value = 0
    while True: 
        preceeding_non_squared_value += 1
        if number_of_cans - (preceeding_non_squared_value*preceeding_non_squared_value) >= 0: 
            levels += 1
            number_of_cans = number_of_cans - (preceeding_non_squared_value*preceeding_non_squared_value)
        else: 
            break
    return levels
