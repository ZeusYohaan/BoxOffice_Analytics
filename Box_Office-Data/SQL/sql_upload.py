import pyodbc

def connect_to_database(server, database, username, password):
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connection_string)
    return conn

def upload_data_db(conn, tableName, single_entry):
    curr = conn.cursor()
    data = single_entry['Date']
    day = single_entry['Day']
    revenue = single_entry['Revenue']
    rank = single_entry['Rank']
    sql_query = f'INSERT INTO {tableName} (Date, Day, Revenue, Rank) VALUES (?, ?, ?, ?)'
    curr.execute(sql_query, (data, day, revenue, rank))
    conn.commit()

def upload_plot_db(conn, fileName, MV_name):
    curr = conn.cursor()
    plot_path = fileName  
    sql_query = 'INSERT INTO PlotTable (FileName, MVName) VALUES (?, ?)'
    curr.execute(sql_query, (plot_path, MV_name))
    conn.commit()
