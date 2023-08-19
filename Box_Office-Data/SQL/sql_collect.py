import numpy as np
import pyodbc


def get_data_sql(conn, tableName):
    curr=conn.cursor()
    sql_query=f'SELECT * FROM {tableName}'
    curr.execute(sql_query)
    ls=curr.fetchall()
    conn.commit()
    return np.array(ls)