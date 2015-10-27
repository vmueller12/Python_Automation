import nltk

#nltk.download()

# tokenizing - 1. word tokenizers (seperates by text)  2. sentence tokenizer (seperates by sentence)

# lexicon and corporas
# corpora - body of text. ex: medical journals, presidental speeches, English language
# lexicon - words and their means

# investor speak .... regular english speak

# investor speak bull = someone who is positive about the market
# english speak bull = scary animal you dont want running at you :)

from nltk.tokenize import sent_tokenize, word_tokenize


example_text = "Hello Mr. Smith there, how are you doing today? The weather is great and Python is awsome."

# prints a list splitted by sentence
print (sent_tokenize(example_text))
# prints a list splitting by words
print (word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)

