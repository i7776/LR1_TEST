"""
Task №4:
a) Counts how many words end with a consonant letter
b)
"""

"""
Correction of the text
"""

def correction_text():
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

    text = text.replace(',', ' ')
    text = text.replace('.', ' ')

    words_list = text.split()
    return words_list


def words_with_consonants_at_the_end(text):

    """
    Counts how many words end with a consonant letter
    :param text: words of the text
    :return :count with consonants at the end
    """

    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0

    for word in text:
        if word[-1] in consonants:
            count += 1


    return count

def average_length(text):

    """
    Calculate average length and words with average length
    :param text: words of the text
    :return :if count=0 returns zero, else returns average length and list of the words with average length
    """

    count = 0
    total_length = 0

    # calculate total length of te words
    for word in text:
       total_length += len(word)

    # calculate average length of the words
    avg_length = round(total_length / count)

    # find words with average length
    avg_length_words = []
    for word in text:
        if len(word) == avg_length:
            avg_length_words.append(word)

    if count != 0:
        return avg_length, avg_length_words
    else:
        return avg_length

def seventh_words(text):

    count = 0
    seventh_words = []

    for word in text:
        count += 1
        if count == 7:
            count = 0
            seventh_words.append(word)

    return seventh_words





