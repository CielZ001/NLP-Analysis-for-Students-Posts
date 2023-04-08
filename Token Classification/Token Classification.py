import csv
import re
import glob
from flair.data import Sentence
from flair.models import SequenceTagger

txt_files = glob.glob("F:/.../texts/**/*.txt", recursive=True)
# print(txt_files)
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
# content = " ".join(text)

# load tagger
tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

txt = []
tags = []
c = 0

for content in text:
    # make sentence
    sentence = Sentence(content)
    # predict NER tags
    tagger.predict(sentence)

    # iterate over entities and print
    for entity in sentence.get_spans('ner'):

        if entity.tag == 'EVENT' or entity.tag == 'PRODUCT' or entity.tag == 'WORK_OF_ART':
            txt.append(entity.text)
            tags.append(entity.tag)

    print(c)
    c += 1
# print sentence
# print(sentence)

# print predicted NER spans
# print('The following NER tags are found:')


# print the entity text and its type
# print(entity.text, entity.tag)

# go through each token in entity and print its idx
# for token in entity:
#     print(token.idx, token.text)
with open('t_c.csv', 'w', encoding='gb18030', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Text', 'Tag'])
    # Write each row with data from the two lists
    for i in range(len(txt)):
        writer.writerow([txt[i], tags[i]])
