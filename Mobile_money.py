import os
from Average import Questionone
from Probability_solution import Questiontwo

class Questionfour:
    def __init__(self):
        """Initialize"""

    def mobile_money(self):
        data = os.path.abspath('./dataset/train_revised.csv')
        # instantiate QuestionOne class
        question_one = Questionone()
        # Use questionne's method to check of the dataset has missing values
        # If not continue with execution
        if not question_one.check_for_missing_values(data):
            # Load the data using question one load_data method
            dataset = question_one.load_data(data)
            question_two = Questiontwo()
            dataset =question_two.filter_according_to_travel_route(dataset,'Kisii')
            mpesa_use = self.mpesa_percentage(dataset)
            return mpesa_use
    def mpesa_percentage(self,dataset):
        """Get the percentage of people using Mpesa"""
        mpesa_payment = len(dataset[dataset['payment_method'] == 'Mpesa'])
        all_rows = dataset['payment_method'].count()
        mpesa_percentage = mpesa_payment / all_rows * 100
        return mpesa_percentage


if __name__ == '__main__':
    mobile_money = Questionfour()
    percent = mobile_money.mobile_money()
    if percent > 50:
        print("""Yes the terminus should have mobile money capabilities because {} percent
                of people use mobile money """.format(percent))
    else:
        print("""No the terminus should not have mobile
                money capabilities because only {} percent
                of people use mobile money""".format(percent))
