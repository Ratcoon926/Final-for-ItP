# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:13:43 2024

@author: Ratcoon
"""
#Right of the bat, to explain what I'm doing here: This code takes the most common words from a website, and then it puts those onto a text file!

#So this set of lines beneath just calls for important features. Requests is a library used to make HTTP requests, BeautifulSoup is used to parse/extract info from HTML/XML docs, Counter is used to count occurences of items (Very important considering my project idea, lastly, re is used for regular expressions, which is important for formatting and cleaning anything extracted from a webpage.
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# So what this set of three does is it takes a URL, which you provide, and gets the content of the website page, and putting it into text format.
url = 'https://serebii.net'  # I have put the website "Serebii.Net", but this should work with any website.
response = requests.get(url)
html_content = response.text

# What this set of 2 lines does is it takes the text file obtained from the 3 lines above and parses it, and gets a more understandable version of what's obtained above.
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()

# The next 2 here do even more of what has already been done above: it cleans up the text. Specifically, it removes non-alphabet characters, and converts it all to lowercase, spliting up the words as well.
text = re.sub(r'[^A-Za-z\s]', '', text)
words = text.lower().split()

# Now what this does, is it removes all the words below from the top word counter, you can also use some code to remove words that are shorter than a certain character limit, but I went with this, might change it in the future, if it has a bunch of complications, which I kinda think it will
stopwords = set([
    'the', 'and', 'is', 'in', 'to', 'a', 'of', 'for', 'on', 'it', 'this', 'that', 
    'with', 'as', 'by', 'at', 'an', 'from', 'or', 'are', 'be', 'was', 'not', 'we', 'you', 'go', 'th'
])
filtered_words = [word for word in words if word not in stopwords]

# All's this does is it counts the occurences of each unique word, not including the words within the stopword code.
word_counts = Counter(filtered_words)

# This takes alllll the words counted from the line above and sorts them in order of the most instances, up to the top three. If you wanted to, you can also change the number in the () to change how large the list is. Currently it is the top 3 though.
most_common_words = word_counts.most_common(3)

# This will open a text file (Creates one in that name if it doesn't already exist) on your PC and write to it the most common words.
with open('most_common_words.txt', 'w') as file:
    for word, count in most_common_words:
        file.write(f"{word}: {count}\n")

print("The 3 most common words have been saved to 'most_common_words.txt'.")