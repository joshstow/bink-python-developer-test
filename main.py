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
    sorted_data = sorted(DATASET, key=lambda x:float(x[10]))   # Sort with key of current rent price

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

def outputSpecificLeaseYearData():
    """
    Output list of masts with lease of 25 years to console.
    
    Args:
        None

    Returns:
        None

    """
    extracted_data = extractSpecificLeaseYearData()
    
    # Print items to console
    for item in extracted_data:
        print(f'\n{item}')
        
    input('\nPress enter to return to menu...')
    clear()
    
def outputTotalRent():
    """
    Calculates and outputs total rent from each mast with a 25 year lease

    Args:
        None

    Returns:
        None
        
    """
    extracted_data = extractSpecificLeaseYearData()
    
    # Sum rent costs for each item
    sum = 0
    for item in extracted_data:
        sum += float(item[10])
    
    print(f'\nTotal rent for all masts with a lease of 25 years:\n{sum}') # Output to console
    
    input('\nPress enter to return to menu...')
    clear()
    
def outputTenantDict():
    """
    Output dictionary containing keys of tenant names and values of number of masts for each tenant.
    
    Args:
        None
        
    Returns:
        None

    """
    DATASET = importData()  # Get dataset list
    
    # Fill dictionary with number of masts owned by each tenant
    tenant_dict = {}
    for row in DATASET:
        if row[6] in tenant_dict:
            tenant_dict[row[6]] += 1
        else:
            tenant_dict[row[6]] = 1
    
    # Output dictionary to console in readable format
    print('\n')
    for key in tenant_dict:
        print(f'{key}: {tenant_dict[key]}')
            
    input('\nPress enter to return to menu...')
    clear()
    
# Run code if file run from command line
if __name__ == '__main__':
    clear()
    
    # User input selection menu
    while True:
        print("""
Bink Python Developer Test | @author: Josh Stow
(1) Get data from the 5 masts with cheapeast rent prices
(2) Get data from masts with leases of 25 years
(3) Get total rent price of all masts with leases of 25 years
\nSelect function from list...""")

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
        if sel == 2:
            clear()
            outputSpecificLeaseYearData()
        if sel == 3:
            clear()
            outputTotalRent()
        # Throw error if selected option doesnt exist
        else:
            clear()
            print('ERROR: Please select a valid function!')
            continue
        