# File Name : dataVisualization.py
# Student Name: Jacob Brumfield, Sharvari Patil, Rithu Aynampudi
# email:  brumfijb@mail.uc.edu, patilsg@mail.uc.edu, aynampru@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/26/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Create an image that displays our team name and create some sort of data visualization that highlights the data of a csv file.

# Brief Description of what this module does: This module takes data from anatomy_test.csv and create a pie chart of the percentages of how often a test question has the answer A, B, C, or D.

# Citations: ChatGPT

# Anything else that's relevant:

 
import matplotlib.pyplot as plt
import csv
 
# Function to load the CSV data
def load_data_from_csv(csv_file):
    '''
    Loads data from a CSV file(anatomy_test.csv)
    @param Path can be read
    returns a list of dictionaries
    '''
    answers = []  # List to store the answers
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if there is one
        for row in reader:
            if row:  # Skip any empty rows
                answers.append(row[-1])  # Assume the answer is in the last column
    return answers
 
# Function to visualize the answers in a pie chart
def visualize_answers(answers):
    '''
    Visualize the distribution of answers using a pie chart
    @param correct csv file pathing
    @param there are answer to grab from
    returns generates pie chart with percentages of answers
    '''
    # Count the frequency of each answer choice (A, B, C, D)
    answer_counts = {answer: answers.count(answer) for answer in set(answers)}
 
    # Plotting the pie chart
    labels = answer_counts.keys()
    sizes = answer_counts.values()
    plt.figure(figsize=(6, 6))  # Set size of the chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff6666'])
    plt.title('Answer Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
    plt.show()

 

 