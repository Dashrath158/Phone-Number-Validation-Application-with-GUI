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

## Contributions and Feedback

Feel free to contribute to this project by submitting pull requests or providing feedback. Your input is valuable and can help improve the app.

If you encounter any issues or have questions, please create an issue in the GitHub repository.

Happy coding!

