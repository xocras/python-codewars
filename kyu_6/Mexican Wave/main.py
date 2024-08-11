# Mexican Wave

# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

def wave(people):
    return [people[0:i].lower() + people[i].upper() + people[i+1:].lower() for i, x in enumerate(people) if x.strip()]

