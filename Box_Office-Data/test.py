import requests
from bs4 import BeautifulSoup

# URL of the page containing the table
url = 'https://www.boxofficemojo.com/release/rl1077904129/?ref_=bo_hm_rd'

# Make the HTTP request
response = requests.get(url)
html = response.text

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table')

# Initialize lists to store data
data = []

# Loop through each row in the table
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    if len(cells) >= 11:  # Ensure there are enough cells in the row
        date = cells[0].text.strip()
        day = cells[1].text.strip()
        rank = cells[2].text.strip()
        revenue = cells[3].text.strip()
        # ... (extract other columns as needed)

        # Store the data in a dictionary
        entry = {
            'Date': date,
            'Day': day,
            'Rank': rank,
            'Revenue': revenue,
            # ... (add other columns as needed)
        }

        # Append the entry to the data list
        data.append(entry)

# Print the extracted data
for entry in data:
    print(entry)
