# Extract the domain name from a URL

# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

