import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    a=0
    # Write code here
    for i in range(len(x)):
       a+=x[i]*y[i]
    return float(a) 
    pass