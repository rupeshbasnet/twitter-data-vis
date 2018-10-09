import nltk
import numpy as np,pandas as pd
import matplotlib.pyplot as plt 
import nltk.data
import re
from nltk.stem.porter import *
pd.options.mode.chained_assignment = None

df = pd.read_csv("clean_data.csv")

# step 1 stop word removal
short_data = df.head()
from nltk.corpus import stopwords
stop = stopwords.words("english")

print(short_data['text'])
print('-------Remove Stop Word--------')
short_data['Step1_SentimentText'] = short_data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
print(short_data['Step1_SentimentText'])
#clean = short_data['Step1_SentimentText']
#clean = re.sub('@[^\s]+','',clean)


