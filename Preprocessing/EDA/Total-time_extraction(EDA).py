#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv
import shutil

# 경로-1: E4 폴더
folder_path_1 = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/E4'

# 경로-2: Event_marker_eda 폴더
folder_path_2 = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/Event_marker_eda'

# 경로-3: Event_marker_eda_1 폴더
folder_path_3 = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/Event_marker_eda_1'

# E4 폴더 내 하위 폴더 목록 가져오기
sub_folders = [sub_folder for sub_folder in os.listdir(folder_path_1) if os.path.isdir(os.path.join(folder_path_1, sub_folder))]

for sub_folder in sub_folders:
    # EDA.csv 파일 경로
    csv_file_path_1 = os.path.join(folder_path_1, sub_folder, 'EDA.csv')
    
    # EDA.csv 파일의 행 개수 (마지막 행번호)
    with open(csv_file_path_1, 'r') as file:
        csv_reader = csv.reader(file)
        last_row_number = sum(1 for _ in csv_reader) - 1
    
    # 대상 CSV 파일 경로
    target_csv_file_path = os.path.join(folder_path_2, f'{sub_folder}.csv')
    
    # 대상 CSV 파일의 1열 23행에 (행번호 - 1) 저장
    with open(target_csv_file_path, 'r+') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        rows[22][0] = str(last_row_number - 1)
        file.seek(0)
        writer = csv.writer(file)
        writer.writerows(rows)
        file.truncate()

    # 대상 CSV 파일을 Event_marker_eda_1 폴더로 복사
    target_csv_file_path_1 = os.path.join(folder_path_3, f'{sub_folder}.csv')
    shutil.copyfile(target_csv_file_path, target_csv_file_path_1)

print('행번호 저장 완료')


# In[ ]:




