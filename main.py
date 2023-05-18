"""
Zhaohua Zhang APCSP 132
AI App Project
This app incorperates GPT-3 running the Davinci 002 engine. When the
user runs the code, a gui will pop up, prompting for the sure to enter
two birthdates and a button to check the compatibility based off their 
star signs. The GPT-3 engine will generate a paragraph explaining their 
star signs and give a verdict on whether they are compatable or not.

"""


import tkinter as tk
import openai
import time

openai.api_key = "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"

# Rate limiting variables
MAX_REQUESTS_PER_MINUTE = 60
REQUESTS_INTERVAL = 60 / MAX_REQUESTS_PER_MINUTE
last_request_time = 0

def generate_text(prompt):
    global last_request_time

    # Check time since last request and sleep if needed to stay within rate limits
    current_time = time.time()
    time_since_last_request = current_time - last_request_time
    if time_since_last_request < REQUESTS_INTERVAL:
        time.sleep(REQUESTS_INTERVAL - time_since_last_request)

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Update last request time
    last_request_time = time.time()

    message = completions.choices[0].text
    return message.strip()

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=5000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def get_star_sign(day, month):
    # Function to determine the star sign based on the given day and month
    # (Same as before)
    pass

def check_compatibility():
    dob1 = entry_dob1.get().strip()
    month1, day1, year1 = map(int, dob1.split("-"))
    star_sign1 = get_star_sign(day1, month1)

    dob2 = entry_dob2.get().strip()
    month2, day2, year2 = map(int, dob2.split("-"))
    star_sign2 = get_star_sign(day2, month2)

    prompt = f"What is the compatibility of {star_sign1} and {star_sign2}?"
    compatibility = generate_text(prompt)

    result_text.configure(text=f"Compatibility: {compatibility}")

# Create the main window
window = tk.Tk()
window.title("Star Sign Compatibility Checker")

# Create and position the labels
label_dob1 = tk.Label(window, text="Person 1 Date of Birth (mm-dd-yyyy):")
label_dob1.grid(row=0, column=0, padx=10, pady=10)

label_dob2 = tk.Label(window, text="Person 2 Date of Birth (mm-dd-yyyy):")
label_dob2.grid(row=1, column=0, padx=10, pady=10)

# Create and position the entry fields
entry_dob1 = tk.Entry(window)
entry_dob1.grid(row=0, column=1, padx=10, pady=10)

entry_dob2 = tk.Entry(window)
entry_dob2.grid(row=1, column=1, padx=10, pady=10)

# Create and position the button
btn_check = tk.Button(window, text="Check Compatibility", command=check_compatibility)
btn_check.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and position the result label
result_text = tk.Label(window, text="Compatibility: ")
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
window.mainloop()
