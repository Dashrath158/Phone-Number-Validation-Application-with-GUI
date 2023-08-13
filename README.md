# Phone-Number-Validation-Application-with-GUI

Welcome to the Phone Number Validation App! This app allows you to validate phone numbers using the numverify.com API. You can also configure the app to work with other APIs with some adjustments.

## Getting Started

Follow these steps to access the code and set up the app:

1. **Sign Up for API Access:**
   - Visit the numverify website (or another API provider) to sign up and obtain an API access key.
   - Keep the API access key handy, as you'll need it to configure the app.

2. **Clone the Repository:**
   - Clone this repository to your local machine using the following command:
     ```
     git clone https://github.com/your-username/phone-number-validation.git
     ```

3. **Install Dependencies:**
   - Make sure you have Python installed on your machine.
   - Install the required dependencies using the following command:
     ```
     pip install tkinter requests
     ```

4. **Configure the API Key:**
   - Open the `main.py` file in your code editor.
   - Look for the `api_key` variable and replace the placeholder with your actual API access key.
   - Save the file.

5. **Run the App:**
   - Open a terminal and navigate to the repository directory.
   - Run the app using the following command:
     ```
     python main.py
     ```

6. **Use the App:**
   - The app will launch and display a GUI interface.
   - Enter a phone number in the desired format (e.g., +1234567890) and click the "Validate" button.
   - The app will provide information about the phone number's validity and other details.

7. **Customize for Other APIs:**
   - If you want to use a different API, you can modify the API endpoint and parameters in the `validate_phone_number` function in the `main.py` file.
   - Adjust the code to match the requirements of the chosen API.
## Basic Functions of the App

The Phone Number Validation App is designed to validate and provide details about phone numbers. The app utilizes the numverify.com API to perform these functions. Below, we'll walk through the basic functions of the app along with an overview of the code snippets provided.

### Phone Number Validation

The main feature of the app is to validate a given phone number and provide related details. The validation process checks if the phone number is in a valid format and then uses the numverify.com API to retrieve information about the number.

### User Interface

The app features a graphical user interface (GUI) created using the `tkinter` library. Users can input a phone number in the designated Entry widget and click the "Validate" button to initiate the validation process. The result of the validation is displayed in the designated result label.

### Core Code Logic

The core logic of the app revolves around the `validate_phone_number` function. This function takes an API key and a phone number as inputs and communicates with the numverify.com API to retrieve validation details.

The `validate_input` function ensures that the entered phone number follows a predefined format before initiating validation.

### Writing to File

The app also includes functionality to write the validated phone number and result to a file named `history.txt`. This allows users to keep a record of their validation attempts.

### User Input Validation

To enhance the user experience, the app validates user input as it's being entered. The `validate_phone_number_input` function uses regular expressions to ensure that only valid characters (numbers and '+') are entered.

## Contributions and Feedback

Feel free to contribute to this project by submitting pull requests or providing feedback. Your input is valuable and can help improve the app.

If you encounter any issues or have questions, please create an issue in the GitHub repository.

Happy coding!

