import pandas as pd


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Replace 'all-the-news.csv' with the actual file name or URL to the CSV file
data1 = pd.read_csv('articles1.csv')
data2 = pd.read_csv('articles2.csv')
data3 = pd.read_csv('articles3.csv')

data = pd.concat([data1, data2, data3], ignore_index=True)
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # Tokenize and convert to lower case
    tokens = nltk.word_tokenize(text.lower())
    
    # Remove stopwords and non-alphabetic characters
    words = [word for word in tokens if word.isalpha() and word not in stop_words]
    
    # Lemmatize words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(lemmatized_words)

# Apply preprocessing to your dataset
data['processed_text'] = data['content'].apply(preprocess)

# Vectorize the preprocessed text using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['processed_text'])

