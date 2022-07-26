# -*- coding: utf-8 -*-
"""Classification of Articles.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FzVQvQkuKeNk8FSoej9SGZ4DIO8d8bK4
"""

from tensorflow.keras.layers import LSTM, Dense,Dropout,Embedding,Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import TensorBoard
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras import Input,Sequential
from tensorflow.keras.utils import plot_model
import pandas as pd
import numpy as np
import datetime
import pickle
import json
import os
import re

#%%
LOGS_PATH = os.path.join(os.getcwd(),'logs',datetime.datetime.now().
                         strftime('%Y%m%d-%H%M%S'))

TOKENIZER_SAVE_PATH = os.path.join(os.getcwd(),'saved_models','tokenizer.json')
OHE_SAVE_PATH = os.path.join(os.getcwd(),'saved_models','ohe.pkl')
MODEL_SAVE_PATH = os.path.join(os.getcwd(),'saved_models','model.h5')

#%%
# Data loading
df = pd.read_csv('https://raw.githubusercontent.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial/master/bbc-text.csv')

#%% Data Inspection
df.head()

df.describe().T 
# Data has 5 categories, with Sport as the most frequent theme
# Data has 2225 articles with 2126 unique article (this means there are duplicates)

df.info()
# data has 2 objects

category = df['category'] 
article = df['text']

category.unique()

#df['category']
df['text'][5]

#%% Data cleaning

df.duplicated().sum()

df = df.drop_duplicates()

df.shape

# Removing unnecessary symbols and changing the words to lowercase
for index,text in enumerate(article):
    article[index]=re.sub('<.*?','',text) 
    article[index]=re.sub('[^a-zA-Z]',' ',text).lower().split()

vocab_size = 10000
oov_token = '<OOV>'

tokenizer = Tokenizer(num_words=vocab_size,oov_token=oov_token)
tokenizer.fit_on_texts(article)
word_index = tokenizer.word_index

print(dict(list(word_index.items())[0:10]))
# 10 words and its associated numbers

article_int = tokenizer.texts_to_sequences(article) #convert to numbers

length_article = []
for i in range(len(article_int)):
    length_article.append(len(article_int[i]))

print(np.median(length_article))

max_length = np.median(length_article)

max_length
# This value will be used for padding articles with less than 335 in length.

#%% Data Preprocessing

padded_review = pad_sequences(article_int,maxlen=int(max_length),
              padding='post',truncating='post')
# Making the articles length the same by using padding

#Y target - category
ohe=OneHotEncoder(sparse=False)
category = ohe.fit_transform(np.expand_dims(category,axis=-1))

# Splitting data
X_train,X_test,y_train,y_test=train_test_split(padded_review, category,
                                               test_size=0.3, random_state=123)

#%% Model Development

input_shape = np.shape(X_train)[1:]
out_dim=128

model= Sequential()
model.add(Input(shape=input_shape))
model.add(Embedding(vocab_size,out_dim))
model.add(Bidirectional(LSTM(128,return_sequences=True)))
model.add(Dropout(0.3))
model.add(Bidirectional(LSTM(128)))
model.add(Dropout(0.3))
model.add(Dense(5,activation = 'softmax'))
model.summary()

model.compile(optimizer='adam',loss='categorical_crossentropy',
              metrics=['accuracy'])

tensorboard_callback = TensorBoard(log_dir=LOGS_PATH,histogram_freq=1)

model.fit(X_train,y_train,validation_data=(X_test,y_test),
          epochs=5,callbacks=[tensorboard_callback])

#%reload_ext tensorboard
#%tensorboard --logdir logs

#%% Model analysis

y_pred = np.argmax(model.predict(X_test), axis=1)
y_actual = np.argmax(y_test,axis=1)

print(classification_report(y_actual,y_pred))

#%% Model saving

# Tokenizer
token_json = tokenizer.to_json()

with open(TOKENIZER_SAVE_PATH,'w') as file:
    json.dump(token_json,file)

# OHE
with open(OHE_SAVE_PATH, 'wb') as file:
    pickle.dump(ohe,file)

# MODEL
model.save(MODEL_SAVE_PATH)

plot_model(model,show_shapes=(True,False),show_layer_names=True)

# from google.colab import files
# !zip -r /content/logs.zip /content/logs

# files.download('/content/logs.zip')