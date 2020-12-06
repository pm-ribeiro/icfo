'''
  [categoria 3]
  Semivogal - Ditongo Fonológico

  Subcategoria  | Exemplo erro  | Palavra alvo
  u → l         | cél           |   céu
  l → u         | sau           |   sal
  Omissão       | fata          |   falta

'''

# subcategories
category_3_1 = 'Semivogal - Ditongo Fonológico: u → l'
category_3_2 = 'Semivogal - Ditongo Fonológico: l → u'
category_3_3 = 'Semivogal - Ditongo Fonológico: Omissão'

'''
  O ditongo é considerado fonológico quando não pode ser suprimido pelos
  falantes sob pena de afetar o sentido da palavra.
  peito e leite não podem ser produzidos como peto e lete porque aquilo
  que é fonológico tem repercussão no sentido, é distintivo na língua
'''

# ---------------------------------------------------------------
# Libraries and packages

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
# ---------------------------------------------------------------

vogals = [
            'a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê',
            'i', 'í', 'o','ó', 'ô', 'u', 'ú', 'y'
          ]

# u → l cél →  céu
def changes_l_to_u(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'l', s, e, 'u')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_3_1,
    })
    return word_rule_dict
  else:
    return False


# l → u sau → sal
def changes_u_to_l(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'u', s, e, 'l')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_3_2,
    })
    return word_rule_dict
  else:
    return False

# Add 'u' or 'l'
def omission(misspelled_word):
  word_rule_dict = {}
  possible_corrections = []

  for index, c in enumerate(misspelled_word):
    if(c in vogals):
      target_word = (
                      misspelled_word[:index] +
                      misspelled_word[index:index+1] + 'l' +
                      misspelled_word[index+1:]
                    )
      word_rule_dict = validate_target_word(misspelled_word, target_word)

      if(word_rule_dict):
        word_rule_dict.update({
          "error_category": category_3_3,
        })
        possible_corrections.append(word_rule_dict)

  if(possible_corrections):
    return possible_corrections
  else:
    return False

def category_3(misspelled_word):
  misspelled_word = misspelled_word.lower()
  possible_corrections = []
  correction = {}
  omission_corrections = []

  # -------------------------------------------------------------------------
  # category_3_1 = 'Semivogal - Ditongo Fonológico: u → l'
  # example: cél → céu
  if(re.findall('l', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('l', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_l_to_u(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # -------------------------------------------------------------------------
  # category_3_2 = 'Semivogal - Ditongo Fonológico: l → u'
  # example: sau → sal
  if(re.findall('u', misspelled_word)):
      match_indexes = [(m.span()) for m in re.finditer('u', misspelled_word)]
      for indexes in match_indexes:
        s, e = indexes
        correction = changes_u_to_l(misspelled_word, s, e)
        if(correction):
          possible_corrections.append(correction)

  # -------------------------------------------------------------------------
  # category_3_3 = 'Semivogal - Ditongo Fonológico: Omissão'
  # example: fata → falta
  omission_corrections = omission(misspelled_word)
  if(omission_corrections):
    for item in omission_corrections:
      possible_corrections.append(item)

  if(possible_corrections):
    return possible_corrections
  else:
    return False

# tests
# print(category_3('fata'))