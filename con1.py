import json

# Read JSON file
with open("output.json", "r") as file:
    json_data = json.load(file)

# Access values and assign to variables
for entry in json_data:
    userid = entry["userid"]
    password = entry["password"]
    id_number = entry["id"]

    # Use the assigned values in your code as needed
    # For example:
    print("User ID:", userid)
    print("Password:", password)
    print("ID:", id_number)

    # Assign values to variables within your GitHub code
    # For example:
    # github_variable_1 = userid
    # github_variable_2 = password
    # github_variable_3 = id_number
