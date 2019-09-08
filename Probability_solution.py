
import os
import pandas as pd
from Average import Questionone


# load = Questionone()
# load.load_data()
class Questiontwo:

    def __init__(self):
        """Initializer"""

    def find_probability(self):
        """Find the probability"""
        data = os.path.abspath('./dataset/train_revised.csv')
        # instantiate QuestionOne class
        question_one = Questionone()
        #Use questionne's method to check of the dataset has missing values
        #If not continue with execution
        if not question_one.check_for_missing_values(data):
            #Load the data using question one load_data method
            dataset = question_one.load_data(data)

            dataset = self.filter_according_to_travel_route(dataset, route="Kijauri")

            dataset = self.filter_according_to_time(dataset, time='7:30')
            #To find the probability divide the shuttle instance by len of dataset
            probability = dataset.groupby('car_type').size().div(len(dataset))
            return probability

    def filter_according_to_travel_route(self, dataset, route):
        """Filter the data according to the route passed"""
        """Drop all the rows where the travel_from column is not the specified route:Kijauri"""
        dataset.drop(dataset[dataset['travel_from'] != route].index,
             axis=0, inplace=True)
        return dataset


    def filter_according_to_time(self, dataset, time):
        """"Filter the data according to the time passed"""
        """Drop all rows where the travel_time column is not before the specified time:7:30"""
        dataset['time'] = pd.to_datetime(dataset['travel_time'])
        dataset.drop(dataset[(dataset['time'] >= time)].index, axis=0, inplace=True)
        return dataset


if __name__ == '__main__':
    run = Questiontwo()
    prob=run.find_probability()
    print('The probability is:',prob)
