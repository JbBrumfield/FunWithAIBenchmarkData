# File Name : image.py
# Student Name: Jacob Brumfield, Sharvari Patil, Rithu Aynampudi
# email:  brumfijb@mail.uc.edu, patilsg@mail.uc.edu, aynampru@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/26/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Create an image that displays our team name and create some sort of data visualization that highlights the data of a csv file.
# Brief Description of what this modules does: This module showcases the actual outputs of the team logo as well as the data visualizations.
# Citations: ChatGPT

# Anything else that's relevant:
 
from readingLevelPackage.readingLevel import Reading_Level

from utilitiesPackage.utilities import *

from utilitiesPackage.CSV_Utilities import *

from PDFPackage.PDFUtilities import *

from dataVisPackage.dataVisualization import visualize_answers, load_data_from_csv  # Importing the necessary functions for data visualization

import matplotlib.pyplot as plt
 
if __name__ == "__main__":
 
    # Load CSV data

    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])

    questions = CSV_Processor.read_data()

    print(len(questions), "questions read")
 
    # Create PDF with questions

    myPDF = PDFUtilities()

    myPDF.create_question_PDF("Management Test", "MMLU", questions)
 
    print("The first question:")

    print(questions[0])
 
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])

    # Perform readability analysis on the big string and print the results to the console.

    Reading_Level.compute_readability_indices("MMLU", text)
 
    # Use data visualization for anatomy_test.csv

    # Load the answers from anatomy_test.csv

    answers = load_data_from_csv("dataPackage/MMLU/data/anatomy_test.csv")
 
    # Visualize the answer distribution with a pie chart

    visualize_answers(answers)
 
    # Image Display logic (RATTATA logo)

    import matplotlib.image as mpimg

    # Assuming 'rattata_logo.png' is in the 'imagePackage' directory

    img = mpimg.imread('rattata.png')
 
    # Display the image (200x200)

    plt.figure(figsize=(4, 4))  # Aspect ratio maintained

    plt.imshow(img)

    plt.axis('off')  # Turn off axis

    plt.title("Team RATTATA")  # Optional: Set a title for your image

    plt.show()
 
    # 6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.

    # 6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.

    questions_written = write_questions_to_text_files("MMLU", questions)

    print(questions_written, "questions written to the file.")
 
    """

    # This code is commented out

    # Reading_Level.test01()
 
    text = "This is a sentence that we can use to test the reading level computations. "

    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)

    for key in reading_level_indices.keys():

        print(key, ":", reading_level_indices[key])

    # A test with text at a higher reading level

    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."

    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)

    for key in reading_level_indices.keys():

        print(key, ":", reading_level_indices[key])

    """

 