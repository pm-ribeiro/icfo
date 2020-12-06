#libraries and packages

#NLTK related
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

#spacy related
import spacy
import spacy.cli
spacy.cli.download("pt_core_news_sm")

import pt_core_news_sm
nlp_spacy = pt_core_news_sm.load()

#Dicio related
from dicio import Dicio # import the dictionary
dicio = Dicio() # Create a Dicio object

#PyHyphen related
from hyphen import Hyphenator
pt_br = Hyphenator('pt_BR')

#Docx
import docx

#Time related
import time
import timeit
import datetime

from string import punctuation

#plot related
# import matplotlib.style as style
# style.use('seaborn-poster')

# Regex
import re

#csv related
import csv

#Other libs
import os
# from collections import defaultdict
# from heapq import nlargest
# import pandas as pd

#----------------------------------------------------------------------------