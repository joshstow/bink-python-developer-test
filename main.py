# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:31:59 2021

@author: Josh Stow
"""

# Import dependencies
import csv

def importData():
    """
    Read data from csv into list.
    
    Args:
        None
        
    Returns:
        data::list

    """
    with open('dataset.csv', 'r') as f:
        reader = csv.reader(f)  # Instantiate csv reader obj
        data = [row for row in reader]  # Comprehend list of rows from csv
        del data[0] # Remove header row
        
        return data
    
def sortList(dataset):
    """
    Sort list in ascending order of current rent price.
    
    Args:
        dataset::[[str]]

    Returns:
        sorted_data::[[str]]

    """
    sorted_data = sorted(dataset, key=lambda x:int(float(x[10])))   # Sort with key of current rent price

    return sorted_data

def getFiveCheapest(sorted_data):
    """
    Get first five items from list sorted by rent price in ascending order.
    
    Args:
        sorted_data::[[str]]

    Returns:
        None

    """
    cheapest_five = sorted_data[:5]
    for item in cheapest_five:
        print(item)

# Run code if file run from command line
if __name__ == '__main__':
    
    DATASET = importData()
    #print(DATASET)  # Debugging
    sorted_data = sortList(DATASET)
    #print(sorted_data) # Debugging
    getFiveCheapest(sorted_data)
    