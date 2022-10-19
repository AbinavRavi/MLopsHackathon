import numpy as np
import pandas as pd
from tqdm import tqdm

import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer  


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
def clean_text(text):
    
    sw = stopwords.words('english')
    lemmatizer = WordNetLemmatizer() 
    text = text.lower()
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    text = re.sub(r"[^a-zA-Z?.!,¿]+", " ", text) 
    #Removing URLs 
    text = re.sub(r"http\S+", "",text) 
    #text = re.sub(r"http", "",text)
    html=re.compile(r'<.*?>') 
    text = html.sub(r'',text) #Removing html tags
    punctuations = '@#!?+&*[]-%.:/();$=><|{}^' + "'`" + '_'
    for p in punctuations:
        text = text.replace(p,'') #Removing punctuations   
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    text = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(text) #removing stopwords
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text) #Removing emojis
    return text


def get_label(text):

    labels = {'elonmusk': 0 ,
              'kanyewest': 1
    }

    text = labels[text.split('/')[1]]
    return text


df = pd.read_csv('kanye_elon_1900.csv')
df['text'] = df['text'].apply(lambda x: clean_text(x))
df['target'] = df['source'].apply(lambda x: get_label(x))
print(df.target.unique())

print(df.shape)
print(df.columns)

X_train, X_test , y_train, y_test = train_test_split(df['text'].values,df['target'].values, 
                                                     test_size=0.2, random_state=123, 
                                                     stratify=df['target'].values
                                    )

tfidf_vectorizer = TfidfVectorizer() 
tfidf_train_vectors = tfidf_vectorizer.fit_transform(X_train)
tfidf_test_vectors = tfidf_vectorizer.transform(X_test)

clf = RandomForestClassifier()

clf.fit(tfidf_train_vectors,y_train)

y_pred = clf.predict(tfidf_test_vectors)
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

# import pdb; pdb.set_trace()

# test = np.array('yo i am rapper').reshape(-1)
# test = np.array(" let's go to Mars").reshape(-1)
# test_vec = tfidf_vectorizer.transform(test)
# print(clf.predict(test_vec))

