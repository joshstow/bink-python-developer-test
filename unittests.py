# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 01:03:10 2021

@author: Josh Stow
"""

# Import dependencies
import unittest
import main

# Create class inheriting from TestCase
class Test(unittest.TestCase):
    
    def test_sortList(self):
        """
        Check sortList function orders list correctly by lease price in ascending order.
        
        """
        # Expected return data
        sorted_data = [['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'],
                       ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'], 
                       ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'],
                       ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'], 
                       ['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Beecroft Hill - Telecom App', 'Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00']]
        
        main.importData = Test.sortList_importData  # Override importData function
        self.assertEqual(main.sortList(), sorted_data)
        
    def sortList_importData():
        """
        Overrides importData function and returns test input.
        
        Args:
            None
            
        Returns:
            ::[[str]]
            
        """
        return [['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Beecroft Hill - Telecom App', 'Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'], 
                ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'], 
                ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'], 
                ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'], 
                ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00']]

    def test_extractSpecificLeaseYearData(self):
        """
        Check extractSpecificLeaseYearData function returns masts with lease duration of 25 years.
        
        """
        # Expected return data
        extracted_data = [['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'], 
                          ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'], 
                          ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'], 
                          ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414', 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21 Aug 2007', '20 Aug 2032', '25', '12750.00']]
        
        main.importData = Test.extractSpecificLeaseYearData_importData   # Override importData function
        self.assertEqual(main.extractSpecificLeaseYearData(), extracted_data)
        
    def extractSpecificLeaseYearData_importData():
        """
        Overrides importData function and returns test input.
        
        Args:
            None
            
        Returns:
            ::[[str]]
            
        """
        return [['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Beecroft Hill - Telecom App', 'Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', '64', '23950.00'], 
                ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', '20', '6600.00'], 
                ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004', '29 Jan 2029', '25', '12250.00'], 
                ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', '25', '9500.00'], 
                ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd', '26 Jul 2007', '25 Jul 2032', '25', '12000.00'], 
                ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414', 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21 Aug 2007', '20 Aug 2032', '25', '12750.00'], 
                ['Cottingley Towers', 'Leeds', '', '', 'LS11', 'Cottingley Towers-WYK0052', 'Everything Everywhere Ltd', '28 Jan 2008', '27 Jan 2018', '10', '12750.00'], 
                ['Potternewton Heights - Tel App', 'Potternewton Heights', 'Potternewton Lne', 'Leeds', '', 'Potternewton Heights', 'Everything Everywhere Ltd', '04 Mar 2008', '03 Mar 2018', '10', '12750.00']]
        
# Run code if file run from command line
if __name__ == '__main__':
    unittest.main() # Run unit tests