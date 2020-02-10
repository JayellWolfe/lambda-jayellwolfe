""" lambdata - a collection of data science helper functions"""

import pandas as pd
import numpy as np

ones = pd.DataFrame(np.ones(10))
zeros = pd.DataFrame(np.zeros(50))


#max number function
def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > mum1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"



#divisible by ten function:

def divisible_by_ten(num):
    if(num % 10 == 0):
        return True
    else:
        return False
