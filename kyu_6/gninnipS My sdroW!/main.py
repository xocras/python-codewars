# gninnipS My sdroW!
# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')])
