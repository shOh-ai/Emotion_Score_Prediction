#!/usr/bin/env python
# coding: utf-8

# ## 1. 데이터 불러오기

# In[3]:


import pandas as pd

df = pd.read_csv('/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/video_id.csv')


# ## 2. One-hot encoding

# In[14]:


from sklearn.preprocessing import OneHotEncoder

# Initialize OneHotEncoder
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Perform one-hot encoding
one_hot_encoded = one_hot_encoder.fit_transform(df['video_ID'].values.reshape(-1, 1))

# Convert the result back to a dataframe
df_encoded = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.categories_[0])

# Display the first few rows of the dataframe
print(df_encoded.head())

