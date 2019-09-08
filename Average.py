import os
import pandas as pd


class Questionone:
    def __init__(self):
        """Initializer"""
        self.df =''

    def load_data(self,data):
        """Read the dataset provided"""
        """Exception handling incase the path does not exist"""
        try:
            self.df = pd.read_csv(data)
            return self.df
        except IOError:
            return IOError

    def check_for_missing_values(self,path):
        """Clean the dataset"""

        df = self.load_data(path)
        return df.isnull().values.any()

    def understand_the_data(self,dataset):
        """Have a look at the dataset"""
        shape = dataset.shape
        description = dataset.describe
        print(shape)
        print(description)

    def filter_according_to_travel_day(self,day):
        """Filter the dataset and return data for the specified day"""
        """First check it the data has any mising values"""
        dataset = os.path.abspath('./dataset/train_revised.csv')
        if not self.check_for_missing_values(dataset):
            #Understand the dataset
            # self.understand_the_data(self.df)
            # Transform the travel date column to date time values to be accessedby dt
            self.df['travel_date'] = pd.to_datetime(self.df['travel_date'])
            # Get the respective day of the week and store it in a new column
            self.df['day_of_week'] = self.df['travel_date'].dt.day_name()
            # Drop all rows where the day was not the day passed:Sunday
            self.df.drop(self.df[self.df['day_of_week'] != day].index, axis=0, inplace=True)
            return self.df



    def find_top_seven_routes(self):
        """Filter the dataset and return data for the top seven routes"""
        df = self.filter_according_to_travel_day('Sunday')
        # Group the dataset according to the frequency of the travel route
        df =df.groupby(["travel_from", "travel_to"]).size().reset_index(name="Frequency")
        #Sort the dataset according to the frequency in descending order
        df =df.sort_values("Frequency", ascending=False)[:7]
        return df

    def find_average(self):
        """Calculate the average of top 7 routes"""
        df = self.find_top_seven_routes()
        # Find the total of the frequency of the top 7 traveled routes
        total =df.sort_values('Frequency', ascending=False).Frequency[:7].sum()
        # Calculate the average by dividing each frequency by the total
        df['average'] = df['Frequency'] / total

        return df


if __name__ == '__main__':
    question_one = Questionone()
    average = question_one.find_average()
    print(average.describe)

