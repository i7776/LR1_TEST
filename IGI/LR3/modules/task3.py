"""
Task №3: Count of punctuation marks
"""

def count_punc(str1):
    """
    Counts punctuation marks in a string
    :param str1: text
    : return: count of punctuation marks
    """
    count = 0
    punc_marks = ".,!?;:-()\"'"

    for elem in str1:
        if elem in punc_marks:
            count += 1

    return count




