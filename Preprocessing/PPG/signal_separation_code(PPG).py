#!/usr/bin/env python
# coding: utf-8

# ## 필요한 59명의 일련번호 리스트로 저장

# In[2]:


import os

folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/PPG'

subfolders = os.listdir(folder_path)
subfolder_list = sorted(subfolders)

print(subfolder_list)


# ## BVP 데이터 구간별로 자르기 총 19개 구간

# In[ ]:


import os
import csv
import math

# BVP.csv 파일 경로
bvp_directory = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/PPG'
bvp_files = os.listdir(bvp_directory)

# 숫자.csv 파일 경로
csv_directory = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/PPG'
csv_files = os.listdir(csv_directory)

# 저장할 디렉토리 경로
output_directory = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/Output_PPG'

# 폴더 이름 리스트
folder_names = ['001', '002', '003', '005', '006', '007', '009', '010', '011', '012', '013', '015',
                '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028',
                '029', '030', '031', '032', '033', '036', '038', '039', '041', '042', '043', '044',
                '045', '047', '048', '052', '053', '054', '055', '059', '060', '062', '063', '064',
                '065', '066', '068', '070', '072', '073', '074', '075', '076', '077', '078']

# 반복문을 사용하여 BVP.csv 파일을 각 구간에 맞게 분할하여 저장
for i in range(len(folder_names)):
    # BVP.csv 파일 경로
    bvp_csv_file = os.path.join(bvp_directory, folder_names[i], 'BVP.csv')

    # 숫자.csv 파일 경로
    csv_file = os.path.join(csv_directory, folder_names[i], f'{folder_names[i]}.csv')

    # 숫자.csv의 2열 2행부터 21행까지의 값 추출 및 정수 부분만 사용
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        column_2_values = list(csv_reader)[1:21]
        row_numbers = [math.floor(float(row[1]))+2 for row in column_2_values]

    # BVP.csv 파일을 각 구간에 맞게 분할하여 저장
    with open(bvp_csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

        for j in range(len(row_numbers) - 1):
            start_idx = row_numbers[j]
            end_idx = row_numbers[j + 1]
            if j == 0:
                end_idx += 1
            else:
                start_idx += 1
            segment_data = data[start_idx:end_idx]

            segment_csv_file = os.path.join(output_directory, folder_names[i], f'{j + 1}.csv')
            with open(segment_csv_file, 'w', newline='') as segment_file:
                writer = csv.writer(segment_file)
                writer.writerows(segment_data)

print('구간별 데이터 저장 완료')


# ## 3, 6, 9, 12, 15, 18번째 구간에 대한 데이터만 남기고 나머지 전부 삭제

# In[ ]:


import os

# Output 폴더 경로
output_directory = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/Output_PPG'

# Output 폴더 내의 모든 하위 폴더 열기
sub_folders = [sub_folder for sub_folder in os.listdir(output_directory) if os.path.isdir(os.path.join(output_directory, sub_folder))]

for sub_folder in sub_folders:
    sub_folder_path = os.path.join(output_directory, sub_folder)
    files = os.listdir(sub_folder_path)
    for file_name in files:
        if file_name.endswith('.csv') and file_name.split('.')[0] not in ['3', '6', '9', '12', '15', '18']:
            file_path = os.path.join(sub_folder_path, file_name)
            os.remove(file_path)

print('불필요한 파일 삭제 완료')

