'''
  [categoria 5]
  Consoante - Soante

  Subcategorias

          | exemplo | alvo
  nh → n  | cana    | canha
  lh → l  | cala    | calha
  lh → li | paliaço | palhaço

'''

# libraries and packages
#------------------------------------------------------------
#Time related
# import time
# import timeit
# import datetime

# Regex
import re

# importing my files
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

# import my_module  # Replace "my_module" here with the module name.
from validate_target_word import *
from change_letters import *
sys.path.pop(0)

#------------------------------------------------------------

# sub categories
category_5_1 = 'Consoante - Soante: nh → n' # nh → n  | cana    | canha
category_5_2 = 'Consoante - Soante: lh → l' # lh → l  | cala    | calha
category_5_3 = 'Consoante - Soante: lh → li' #  lh → li | paliaço | palhaço

# example: cana -> canha
def changes_n_nh(misspelled_word, s, e):
  word_rule_dict = {}
  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'n', s, e, 'nh')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_5_1,
    })
    return word_rule_dict
  else:
    return False

# example: cala -> calha
def changes_l_lh(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'l', s, e, 'lh')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_5_2,
    })
    return word_rule_dict
  else:
    return False

def changes_li_lh(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'li', s, e, 'lh')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_5_3,
    })
    return word_rule_dict
  else:
    return False


def category_5(misspelled_word):
  misspelled_word = misspelled_word.lower()
  possible_corrections = []
  correction = {}

  #--------------------------------------------------------
  # nh → n  | cana    | canha
  #procura 'n'
  if(re.findall('n', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('n', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_n_nh(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  #--------------------------------------------------------
  # lh → l  | cala    | calha
  # procura 'l'
  if(re.findall('l', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('l', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_l_lh(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  #--------------------------------------------------------
  # lh → li | paliaço | palhaço
  # procura 'li' na palavra
  if(re.findall('li', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('li', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_li_lh(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  if(possible_corrections):
    return possible_corrections
  else:
    return False


# Tests - Status - OK
# misspelled_word_5_1 = 'cana' #target: canha
# misspelled_word_5_2 = 'cala' #target: calha
# misspelled_word_5_3 = 'paliaço' #target: palhaço

# print(category_5(misspelled_word_5_3))