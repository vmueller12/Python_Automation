# Stemming form of data pre processing
# root stemp writting -> wrid
# different variation of words but the actual meaning is unchanged

from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

# ps instance of the PorterStemmer class
ps = PorterStemmer()

# sample list of different python words
example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# stemming the the python words list
stem_words = [ps.stem(w) for w in example_words]

#print(stem_words)

# another example for stemming different words
new_text = "It is very important to be pythoning with python. All pythoners have pythoned."

# tokenizing, splitting the new_text sentence by words
words = word_tokenize(new_text)

# list comprehension, looping through the words list and stemming individual words
print([ps.stem(w) for w in words])

#print(stem_words_new)
