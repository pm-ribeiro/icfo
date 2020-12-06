'''

  [categoria 4]
  Semivogal - Ditongo morfológico

  Subcategorias   |   Exemplo erro    |   Palavra alvo
  ou → o          |   conto           |   contou
  u → l (verbo)   |   tranformol      |   transformou
  u → o (verbo)   |   saio            |   saiu
  e → i (verbo)   |   vae             |   vai

'''

# subcategories
category_4_1 = 'Semivogal - Ditongo morfológico: ou → o'
category_4_2 = 'Semivogal - Ditongo morfológico: u → l'
category_4_3 = 'Semivogal - Ditongo morfológico: u → o'
category_4_4 = 'Semivogal - Ditongo morfológico: e → i'

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
# category_4_1 = 'Semivogal - Ditongo morfológico: ou → o'
# Example: conto -> contou
def changes_o_to_ou(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'o', s, e, 'ou')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(
    word_rule_dict and
    word_rule_dict['vowel_meeting'] == 'ditongo' and
    (word_rule_dict['POS'] == 'VERB' or word_rule_dict['POS'] == 'AUX')
  ):
    word_rule_dict.update({
      "error_category": category_4_1,
    })
    return word_rule_dict
  else:
    return False

# ---------------------------------------------------------------
# category_4_2 = 'Semivogal - Ditongo morfológico: u → l'
# Example: tranformol -> transformou
def changes_l_to_u(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'l', s, e, 'u')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(
    word_rule_dict and
    word_rule_dict['vowel_meeting'] == 'ditongo' and
    (word_rule_dict['POS'] == 'VERB' or word_rule_dict['POS'] == 'AUX')
  ):
    word_rule_dict.update({
      "error_category": category_4_2,
    })
    return word_rule_dict
  else:
    return False

# ---------------------------------------------------------------

# category_4_3 = 'Semivogal - Ditongo morfológico: u → o'
# Example: saio -> saiu
def changes_o_to_u(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'o', s, e, 'u')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(
    word_rule_dict and
    word_rule_dict['vowel_meeting'] == 'ditongo' and
    (word_rule_dict['POS'] == 'VERB' or word_rule_dict['POS'] == 'AUX')
  ):
    word_rule_dict.update({
      "error_category": category_4_3,
    })
    return word_rule_dict
  else:
    return False

# ---------------------------------------------------------------
# category_4_4 = 'Semivogal - Ditongo morfológico: e → i'
# Example: vae -> vai
def changes_e_to_i(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'e', s, e, 'i')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # validates the correction
  if(
    word_rule_dict and
    word_rule_dict['vowel_meeting'] == 'ditongo' and
    (word_rule_dict['POS'] == 'VERB' or word_rule_dict['POS'] == 'AUX')
  ):
    word_rule_dict.update({
      "error_category": category_4_4,
    })
    return word_rule_dict
  else:
    return False

# ---------------------------------------------------------------
def category_4(misspelled_word):
  misspelled_word = misspelled_word.lower()
  possible_corrections = []
  correction = {}

  #--------------------------------------------------------
  # ou → o : conto -> contou
  # procura 'o'
  if(re.findall('o', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('o', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_o_to_ou(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # u → l (verbo): tranformol -> transformou
  # procura 'l'
  if(re.findall('l', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('l', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_l_to_u(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # u → o (verbo): saio -> saiu
  # procura 'o' troca por 'u'
  if(re.findall('o', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('o', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_o_to_u(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # e → i (verbo): vae -> vai
  # procura 'e' troca por 'i'
  if(re.findall('e', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('e', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_e_to_i(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  if(possible_corrections):
    return possible_corrections
  else:
    return False

# -----------------------------------------------------------------------------
# Tests - Status: OK

# print('[ category_4_1 Semivogal - Ditongo morfológico: ou → o ]')
# print(category_4('conto')) # ou → o : conto -> contou

# print('[ category_4_2 Semivogal - Ditongo morfológico: u → l ]')
# print(category_4('transformol')) # transformol - > transformou

# print('[category_4_3 Semivogal - Ditongo morfológico: u → o ]')
# print(category_4('saio')) # saio -> saiu

# print('[ category_4_4 Semivogal - Ditongo morfológico: e → i ]')
# print(category_4('vae')) # vae -> vai
