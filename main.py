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
    
def sortList():
    """
    Sort list in ascending order of current rent price.
    
    Args:
        None

    Returns:
        sorted_data::[[str]]

    """
    DATASET = importData()  # Get dataset list
    sorted_data = sorted(DATASET, key=lambda x:int(float(x[10])))   # Sort with key of current rent price

    return sorted_data

def getFiveCheapest():
    """
    Get first five items from list sorted by rent price in ascending order.
    
    Args:
        None

    Returns:
        None

    """
    sorted_data = sortList() # Get sorted dataset list
    cheapest_five = sorted_data[:5] # Isolate first 5 items
    
    # Print items to console
    for item in cheapest_five:
        print(f'\n{item}')
        
    input('Press enter to return to menu...')



# Run code if file run from command line
if __name__ == '__main__':
    # User input selection menu
    while True:
        
        print("""
Bink Python Developer Test | @author: Josh Stow
(1) Get data from the 5 masts with cheapeast rent prices\n
Select function from list...""")

        # Get user input, only accept int values
        try:
            sel = int(input('> '))
        except:
            print('Error: Please select a valid function')
            continue
        
        # Determine selection
        if sel == 1:
            getFiveCheapest()
        # Throw error if selected option doesnt exist
        else:
            print('Error: Please select a valid function')
            continue
        
    