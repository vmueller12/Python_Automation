from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration"

# assigning stop words from english language 
stop_words = set(stopwords.words("english"))

# print out all stopwords which are stored in the corpus stopwords lib
#print(stop_words)

# spliting the sentence by words
words = word_tokenize(example_sentence)
# list comprehension 
filtered_sentence = [w for w in words if w not in stop_words]

print(filtered_sentence)
#print('-----')
#print(words)

