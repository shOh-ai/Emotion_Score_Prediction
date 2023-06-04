#!/usr/bin/env python
# coding: utf-8

# ## train_subject_number

# In[2]:


import csv

numbers = ['053', '009', '066', '024', '023', '047', '036', '021', '078', '001', '027', '075', '076', '006', '073', '031', '063', '038', '015', '032', '064', '062', '054', '028', '026', '044', '041', '022', '033', '042', '012', '077', '070', '072', '005', '060', '010', '011', '013', '045', '055']

numbers.sort()

file_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/sub_id.csv'

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID'])
    for num in numbers:
        writer.writerow([num])


# ## train_video_order

# In[9]:


import pandas as pd

# scale.xlsx 파일 경로
xlsx_file = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/scale.xlsx'

# CESAF 시트 열기
sheet_name = 'CESAF'
df = pd.read_excel(xlsx_file, sheet_name=sheet_name, header=None)

# 1열의 값이 일치하는 행들 선택
target_values = ['001', '005', '006', '009', '010', '011', '012', '013', '015', '021', '022', '023', '024', '026',
                 '027', '028', '031', '032', '033', '036', '038', '041', '042', '044', '045', '047', '053', '054',
                 '055', '060', '062', '063', '064', '066', '070', '072', '073', '075', '076', '077', '078']
selected_rows = df[df.iloc[:, 0].isin(target_values)]

# 43열부터 48열의 값을 가져와서 video_id.csv에 저장
output_csv_file = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/video_id.csv'
selected_values = selected_rows.iloc[:, 42:48].values.flatten()

# CSV 파일로 저장
df_output = pd.DataFrame({'video_ID': selected_values})
df_output.to_csv(output_csv_file, index=False, header=True)

print('CSV 파일 저장 완료.')

