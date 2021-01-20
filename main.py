# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:31:59 2021

@author: Josh Stow
"""

# Import dependencies
import csv
import os
from datetime import datetime as dt

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
    Prettify(cheapest_five)
        
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
    Prettify(extracted_data)
        
    input('\nPress enter to return to menu...')
    clear()
    
def outputTotalRent():
    """
    Calculates and outputs total rent from each mast with a 25 year lease.

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
    print('')
    for key in tenant_dict:
        print(f'{key}: {tenant_dict[key]}')
            
    input('\nPress enter to return to menu...')
    clear()
    
def outputDataBetweenDates():
    """
    Output data with lease start dates between 01/06/1999 and 31/08/2007 in DD/MM/YYYY format.

    Args:
        None
        
    Returns:
        None

    """
    DATASET = importData()  # Get dataset list
    
    # Declare constant date objects
    DATE1 = dt(1999, 6, 1)
    DATE2 = dt(2007, 8, 31)
    
    # Compare each masts start lease date
    extracted_data = []
    for row in DATASET:
        temp_dates = (dt.strptime(row[7], '%d %b %Y'),dt.strptime(row[8], '%d %b %Y')) # Store converted datetime objects in tuple (start date, end date)
        
        # Edit row with dates formatted by DD/MM/YYYY if start date is valid
        if temp_dates[0] > DATE1 and temp_dates[0] < DATE2:
            row[7] = dt.strftime(temp_dates[0], '%d/%m/%Y')
            row[8] = dt.strftime(temp_dates[1], '%d/%m/%Y')
            extracted_data.append(row)  # Append updated row to list
    
    # Output items to console
    Prettify(extracted_data)
            
    input('\nPress enter to return to menu...')
    clear()
    
def Prettify(list):
    """
    Outputs list of mast data to console in readable format.
    
    Args:
        list::[[str]]

    Returns:
        None

    """
    # Iterate over list
    for item in list:
        print(f'\nProperty Name: {item[0]}\nAddress:')
        # Loop over address elements as some are empty in specific cases
        for line in item[1:5]:
            if line != '':
                print(line)
        print(f"""Unit Name: {item[5]}
Tenant Name: {item[6]}
Lease Dates: {item[7]} --> {item[8]}
Lease Duration: {item[9]} yrs
Current Rent: £{item[10]}""")
            
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
(4) Get number of masts owned by each company
(5) Get data from masts with lease start date between 01/06/1999 and 31/08/2007
(6) Exit program
\nSelect function from list...""")

        # Get user input,
        sel = input('\n> ')
        
        # Only accept int values
        try:
            sel = int(sel)
        except:
            clear()
            print('ERROR: Please select a valid function!')
            continue
        
        # Determine selection
        if sel == 1:
            clear()
            getCheapest()
            continue
        if sel == 2:
            clear()
            outputSpecificLeaseYearData()
            continue
        if sel == 3:
            clear()
            outputTotalRent()
            continue
        if sel == 4:
            clear()
            outputTenantDict()
            continue
        if sel == 5:
            clear()
            outputDataBetweenDates()
            continue
        if sel == 6:
            clear()
            exit()
        # Throw error if selected option doesnt exist
        else:
            clear()
            print('ERROR: Please select a valid function!')
            continue
        