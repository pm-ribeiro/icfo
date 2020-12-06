#-----------------------------------------------------------------------------
#Files, libs and packages needed

from search_word_in_vop import *
from find_vowel_meeting import *
from word_to_cv import *
from word_syllables import *

#spaCy related
import spacy
nlp_spacy = spacy.load("pt_core_news_sm")

#-----------------------------------------------------------------------------

def validate_target_word(misspelled_word, target_word):
  found = False
  found_word = {}
  
  # searchs in VOP
  if(search_word_in_vop(path_to_vop_set, target_word)):
    found = True  
  else: # searchs in dicio
    if(dicio.search(target_word)):
      found = True 

  if(found):
    #gets POS
    for token in nlp_spacy(target_word):
      POS = token.pos_
    # concatena os elementos do array por -
    syllables = "-".join(word_syllables(target_word))

    found_word.update({
      "misspelled_word": misspelled_word,
      "target_word": target_word,
      "POS": POS, 
      "syllabic_separation": syllables, 
      "vowel_meeting":  find_vowel_meeting(target_word),
      "cvs_encoding":  word_to_cv(target_word),
    })
    return found_word
  else:
    return False

#Tests - Status = OK
# misspelled_word = "palabra"
# target_word = "palavra"
# print(validate_target_word(misspelled_word, target_word))