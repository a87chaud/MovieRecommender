import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
import tensorflow as tf

def pre_process(root_dir):
    corpus = []
    
    for dirs, subdirs, files in os.walk(root_dir):
        for file in files:
            curr_file = open(os.path.join(dirs,file), 'r')
            data = curr_file.read()
            # Each file is a string 
            # Need to remove specials chars + lower case + tokenize
            data = data.lower()
            file_str = re.sub(r'[^a-z ]', '', data)
            corpus.append(file_str)
    
    return corpus
    
            

tfidf_train = TfidfVectorizer(min_df = 1, max_df = 0.8, ngram_range=(1,2))
corpus = pre_process('./train/test_folder')
X_train = tfidf_train.fit_transform(corpus)
print(tfidf_train.get_feature_names_out())
# df = pd.DataFrame(features.todense(), columns = tfidf_train.get_feature_names_out()())
# print(df)