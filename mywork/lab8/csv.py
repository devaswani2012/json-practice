import json

json_file_path = '../../data/schacon.repos.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

limited_data = data[:5]

with open('chacon.csv', 'w') as csv_file:
    for item in limited_data:
        name = item.get('name', 'N/A')
        html_url = item.get('html_url', 'N/A')
        updated_at = item.get('updated_at', 'N/A')
        visibility = item.get('visibility', 'N/A')
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)

