# Steps:
# 1. Read the text files
# 2. Lowercase words and remove URLs
# 3. Join all the text files into a single string
# 4. Tokenize the string into individual words
# 5. Remove stopwords and punctuation from the list of words
# 6. Stem the filtered words using the Snowball stemmer
# 7. Lemmatize the stemmed words using the WordNet lemmatizer
# 8. Count the frequency of each word in the list
# 9. Sort the word counts in descending order
# 10. Write the sorted word counts to a CSV file

# Import necessary libraries
import glob
import re
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import string
from collections import defaultdict


# Define the path of the directory containing the text files to be processed
# Need to be modified for different users
txt_files = glob.glob("F:/.../WK 0221/Py/texts/**/*.txt", recursive=True)

# Create an empty list to store the text from the files
text = []

# Loop over each text file and append the content to the list
for txt_file in txt_files:
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read().lower()

        # Remove URLs from the content using regular expressions
        content_without_urls = re.sub(r"http\S+", "", content)
        contents = re.sub(r"www\S+", "", content_without_urls)
        text.append(contents)

# Join the text from all files into a single string
content = " ".join(text)

# Tokenize the string into individual words
words = nltk.word_tokenize(content)

# Remove stopwords and punctuation from the list of words
stop_words = set(stopwords.words('english'))

punctuations = set(string.punctuation)
filtered_words = []
for word in words:
    if word not in stop_words:
        filtered_word = ''.join(ch for ch in word if ch not in punctuations)
        if filtered_word:
            filtered_words.append(filtered_word)

# Stem the filtered words using the Snowball stemmer
stemmer = SnowballStemmer('english')
stemmed_words = []
for word in filtered_words:
    stemmed_word = stemmer.stem(word)
    stemmed_words.append(stemmed_word)

# Lemmatize the stemmed words using the WordNet lemmatizer
lemma = nltk.wordnet.WordNetLemmatizer()
lemma_words = []
for word in stemmed_words:
    lemma_word = lemma.lemmatize(word)
    lemma_words.append(lemma_word)

# Count the frequency of each word in the list
word_counts = defaultdict(int)

for word in filtered_words:
    word_counts[word] += 1

# Sort the word counts in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Write the sorted word counts to a CSV file
# with open('unigram.csv', 'w', encoding='gb18030', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(sorted_word_counts)
