import string

from cullo.services.training_preprocessing.training import train_data

import spacy
from sklearn.svm import SVC
import numpy as np

print("In Interpretor")

nlp = spacy.load('en', vectors='en_glove_cc_300_1m_vectors')
clf = SVC()

def preprocess():
    """
    This mathod takes dataframe as an input, and trains support vector model
    """
    print("preprocess starts")
    final_df = train_data()
    messages = final_df['msg'].tolist()
    intents = final_df['intent_value'].tolist()

    n_msg = len(messages)
    #embedding_dim = nlp.vocab.vectors_length

        # vector representation of all messages

    X_shape = (n_msg, 384)

    X_train = np.zeros(X_shape)

    for i, message in enumerate(messages):
            # Pass each each sentence to the nlp object to create a document

        #doc = nlp(unicode(message))
        doc = nlp(message)
            # Save the document's .vector attribute to the corresponding row in X
        X_train[i, :] = doc.vector

    clf.fit(X_train, intents)
    print("preprocess ends")

def interpret(message):
    """This method takes message as an input and
        returns the intent of the message"""
    msg = message.lower()
    """if 'order' in msg:
        return 'order'
    if 'black' in msg or 'green' in msg:
        return 'specify_tea'"""
    if any([d in msg for d in string.digits]):
        return 'number'
    X_test = nlp(message).vector
    y_pred = clf.predict(X_test.reshape(1, -1))
    if y_pred == 0:
        return "atis_flight"
    if y_pred == 1:
        return "atis_airfare"
    return 'none'
