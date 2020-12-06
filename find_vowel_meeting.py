'''
  receives a word in string format,
  returns vowel meeting (tritongo, ditongo, hiato) or None
'''
#-----------------------------------------------------------------------------
#Files, libs and packages needed

# Regex
import re

from word_syllables import *
from word_to_cv import *

#-----------------------------------------------------------------------------

def find_vowel_meeting(word):
  stop_flag = False
  word = word.lower()
  vowel_meeting_pattern = re.compile(r'[^V]*(V{2,3})[^V]*') #pattern to find vowel meeting in word

  #vowel patterns in syllables
  triphthong_pattern = re.compile(r'[^V](V{3})[^V]')
  diphthong_pattern  = re.compile(r'[^V](V{2})[^V]')
  gap_pattern  = re.compile(r'[^V]V[^V]')


  if(vowel_meeting_pattern.search(word_to_cv(word))): #If theres vowel meeting, which one is?
    #split into syllables
    syllables = word_syllables(word) #calls method to split word into syllables
    syllables_to_cv = [] #holds the CV enconded syllables
    #converts syllables to CV encoding
    for syllable in syllables:
      syllables_to_cv.append('_' + word_to_cv(syllable) + '_') #add marker (underline) at the beginning and end of the syllable

    #searchs for vowel meeting in CV enconded syllables
    #1st search for triphthong
    if(not stop_flag):
      for cv_syllable in syllables_to_cv:
        if(triphthong_pattern.search(cv_syllable) ):
          stop_flag = True
          return 'tritongo'
        else:
          continue

    #2nd search for diphthongs
    if(not stop_flag):
      for cv_syllable in syllables_to_cv:
        if(diphthong_pattern.search(cv_syllable) ):
          return 'ditongo'
        else:
          continue

    #3rd search for gaps
    if(not stop_flag):
      for cv_syllable in syllables_to_cv:
        if(gap_pattern.search(cv_syllable) ):
          return 'hiato'
        else:
          continue
  else:
    # Theres no vowel meeting
    return None

#Tests - Satus = OK
# gap_examples = [ 'saída', 'poético', 'saúde', 'ciúme', 'país']
# print('\n--todos devem ser hiatos--')
# for example in gap_examples:
#   print(example, find_vowel_meeting(example))