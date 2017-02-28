# -*- coding: utf-8 -*-

#Created by Aditya Daryanani on 2/24/17 

import numpy as np

class Utility:
               
    def GetScanArraySize(self):
        n = raw_input("Enter the size N of the scan array\n")  
        if(n.isdigit() == 0 or int(n)<0 or int(n)>1000):
            print("The size of the scan array needs to be a positive integer between 1 and 1000\n")
            return -1
        else:    
            return int(n)      
        
    def GetUserOption(self):
        o = raw_input("Enter 1 to use the scan examples from the problem or 2 to generate random examples \n") 
        if(o.isdigit() == 1 and (int(o)==1 or int(o)==2)):
            return int(o)
        else:
            print("The options can be either 1 and 2. Please run again\n")
            return -1
    def GetScanReadingCount(self):
        t = raw_input("How many scan readings do you want to generate?\n")  
        if(t.isdigit() == 0 or int(t)<0 or int(t)>50):
            print("The size of the scan array needs to be a positive integer between 1 and 50\n")
            return -1
        else:
            return int(t)
    
    def GetMedianFilterReadingCount(self, t):
        d = raw_input("How many historical scan readings do you want to be included in the temporal median filter average?\n")  
        if(d.isdigit() == 0 or int(d)<0 or int(d)>50 or int(d)>t):
            print("The temporal median filter window size needs to be a positive integer less than the number of samples t\n")
            return -1
        else:    
            return int(d)

    def GenerateRandomScanVector(self, n):
        scanArray = np.random.uniform(low=0.00, high=55.00, size=(1,n))
        return scanArray
                
class Filters:
   
   def RangeFilter(self, scanArray):
       scanArray[scanArray > 50.00] = 50.00
       scanArray[scanArray < 0.03] = 0.03
       return scanArray
       
   def TemporalMedianFilter(self, histArray):
       meanArray = np.median(histArray, axis=0)
       return meanArray

def main():
    u = Utility()
    o = u.GetUserOption() 
    if(o==-1):
        return
    f = Filters()
    if(o==1):
        n=5
        t=5
        d=3
        histArray = np.array([[0, 1, 2, 1, 3],[1, 5, 7, 1, 3],[2, 3, 4, 1, 0],[3, 3, 3, 1, 3],[10,2, 4, 0, 0]])
    if(o==2):
        n = u.GetScanArraySize()
        if(n==-1):
            return
        t = u.GetScanReadingCount()
        if(t==-1):
            return
        d = u.GetMedianFilterReadingCount(t)
        if(d==-1):
            return
        histArray = np.zeros((t,n), dtype=float)
    
    for i in range(0,t):
          if (o==2):
              scanArray = u.GenerateRandomScanVector(n)
              print("Generated scan reading is ")
              print(scanArray)
              print("\n")
              filteredArray = f.RangeFilter(scanArray)
              print("Range filtered scan reading is ") 
              print(filteredArray)
              print("\n")
              histArray[i][:] = filteredArray
          if(i>d):
              medianArray = f.TemporalMedianFilter(histArray[:][i-d-1:i])
          if(i<=d):    
              medianArray = f.TemporalMedianFilter(histArray[:][:i])
          print("The median scan reading is ") 
          print(medianArray)
          print("\n")
    if(t>d):
        medianArray = f.TemporalMedianFilter(histArray[:][t-d-1:t])
    if(t<=d):    
        medianArray = f.TemporalMedianFilter(histArray[:][:t])
    print("The final median scan reading is ") 
    print(medianArray)
    print("\n")    
if __name__ == "__main__": main()
