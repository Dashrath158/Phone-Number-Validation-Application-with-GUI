# Required libraries
import requests
from tkinter import *
import re


# Program Logic
def validate_phone_number(api_key, phone_number):
    base_url = "http://apilayer.net/api/validate"
    params = {
        "access_key": api_key,
        "number": phone_number,
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": "An error occurred while making the request"}
    except ValueError as e:
        return {"error": "An error occurred while parsing the response"}


# GUI Logic using Tkinter
def on_click():
    api_key = "6e25222ebb815d198a348fe7abe7da13"
    phone_number = phone_entry.get()  # Get the phone number from the Entry widget
    if validate_input(phone_number):
        result_data = validate_phone_number(api_key, phone_number)
        formatted_result = format_result(result_data)
        result_label.config(text=formatted_result)
        # Write the phone number and result to a file
        with open('history.txt', 'a') as file:
            file.write(f"Phone Number: {phone_number}\n")
            file.write(formatted_result)
            file.write("\n" * 3)
    else:
        result_label.config(text="\nInvalid Input Format. Use only numbers and '+' symbol.")


# Validate input
def validate_input(phone):
    pattern = r'^\+?\d+$'
    return re.match(pattern, phone)


# Format dictionary data into a readable string
def format_result(data):
    formatted_result = ""
    for key, value in data.items():
        formatted_result += f"{key}: {value}\n"
    return formatted_result


# Validate the input to match the predefined format
def validate_phone_number_input(P):
    if re.match(r'^\+\d{0,15}$', P) is not None:
        return True
    return False


# GUI logic
root = Tk()
root.geometry("960x720")
root.minsize(640, 480)
root.maxsize(1920, 1080)
root.title("PhoneNumberValidation")

input_frame = Frame(root, relief=SOLID, bg="grey", borderwidth=5,padx=30,pady=40)
input_frame.pack(side=TOP,fill="both")

phone_label = Label(input_frame, text="Enter phone number:", font="Comicsans 30 bold",padx=30,pady=40)
phone_label.pack(fill="both")

phone_entry_frame = Frame(input_frame, bg="grey", padx=10, pady=10)
phone_entry_frame.pack(fill="y")

vcmd = (phone_entry_frame.register(validate_phone_number_input), '%P')

phone_entry = Entry(phone_entry_frame, font="Comicsans 25", width=40, borderwidth=5, relief=SOLID , validate="key", validatecommand = vcmd)
phone_entry.pack(fill="y")

validate_button = Button(input_frame, text="Validate", bg="yellow", font="Comicsans 20 bold", relief=SOLID, borderwidth=4,command=on_click, padx=30, pady=15)
validate_button.pack(fill="y")

result_label = Label(root, text="", font="Comicsans 12 bold",padx=30,pady=100)
result_label.pack(fill="both")

root.mainloop()