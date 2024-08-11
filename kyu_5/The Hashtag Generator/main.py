# The Hashtag Generator

# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    hashtag = '#' + ''.join(x for x in s.title().split())
    return hashtag if s and len(hashtag) <= 140 else False
