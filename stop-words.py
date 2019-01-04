# Andrew Miller 11/21/18
# stop-words.py
#
# This program randomly chooses Wikipedia articles and compares the words 
# between them to generate a list of stop words. The articles sampled are all
# at least 1000 words long and stop words are defined as words that occur in at
# least 75% of the articles. The array of stop words that are found are saved
# as a numpy array.
#
# To run:
# stop-words.py <array name>
# The results are saved in a file called <array name>.npy
# Each stop word found is also printed so you can see what the stop words are
# 
import wikipedia as wp # wikipedia library
import re # regular expressions
import numpy as np # for saving the array
import sys # for taking in args

# number of random articles to use
n = 100

# This function processes a wiki page and creates a list of each token type
def process_article(a):
  # normalize the text
  a = a.lower()
  a = re.sub(r"[^0-9a-zA-Z\s]",'',a)
  a = a.split()
  # check if we have a valid article, return none if we dont
  if len(a) < 1000:
    return None
  # find each unique word in the article and return as a list
  types = []
  for w in a:
    if w not in types:
      types.append(w)
  return types

# This function chooses n random wiki pages to find stop words in.
# n is defined above
def random_pages():
  # 2d array that stores an array for each random article with the unique word
  # types found in each
  pages = [] 
  # loop until we have n articles
  while len(pages) < n:
    valid = False
    # choose new article until we have a valid one
    while valid == False:
      try:
	# randomly choose a wiki article
        p = wp.WikipediaPage( wp.random(1) ) 
        valid = True
	# if None is returned, then article is not valid
        words = process_article(p.content)
        if words == None:
          valid = False
        else: 
	  # if it's valid, append to pages
	  pages.append(words)
      # simply ignore ambiguous articles instead of choosing which sense
      except wp.exceptions.DisambiguationError:
        valid = False
  return pages
  
def main():
  title = sys.argv[1] # take in name for stop list
  pages = random_pages() # choose n random pages
  types = {} # dict to track document frequency ( word : count )
  # find document frequency of each type
  for p in pages:
    for w in p:
      if w not in types:
        types[w] = 1
      else:
        types[w] += 1

  stop = [] # array of stop words
  for k in types.keys(): 
    # if the word appears in 75% of the articles, it's a stop word
    if types[k] >= (.75*n):  
      stop.append(k)
      print k 
  # save the stop word list as a numpy array, using the user provided title
  np.save(title,np.array(stop))

if __name__ == "__main__":
  main()

