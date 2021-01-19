# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:31:59 2021

@author: Josh Stow
"""

# Import dependencies
import csv
import os



# Define lambda functions
clear = lambda: os.system('cls')



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

def getCheapest():
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
        
    input('\nPress enter to return to menu...')
    clear()
    
def extractSpecificLeaseYearData():
    """
    Create list of masts from dataset that have a lease of 25 years.
    
    Args:
        None

    Returns:
        extracted_data::[[str]]

    """
    DATASET = importData()  # Get dataset list
    extracted_data = [row for row in DATASET if int(row[9]) == 25]  # Comprehend list of items where lease years is 25

    return extracted_data

# Run code if file run from command line
if __name__ == '__main__':
    clear()
    
    # User input selection menu
    while True:
        print("""
Bink Python Developer Test | @author: Josh Stow
(1) Get data from the 5 masts with cheapeast rent prices\n
Select function from list...""")

        # Get user input,
        sel = input('\n> ')
        
        # Only accept int values
        try:
            sel = int(sel)
        except:
            clear()
            print('ERROR: Please only use integer values!')
            continue
        
        # Determine selection
        if sel == 1:
            clear()
            getCheapest()
        # Throw error if selected option doesnt exist
        else:
            clear()
            print('ERROR: Please select a valid function!')
            continue
        