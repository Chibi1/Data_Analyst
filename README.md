# Data_Analyst
Short programs where I used pandas,JSON, CVS


Tast 1:
The task is to read data from the address
http://api.nbp.pl/api/exchangerates/tables/A?format=json and load it into a DataFrame object.
The index is the data from the "code" column.


Task 2:
At the address https://bit.ly/2K8JOur, we have data from advertisements on otomoto.pl (pay attention to the delimiter type). There is a column called "Wyposażenie" (Equipment) that contains items (separated by a vertical bar (pipe)) that are part of the car's equipment in the ad. Please convert it to the format, where each equipment item will be a separate column with True/False values 
(True = the equipment is available, False = the equipment is not available).


Task 3:
To load data from the file at https://bit.ly/2nNFoRe, where missing values are marked as "?" (question mark), and perform the specified tasks, you can use the pandas library:

-Find the most expensive car (without using the sort_values() or nlargest() methods).

-Find the number of rows for each brand (in the "company" column).

-Find the average price.

-Find the median price.

-Find the cars whose price is greater than the median

-The "length" column contains the length of the car in inches - please convert the values to metric units and provide them in centimeters.

-The "num-of-cylinders" column contains information about the number of cylinders written in words - please convert them to numeric values.



Task 4:
To load a CSV file from the given URL (https://www.dropbox.com/s/axeucvys209d30h/inc5000_all10years.csv?dl=1) into a DataFrame, you can use the pandas library:



1.Find data that meets the following conditions:

-The 'industry' column has the value 'Software'

-The company's state ('state_s') is California (CA)

-The year ('year') is 2017

-The company name ('company') starts with the letter 'S' or the letter 'C'



2.Sort the obtained data based on the following columns:

-Sort by 'yrs_on_list' in ascending order

-Sort by 'revenue' in descending order

-Sort by 'workers' in ascending order
