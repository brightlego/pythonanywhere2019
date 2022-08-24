import numpy as np

def wrapper():
    input_data = np.array([1,3,4,7])
    output = doubled(input_data) + squared(input_data)
    return(output)

def doubled(input_data):
    doubled_input = 2*input_data
    return(doubled_input)

def squared(input_data):
    squared_input = input_data**2
    return(squared_input)