import json
import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords

data = pd.read_csv("clean_data.csv")

string_type = data.astype(str)
