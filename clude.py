import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

file = open('rushi.txt','r')
file_contents = file.read()

def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very"]

    frequencies = {}
    file_contents = file_contents.split()
    str1 = " "

    for word in file_contents:
        str1 =''.join(ch for ch in word if ch.isalnum())
        if str1.lower() not in uninteresting_words:
            if str1.lower() not in frequencies:
                frequencies[str1.lower()] = 1
            else:
                frequencies[str1.lower()] += 1

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
