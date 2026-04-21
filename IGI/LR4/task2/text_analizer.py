"""
Module for Task 2.
Provides a TextAnalyzer class that uses regular expressions for text processing.
Includes functions for counting sentence types, extracting phone numbers,
calculating average word lengths, and archiving results into a ZIP file.
"""

import re

class TextAnalyzer:
    """
    A class to perform various text analysis tasks using regular expressions.
    """

    def __init__(self, text):
        """Initializes the analyzer with the target text"""
        self.text = text

    def phone_numbers(self):
        """Finds all phone numbers starting with '29' and having 9 digits total"""
        return re.findall(r'\b29\d{7}\b', self.text)

    def list_words(self):
        """Finds words where the second letter is a consonant and the third is a vowel"""
        return re.findall(r'\b\w[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz][aeiouyAEIOUY]\w*', self.text)

    def end_with_constant(self):
        """Counts the number of words ending with a consonant"""
        words = re.findall(r'\w*[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz]\b', self.text)
        return len(words)

    def average_length(self):
        """
        Calculate average length and words with average length
        :return : A tuple (average length, list of words with this length)
        """
        words = re.findall(r'\w+', self.text)

        if len(words) == 0:
            return 0, []

        total_length = 0

        # calculate total length of te words
        for word in words:
            total_length += len(word)

        # calculate average length of the words
        avg_length = round(total_length / len(words))

        # find words with average length
        avg_length_words = []
        for word in words:
            if len(word) == avg_length:
                avg_length_words.append(word)

        return avg_length, avg_length_words

    def seventh_words(self):
        """
        Finds every seventh word
        """
        words = re.findall(r'\w+', self.text)

        return words[6::7]

    def smile(self):
        """Counts the number of smiles"""
        smiles = re.findall(r'[;:]-*[\(\)\[\]]+', self.text)
        return len(smiles)

    def analyze_sentences(self):
        """
        Analyzes the structure of the text
        :return: Tuple containing counts of (total, declarative, interrogative, exclamatory).
        """
        sentences = re.findall(r'[^.!?]+[.!?]', self.text)
        total = len(sentences)

        declarative = len(re.findall(r'[^.!?]+\.', self.text)) # .
        interrogative = len(re.findall(r'[^.!?]+\?', self.text)) # ?
        exclamatory = len(re.findall(r'[^.!?]+\!', self.text)) # !

        return total, declarative, interrogative, exclamatory