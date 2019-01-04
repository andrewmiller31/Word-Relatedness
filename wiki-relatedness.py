# Andrew Miller 11/20/18
#
# wiki-relatedness.py
# The purpose of this program is to find the relatedness between two Wikipedia 
# articles based on the words that occur. This is done by taking the first n 
# words from each article and checking which words overlap. The measure for
# relatedness is found by simply dividing the number of overlaps by n.
# To eliminate noise and give a more accurate relatedness approximation,
# stop words are ignored when choosing the first n words. A stop word is a 
# commonly occuring word (the, and, or, etc.) that would act as noise if they
# weren't filtered out. 
#
# The stop words selected by randomly choosing 100 Wikipedia pages over 1000
# words and tracking which words occur in at least 75% of the articles.
#
# All words are processed to be in lowercase and have no punctuation in hopes
# of improving the number of words that overlap.
#
# To run:
# python wiki-relatedness.py <numpy array of stop words>
# input n
# input for word 1 and word 2 until one of them is set as EXITNOW

import wikipedia as wp # wikipedia library
import re # regular expressions
import sys # used for taking command line args
import numpy as np # used for array loading

# stop word array that will be populated when you run the program
stop = []

# This function removes non-alphanumeric characters, converts to all lowercase,
# and splits a string into an array of words.
def process_article(a):
  a = a.lower() # lowercase
  # sub anything other than number, letter, or space, with nothing
  a = re.sub(r"[^0-9a-z\s]",'',a) 
  return a.split() # return as an array of words

# This function finds the first n words in an article, filtering out stop words
def get_n_words(a,n):
  global stop # use the defined list of stop words
  # convert text into an array of lowercase strings with no punctuation
  words = process_article(a) 
  # create dictionary to track the words
  # key-value pair will be (word : count)
  n_words = {}
  i = 0 #iterator
  count = 0 # count for how many words have been found
  # while there are words available and n words haven't been taken yet
  while i < len(words) and count < n:
    w = words[i] # select current word
    if w not in stop: # filter out stop words
      count += 1 # add to count if it's a valid word
      # either add word with count of 1 or add 1 to existing word
      if w in n_words: 
	n_words[w] += 1
      else:
	n_words[w] = 1
    i += 1
  # return the dict
  return n_words

# This function counts the number of words in common between two dictionaries
# The dicts should have the key-value pair of word : count
def words_in_common(a1,a2):
  common = [] # array to track overlapping words
  count = 0 # count of how many overlapping words there are
  # for each key(word) in a1, check if it exists in a2
  for k in a1.keys():
    if k in a2:
      # if it exist, add to count the count of the dict with the lower value
      # because that's how many we can count as an overlap
      count += a1[k] if a1[k] > a2[k] else a2[k]
      common.append(k) # add word to list of overlapping
  return count,common # return tuple of count and overlapping array

# This function compares two wikipedia pages to see how related they are
# It takes in two words as input, as well as n, the number of words to use
def comp_words(w1,w2,n):
  # try to open the two pages. If either do not exist, then there are no words
  # in common so the relatedness is -1.0000
  try:
    a1 = wp.WikipediaPage(w1)
    a2 = wp.WikipediaPage(w2)
  except:
    print_results('-1.0000',[])
    return # return because no further processing is needed
  # get n words from each page
  words1 = get_n_words(a1.content,n)
  words2 = get_n_words(a2.content,n)
  # print a warning message if n words are not found in either of them
  # if there are less then n words, the results will be inaccurate
  if sum(words1.values()) != n or sum(words2.values()) != n:
    print 'Warning: at least one of the articles is not long enough for',n,'words'
  # find all the words that overlap between the two pages
  count,common = words_in_common(words1,words2)
  # calculate the relatedness ( # words in common / n)
  r =  float(count) / n 
  # format to 4 decimal places
  r = "{0:.4f}".format(r)
  # print the relatedness measure along with all words in common
  print_results(r,common)  

# a function that takes in the input words
def get_input():
  w1 = raw_input('Input word 1: ')
  w2 = raw_input('Input word 2: ')
  return w1,w2

# a function that prints the relatedness results
# r is the relatedness
# c is the list of words in common
def print_results(r,c):
  overlaps = ''
  # concatenate the words into a single string
  for o in c:
    if overlaps == '':
      overlaps += o
    else:
      overlaps += ', ' + o
  print 'relatedness:',r
  print 'overlaps:',overlaps,'\n'



def main():
  global stop
  # load the stop word list from the command line argument
  st = sys.argv[1]
  stop = np.load(st)
  # read n
  n = input('Input N value: ')
  # read input for words and calcuate relatedness until one of the words is
  # EXITNOW
  w1,w2 = get_input()
  while w1 != 'EXITNOW' and w2 != 'EXITNOW':
    comp_words(w1,w2,n)
    w1,w2 = get_input()

if __name__ == "__main__":
  main()
