"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class PhotoQuizApp(tk.Tk):
    # TODO 2) Create a constructor
    def __init__(self):
        # TODO 3) call Tk's constructor
        super().__init__()
        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.
        self.label = tk.Label()
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# TODO 5) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 6) Create an object of the tkinter class
    quiz = PhotoQuizApp()
    # TODO 7) Set the app window width and height using geometry()
    quiz.geometry("500x500")
    # TODO 8) Declare and initialize a score variable
    score = 0
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable
    image1 = create_image("carrots.jpg", 200, 200)
    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)
    quiz.label.configure(image=image1)
    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.
    response1 = simpledialog.askstring(title="Question 1", prompt="What are these?")
    # TODO 12) If the answer is correct, increase the score by 1
    if response1 == "Carrots":
        score = score + 1
        messagebox.showinfo(title="Correct", message="You got +1 point")
    else:
        messagebox.showinfo(title="Incorrect", message="Sorry, that's wrong")
    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question
    image2 = create_image("fossil.jpg", 200, 200)
    quiz.label.configure(image=image2)
    response2 = simpledialog.askstring(title="Question 2", prompt="What is this?")
    if response2 == "A fossil":
        score = score + 1
        messagebox.showinfo(title="Correct", message="You got +1 point")
    else:
        messagebox.showinfo(title="Incorrect", message="Sorry, that's wrong")

    image3 = create_image("python.png", 200, 200)
    quiz.label.configure(image=image3)
    response3 = simpledialog.askstring(title="Question 3", prompt="What colors is this made of?")
    if response3 == "Blue and yellow":
        score = score + 1
        messagebox.showinfo(title="Correct", message="You got +1 point")
    else:
        messagebox.showinfo(title="Incorrect", message="Sorry, that's wrong")

    # TODO 14) Display the score to the user after asking the last question
    messagebox.showinfo(title="Final score", message="Score = " + str(score))