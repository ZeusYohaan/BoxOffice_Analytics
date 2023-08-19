import subprocess
import multiprocessing
import time

def process_mv(url, tableName):
    file_path = r'C:\Coding Folders\Pyhton_Projects\Box_Office-Data\data_collect.py'
    subprocess.Popen(['python', file_path, url, tableName])

def plot_mv(table_list):
    file_path= r'C:\Coding Folders\Pyhton_Projects\Box_Office-Data\plot_data.py'
    subprocess.Popen(['python', file_path])
table_list= ['Oppenheimer', 'Barbie']
if __name__ == '__main__':
    urls_and_tableNames = [
        ('https://www.boxofficemojo.com/release/rl3725886209/?ref_=bo_hm_rd', 'Oppenheimer'),
        ('https://www.boxofficemojo.com/release/rl1077904129/?ref_=bo_hm_rd', 'Barbie')
    ]
    
    processes = []
    for url, tableName in urls_and_tableNames:
        proc = multiprocessing.Process(target=process_mv, args=(url, tableName))
        processes.append(proc)
        proc.start()
    time.sleep(5)
    
    proc2= multiprocessing.Process(target=plot_mv, args=(table_list,))
    proc2.start()
    processes.append(proc2)
    for proc in processes:
        proc.join()

    print('Data collection and upload completed.')
