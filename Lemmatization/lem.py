from nltk.stem import WordNetLemmatizer


sentence = "Come on, come on turn the radio on. It's friday night and I won't be long."
wnl = WordNetLemmatizer()

final = " ".join([wnl.lemmatize(i) for i in sentence.split()])
print(final)
