# Cat years, Dog years

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]

