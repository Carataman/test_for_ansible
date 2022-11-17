import os
import datetime


fm_path = ('/mnt/targets/arch/trucks/')

def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            try:
                dir = os.path.join(root, item)
                os.rmdir(dir)
            except Exception as e:
                pass


del_emp_dir(fm_path)

file_list = os.listdir(fm_path)
full_list = [os.path.join(fm_path, i) for i in file_list]
time_sorted_year_list = sorted(full_list)
print(time_sorted_year_list)

for element in time_sorted_year_list:
    del_emp_dir(element)
    month_list = os.listdir(element)
    full_month_list = [os.path.join(element, i) for i in month_list]
    time_sorted_month_list = sorted(full_month_list)
print(time_sorted_month_list)

for element in time_sorted_month_list:
    del_emp_dir(element)
    day_list =  os.listdir(element)
    full_day_list = [os.path.join(element, i) for i in day_list]
    time_sorted_day_list = sorted(full_day_list)
print(time_sorted_day_list)








