import numpy as np
import requests
from bs4 import BeautifulSoup
from SQL.sql_upload import *
from engine import *
import sys

url=sys.argv[1]
tableName=sys.argv[2]

server = 'DESKTOP-E0NOB13'
database = 'MediaData'
username = 'YoUser'
password = '2004'

conn = connect_to_database(server, database, username, password)
curr = conn.cursor()

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the HTTP request fails
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table')

    ls = []

    for row in table.find_all('tr')[1:]:  # Skip the header row
        dict = {}
        cells = row.find_all('td')
        date = cells[0].text.strip()
        day = cells[1].text.strip()
        rank = cells[2].text.strip()
        revenue = cells[3].text.strip()
        dict['Date'] = date
        dict['Day'] = day
        dict['Revenue'] = revenue
        dict['Rank'] = rank
        ls.append(dict)

    ls_arr = np.array(ls)

    sql_query = f'DELETE FROM {tableName}'
    curr.execute(sql_query)
    conn.commit()

    for i in ls_arr:
        upload_data_db(conn, tableName, i)

except requests.RequestException as e:
    print("Error during HTTP request:", e)

except Exception as e:
    print("An error occurred:", e)

finally:
    conn.close()
print('Data Uploaded for '+ tableName)