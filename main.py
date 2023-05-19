"""
Group Members: Zhaohua Zhang, Danisha Panigrahi, Ishita Chaurasia
Period 1 Millard

AI App - Tutoring App Using AI
The code uses python that creates a gui using tkinter for an AI tutoring app. 
The app allows users to select a grade level and enter a subject. 
It then uses the GPT-3 API to generate problems based on the selected grade and subject. 
The generated problems are displayed in the app's interface from the chatbot.

"""

import tkinter as tk
import openai

# OpenAI GPT-3 API credentials
OPENAI_API_KEY = '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'

# Initialize the OpenAI API
openai.api_key = OPENAI_API_KEY

# Dictionary of grade levels and subjects
grades = {
    'Kindergarten': ['Math', 'English'],
    '1st Grade': ['Math', 'English', 'Science'],
    '2nd Grade': ['Math', 'English', 'Science'],
    '3rd Grade': ['Math', 'English', 'Science'],
    '4th Grade': ['Math', 'English', 'Science'],
    '5th Grade': ['Math', 'English', 'Science'],
    '6th Grade': ['Math', 'English', 'Science'],
    '7th Grade': ['Math', 'English', 'Science'],
    '8th Grade': ['Math', 'English', 'Science'],
    '9th Grade': ['Math', 'English', 'Science'],
    '10th Grade': ['Math', 'English', 'Science'],
    '11th Grade': ['Math', 'English', 'Science'],
    '12th Grade': ['Math', 'English', 'Science']
}

# Create the Tkinter GUI application
class TutorApp:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)

        # Grade Level Label
        self.grade_label = tk.Label(self.root, text='Select Grade Level:')
        self.grade_label.pack()

        # Grade Level Dropdown
        self.grade_var = tk.StringVar()
        self.grade_dropdown = tk.OptionMenu(self.root, self.grade_var, *grades.keys())
        self.grade_dropdown.pack()

        # Subject Label
        self.subject_label = tk.Label(self.root, text='Enter Subject:')
        self.subject_label.pack()

        # Subject Entry Field
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack()

        # Get Problem Button
        self.problem_button = tk.Button(self.root, text='Get Problem', command=self.get_problem)
        self.problem_button.pack()

        # Feedback Label
        self.feedback_label = tk.Label(self.root, text='Feedback:')
        self.feedback_label.pack()

        # Feedback Text Display
        self.feedback_text = tk.Text(self.root, height=10, width=50)
        self.feedback_text.pack()

    def get_problem(self):
        # Get selected grade level and subject
        grade_level = self.grade_var.get()
        subject = self.subject_entry.get()

        if grade_level and subject:
            # Construct prompt using grade level and subject
            prompt = f"Grade Level: {grade_level}\nSubject: {subject}\n"

            # Generate problem using the OpenAI GPT-3 API
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7
            )
            problem = response.choices[0].text.strip()

            # Display the generated problem in the feedback section
            self.feedback_text.delete(1.0, tk.END)
            self.feedback_text.insert(tk.END, problem)
        else:
            # Display error message if grade level or subject is missing
            self.feedback_text.delete(1.0, tk.END)
            self.feedback_text.insert(tk.END, 'Please select grade level and enter a subject.')

# Create the root window
root = tk.Tk()

# Set the title of the GUI
title = "AI Tutoring App"

# Set the window size
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Create an instance of the TutorApp
tutor_app = TutorApp(root, title)

# Start the Tkinter event loop
root.mainloop()
