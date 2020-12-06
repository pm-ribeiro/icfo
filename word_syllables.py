'''
  Receives a word in string format
  returns an array containing the word's syllabic separation
  if the syllabic separation is not found, returns a warning
  Uses VOP + Dicio + PyHyphen
'''

#-----------------------------------------------------------------------------
#Files, libs and packages needed

from search_word_in_vop import *

#Dicio related
from dicio import Dicio # import the dictionary
dicio = Dicio() # Create a Dicio object

#PyHyphen related
from hyphen import Hyphenator
pt_br = Hyphenator('pt_BR')

#-----------------------------------------------------------------------------

def word_syllables(word):
  syllables = ""
  word = word.lower()
  word_copy = {}

  # tries syllabification by VOP
  word_copy = search_word_in_vop(path_to_vop_set, word)

  if(word_copy):
    syllables = word_copy['syllabic_separation']
    if(syllables != ''):
      syllables = syllables.split('·') #transform into an array of syllabless
      return syllables

  # tries syllabification by DICIO
  word_copy = dicio.search(word)
  #searches for the word in the dictionary, if it exists searchs syllables
  if(word_copy):
    for k, v in word_copy.extra.items():
      if(k == 'Separação silábica'):
        syllables = v
    if(syllables != ''):
      syllables = syllables.split('-') #transform into an array of syllables
      return syllables

  # attempts syllabification by PyHyphen if 'syllables' still be an empty string
  syllables = pt_br.syllables(word)
  if(syllables != ''):
    return syllables

  # in case no syllabification is found by any method return warning
  if(syllables == ''):
    return "silabificação ainda não disponível"


#Test - Status = OK
# example = 'menino'
# print(example, word_syllables(example))