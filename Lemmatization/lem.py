from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

sentence = "Come on come on turn the radio on, it's Friday night and I won't be long. Gotta do my hair, I put my " \
           "make up on it's friday night and I won't be long. Til I hit the dance floor, hit the dance floor. I got" \
            " all i need."

pts = PorterStemmer()
final = " ".join([pts.stem(i) for i in sentence.split()])

wnl = WordNetLemmatizer()
final2 = " ".join([wnl.lemmatize(i) for i in sentence.split()])
print("Sentence:", sentence)
print("Stemming:", final)
print("Lemmatization:", final2)
