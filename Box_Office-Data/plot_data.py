import numpy as np
import matplotlib.pyplot as plt
from SQL.sql_collect import *
from SQL.sql_upload import *
import datetime
from engine import table_list

def plot_single_data(tablename):
    conn=connect_to_database('DESKTOP-E0NOB13', 'MediaData', 'YoUser', '2004')
    arr=get_data_sql(conn, tablename)
    date=[]
    revenue=[]
    for i in arr:
        date.append(i[0].replace(' ', ''))
        money=float(i[2][1:].replace(',', ''))/1000000
        revenue.append(money)
    date_arr=np.array(date)
    revenue_arr=np.array(revenue)
    plt.plot(date_arr, revenue_arr, marker='o')

    for i, txt in enumerate(revenue_arr):
        y=round(float(txt), 2)
        plt.annotate(txt, (date[i], y), textcoords="offset points", xytext=(0,10), ha='left')
    plt.show()
    plt.xlabel('Date')
    plt.ylabel('Revenue im millions($)')
    plt.title(f'{tablename} BoxOffice Collection')

    date=str(datetime.date.today())
    file=f'C:\Coding Folders\Pyhton_Projects\Box_Office-Data\Image_Storage\{tablename+str(date)}.jpg'
    plt.savefig(file)

def plot_multiple_data(tabl_list):
    plt.figure(figsize=(19.20, 10.80))
    for i in tabl_list:
        
        conn=connect_to_database('DESKTOP-E0NOB13', 'MediaData', 'YoUser', '2004')
        arr=get_data_sql(conn, i)
        date=[]
        revenue=[]
        for i in arr:
            date.append(i[0].replace(' ', ''))
            money=float(i[2][1:].replace(',', ''))/1000000
            revenue.append(money)
        date_arr=np.array(date)
        revenue_arr=np.array(revenue)
        plt.plot(date_arr, revenue_arr, marker='o')

        for i, txt in enumerate(revenue_arr):
            y=round(float(txt), 2)
            plt.annotate(txt, (date[i], y), textcoords="offset points", xytext=(0,10), ha='left')
        plt.xlabel('Date')
        plt.ylabel('Revenue im millions($)')
        plt.title(f'BoxOffice Collection')
    plt.legend(tabl_list)
    date = str(datetime.date.today())
    name = ''.join(tabl_list)
    file = r'C:\Coding Folders\Pyhton_Projects\Box_Office-Data\Image_Storage\{name}{date}.jpeg'.format(name=name, date=date)
    plt.savefig(file)
    plt.show()
        

plot_multiple_data(table_list)