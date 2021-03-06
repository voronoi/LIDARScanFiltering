# LIDARScanFiltering

//C
This application was developed and tested on the Python 2.7.13 interpreter, library dependencies are Numpy 1.12
c 2017 by Aditya Daryanani

----------------------------------------------------------------------------------------------------------------------------
User Guide
----------------------------------------------------------------------------------------------------------------------------
1.) Application on initialization asks for two options
	Enter 1 to use the scan examples from the problem or 2 to generate random examples
	Option 1 will use the example from the problem pdf table
	Option 2 will generate random scans based on the sizes of the scan arrays that you would choose


2.) Enter the size N of the scan array --> This is the size of the scan vector, in the example in the exercise this is 5.
	if you have pressed option 2 to generate random scans this option will be accessible to you

3.) Enter the number of scan readings - This is the total number T of scan readings that will be generated one after the other	

4.) Enter the (D) - the historical size(how many samples in the past considered for temporal median) of the median filters that you want to take into consideration. This needs to be less than the total number of samples T.




A few random scans of size N wit T number of samples, where D is the window size or historical examples considered for the temporal median filter are generated
This is the output example from this mode: (the first initialization temporal median filter scan will be null or NaN and this is expected) - All the subsequent median readings as shown below are correct as seen in the table in the problem
The median scan reading is 
[ 0.  1.  2.  1.  3.]


The median scan reading is 
[ 0.5  3.   4.5  1.   3. ]


The median scan reading is 
[ 1.  3.  4.  1.  3.]


The median scan reading is 
[ 1.5  3.   3.5  1.   3. ]


The final median scan reading is 
[ 2.5  3.   4.   1.   1.5]


______________________________________________________________________________________________________________________________
Developer Guide
______________________________________________________________________________________________________________________________
The method RangeFilter() in the class Filters is responsible for filtering the LIDAR scan values inside each scan vector between 0.03 and 50 as in the problem requirement

In the same class the method TemporalMedianFilter() is responsible for getting the median of the current + historical D scans

The utility class contains methods to get user inputs and other miscellaneous methods such as random sample readings generation
Random samples are generated between 0.0 to 55.00 thus allowing the RangeFilter() a chance to correct the range to 0.03 to 50 as required by the problem
