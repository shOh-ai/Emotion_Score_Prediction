#!/usr/bin/env python
# coding: utf-8

# ## 1. 데이터 불러오기

# In[19]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/sub_id.csv')


# ## 2. 사람_ID를 범주형 변수로 변환

# In[20]:


label_encoder = LabelEncoder()
df['ID_encoded'] = label_encoder.fit_transform(df['sub_id'])


# ## 3. embedding layer 생성

# In[22]:


import tensorflow as tf
from tensorflow.keras.layers import Embedding
print(tf.__version__)

n_unique_ids = df['ID_encoded'].nunique()
embedding_dim = min(n_unique_ids // 2, 50)  # 임베딩 차원 설정. 보통은 고유 ID의 수의 절반 혹은 50을 선택

embedding_layer = Embedding(input_dim=n_unique_ids, 
                            output_dim=embedding_dim, 
                            input_length=1, 
                            name='ID_embedding')


# ## 4. 임베딩 레이어를 통과하여 벡터 생성 및 확인

# In[23]:


# 데이터를 모델에 넣을 수 있는 형태로 변환
input_data = df['ID_encoded'].values.reshape(-1, 1)

# 임베딩 레이어를 통과
embedded_data = embedding_layer(input_data)

# We can print the output directly
print(embedded_data[0:5])


# In[ ]:




