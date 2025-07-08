import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences 

def tokenize_sentences():
    sentences = [
        'I love my dog',
        'I love my cat',
        'You love my dog!',
        'Do you think my dog is amazing?'
    ]
    tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    word_index = tokenizer.word_index
    sequences = tokenizer.texts_to_sequences(sentences)
    
    padded_sequences = pad_sequences(sequences,maxlen=10)
    print("Word Index from Tokenizer:")
    print(word_index)
    print("Sequences from Tokenizer:")
    print(sequences)
    print("Padded Sequences:")
    print(padded_sequences)

    

def tokenize_sentences1():
    sentences = [
        'I really love my dog',
        'my dog loves my manatee'
    ]
    tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)
    sequences = tokenizer.texts_to_sequences(sentences)
    print("Sequences from Tokenizer1:")
    print(sequences)
