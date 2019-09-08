# Summary of the solution

## Tools

-Language: Python3
-Liblary: Pandas

## Approach

- I decided to use OOP because this way I can reuse methods already defined and implements for a given solution
- Example of this methods are reading data and checking for Empty value
- For working with data I decided to use pandas liblary because it provide simplicity while working with large dataset

## First Question

- First I had to load the data and factor in for Input/Output Error
- Next check to see if there are any missing values in the dataset
- Understand how the dataset is or have a look at it before sorting
- Since we only want data for Sunday then we hav to filter out the dataset and drop the rows that contains the data where the day is not Sunday
- In the already filtered dataset find the top seven most traveled routesand rank them accordingly in descending order.
- Finaly calculate the average of the top seven routes

## Second Question

- Make use of the methods defined in solution one to load the dataset and check if there are any empty values
- If everything is OK filter the dataset according to the route and drop all the rows where the column of travel_from is not Kijauri
- Next filter out the remaining dataset and drop all the rows where the travel_time was after 0730hrs
- The resultant dataset will only contain the values for travel duration that occured before 7:30
- Calculate the probability of the mean of travel being a shuttle because the dataset has both bus and shuttle

## Third Question

- Make use of methods in solution one for loading the dataset and checking if any of the fields are empty
- Get all transaction receipt that have letters MK in then in that order
- Get the index of letter M and add 2 more index to get the next letter after index of K
- store this letters in a separate list
- Loop through the list and hold the letter that appears the most times
- Due to the fact that it is appearing most times then it is the most probale letter in the tri-gram

## Fourth Question

- Make use of methods in solution one for loading the dataset and checking if any of the fields are empty
- Also to avoid repetion use the method in solution two to filter out the dataset according to the specified route
- Next get the no of rows where the payment method used is Mpesa:Assumption made that this is the mobile money means of payment
- Next get the count of all rows of the dataset
- To get the percentage divide the numbet of payments where the method of payment is Mpesa and the total number of rows and multiply the answer by 100
- If the percentage is over 50 percent then recomend YES for having mobile payment else recomend No.
