import sys
import json
import nltk
from textblob import TextBlob
from nltk.stem import PorterStemmer
from .sentiment_util import english_stop_words
from nltk.tokenize import word_tokenize
from textblob.sentiments import NaiveBayesAnalyzer


def format_input(user_input):
    formatted_words = []
    return_text = ""

    porter_algorithm = PorterStemmer()
    stop_words = english_stop_words

    # Tokenize the text by word and remove punctuation.
    words = word_tokenize(user_input)
    tokenized_words = [word.lower() for word in words if word.isalpha()]

    if len(user_input) != 0:
        for in_word in tokenized_words:
            if in_word not in stop_words:
                stemmed_word = porter_algorithm.stem(in_word)
                formatted_words.append(stemmed_word)

    for word in formatted_words:
        return_text += (word + " ")

    return return_text


def get_sentiment(argued_text):
    formatted_argued_text = TextBlob(
        argued_text, analyzer=NaiveBayesAnalyzer())
    return formatted_argued_text.sentiment


def convert_data_to_json(text, sentiment_data):
    if abs(sentiment_data.p_pos - sentiment_data.p_neg) <= .05:
        return_classification = "Neutral"
    elif sentiment_data.classification is "pos":
        return_classification = "Positive"
    else:
        return_classification = "Negative"

    return {
        "argued_text": text,
        "classification": return_classification,
        "percent_posative": sentiment_data.p_pos,
        "percent_negative": sentiment_data.p_neg
    }


def sentiment_analyzer(input_text):
    entered_text = format_input(input_text)
    sentiment_data = get_sentiment(entered_text)
    json_response = convert_data_to_json(input_text, sentiment_data)
    return json_response
