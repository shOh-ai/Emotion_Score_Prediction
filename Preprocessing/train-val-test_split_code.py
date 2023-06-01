#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split

# 데이터 로드
data = pd.read_excel('/Users/sh_oh/Downloads/dataset.xlsx')

# 성별과 실험 순서에 따라 데이터를 나눔
# stratify 파라미터를 사용하여 성별과 실험 순서를 기준으로 분리
train_val, test = train_test_split(data, test_size=0.29, stratify=data[['Sex', 'order']], random_state=42)

# 결과 출력
print("Train and Validation Set:")
print(train_val)
print("\nTest Set:")
print(test)

# 실제로 분리된 데이터에서도 원하는 비율이 유지되었는지 확인하기 위한 코드 / 각 세트에서의 성별 및 실험 순서 비율을 출력
print("Train and Validation Set ratios:")
print(train_val['Sex'].value_counts(normalize=True))
print(train_val['order'].value_counts(normalize=True))

print("\nTest Set ratios:")
print(test['Sex'].value_counts(normalize=True))
print(test['order'].value_counts(normalize=True))

