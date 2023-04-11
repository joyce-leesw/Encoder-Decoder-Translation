import string
from keras.preprocessing.text import Tokenizer

# remove all the string punctuations
def clean_sentence(sentence):
    lower_case = sentence.lower()
    string_punctuation = string.punctuation + "¡" + '¿'    
    clean_sentence = lower_case.translate(str.maketrans('', '', string_punctuation))
    return clean_sentence

def tokenise(sentence):
    txt_tokeniser = Tokenizer()
    txt_tokeniser.fit_on_texts(sentence)
    return txt_tokeniser.texts_to_sequences(sentence), txt_tokeniser