import os
from Average import Questionone
class Questionthree:
    def __init__(self):
        """Initialize"""

    def next_letter(self):
        """FInd the next letter"""
        data = os.path.abspath('./dataset/train_revised.csv')
        # instantiate QuestionOne class
        question_one = Questionone()
        # Use questionne's method to check of the dataset has missing values
        # If not continue with execution
        if not question_one.check_for_missing_values(data):
            # Load the data using question one load_data method
            dataset = question_one.load_data(data)
            #Get all characters occuring after MK and store them in a List
            next_letters = self.get_letters_after_MK(dataset)
            #Get the letter that is most recurring and the number it has recured
            letter,number = self.most_repeated_letter(next_letters)
            return letter,number

    def get_letters_after_MK(self,dataset):
        """Get all letters after MK"""
        probable_letter = []
        for letters in dataset['payment_receipt']:
            # check if the letters have MK in them
            if 'MK' in letters:
                # Get the next letter after K
                if letters.index('MK')+2 < len(letters):
                    probable_letter.append(letters[letters.index('MK')+2])

        return probable_letter

    def most_repeated_letter(self,data):
        """Find the most repeated letter"""
        frequency = 0
        repeated_letter = ''
        for j in data:
            count = data.count(j)
            if count>frequency:
                frequency = count
                repeated_letter = j
        return repeated_letter, frequency

if __name__ == '__main__':
    sequence = Questionthree()
    next_letter = sequence.next_letter()
    print("Most probable next letter is {} because it's count is {} ".format(next_letter[0],next_letter[1]))