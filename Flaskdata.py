import requests
import json

# Define the data to send
data = {
    'team_name': '7657',
    'mobility': 1,
    'balance': 1,
    'amount_of_auto': 1,
    'cone_top': 1,
    'cone_middle': 1,
    'cone_bottom': 1,
    'cube_top': 1,
    'cube_middle': 1,
    'cube_bottom': 1
}

# Convert the data to JSON
json_data = json.dumps(data)

# Define the URL of the Flask app
url = 'http://10.60.4.27:5000/insert_data'

# Send the data using an HTTP POST request
response = requests.post(url, json=json_data)

# Print the response
print(response.text)