# File Name : image.py
# Student Name: Jacob Brumfield, Sharvari Patil, Rithu Aynampudi
# email:  brumfijb@mail.uc.edu, patilsg@mail.uc.edu, aynampru@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/26/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Create an image that displays our team name and create some sort of data visualization that highlights the data of a csv file.
# Brief Description of what this modules does: This modules showcases our team name in a logo that is 200x200 pixels. Our team name is Rattata as seen in the image.
# Citations: ChatGPT

# Anything else that's relevant:

from PIL import Image
import matplotlib.pyplot as plt 
import os
 
# Function to display an image for the team "RATTATA"
def display_team_image():
    '''
    Displays an image of our teams name
    @param image path works
    returns an image of our team name which is rattata
    '''
    # Load the image file (Ensure this image exists in your project directory)
    image_path = 'imagePackage/rattata.png'  # Replace this with your actual image path
    # Open the image using PIL
    image = Image.open(image_path)
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')  # Turn off axis labels
    plt.show()
 
# Call the function to display the team image
display_team_image()

# imageDisplay.py

# Module to display the team logo

 
def display_team_image(image_path):
    '''
    Displays an image of our teams name
    @param image path works
    returns an image of our team name which is rattata
    '''
    try:

        # Check if the image exists at the path

        if not os.path.exists(image_path):

            print(f"Error: The image at {image_path} does not exist.")

            return
 
        # Open the image using PIL

        image = Image.open(image_path)

        # Resize the image to 200x200 pixels, while maintaining the aspect ratio

        image = image.resize((200, 200))  # Resizing to 200x200 pixels

        # Display the image using matplotlib to show it directly on the screen

        plt.imshow(image)

        plt.axis('off')  # Hide the axis for a cleaner look

        plt.show()  # This will open the image in an interactive window

    except Exception as e:

        print(f"Error occurred: {e}")

 