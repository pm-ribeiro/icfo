'''
  [categoria 2]
  Semivogal - Ditongo Fonético


  Subcategoria  |   Exemplo erro  |   Palavra alvo
  ei → e        |   pexe          |   peixe
  ou → o        |   poco          |   pouco
  ᴓ → i         |   feis          |   fez
  ei            |   peira         |   pera
  ou            |   bouto         |   boto

'''

# subcategories
category_2_1 = 'Semivogal - Ditongo Fonético: ei → e'
category_2_2 = 'Semivogal - Ditongo Fonético: ou → o'
category_2_3 = 'Semivogal - Ditongo Fonético: ᴓ → i'
category_2_4 = 'Semivogal - Ditongo Fonético: ei'
category_2_5 = 'Semivogal - Ditongo Fonético: ou'

#----------------------------------------------------------------------
# Libraries and packages

#Time related
import time
import timeit
import datetime

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
# import my_module, replace "my_module" here with the module name.
from validate_target_word import *
from change_letters import *
sys.path.pop(0)

# Regex
import re

#----------------------------------------------------------------------

# category_2_1 = 'Semivogal - Ditongo Fonético: ei → e'
# Example: pexe → peixe
def changes_e_to_ei(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'e', s, e, 'ei')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # valida a correção
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_2_1,
    })
    return word_rule_dict
  else:
    return False

# category_2_2 = 'Semivogal - Ditongo Fonético: ou → o'
# Example: poco → pouco
def changes_o_to_ou(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'o', s, e, 'ou')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # valida a correção
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_2_2,
    })
    return word_rule_dict
  else:
    return False

# category_2_3 = 'Semivogal - Ditongo Fonético: ᴓ → i'
# Example: ᴓ → i feis → fez
def changes_is_to_z(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'is', s, e, 'z')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # valida a correção
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_2_3,
    })
    return word_rule_dict
  else:
    return False

# category_2_4 = 'Semivogal - Ditongo Fonético: ei'
# Example: peira → pera
def changes_ei_to_e(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'ei', s, e, 'e')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # valida a correção
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_2_4,
    })
    return word_rule_dict
  else:
    return False

# category_2_5 = 'Semivogal - Ditongo Fonético: ou'
# Example: bouto → boto
def changes_ou_to_o(misspelled_word, s, e):
  word_rule_dict = {}

  # change_letters(sample_str, original_char, s, e, target_char)
  target_word = change_letters(misspelled_word, 'ou', s, e, 'o')
  word_rule_dict = validate_target_word(misspelled_word, target_word)

  # valida a correção
  if(word_rule_dict):
    word_rule_dict.update({
      "error_category": category_2_5,
    })
    return word_rule_dict
  else:
    return False

def category_2(misspelled_word):
  misspelled_word = misspelled_word.lower()
  possible_corrections = []
  correction = {}

  # -------------------------------------------------------------------------
  # category_2_1 = 'Semivogal - Ditongo Fonético: ei → e'
  # Example: pexe → peixe
  if(re.findall('e', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('e', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_e_to_ei(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # category_2_2 = 'Semivogal - Ditongo Fonético: ou → o'
  # Example: poco → pouco
  if(re.findall('o', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('o', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_o_to_ou(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # category_2_3 = 'Semivogal - Ditongo Fonético: ᴓ → i'
  # Example: ᴓ → i feis → fez
  if(re.findall('is', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('is', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_is_to_z(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # category_2_4 = 'Semivogal - Ditongo Fonético: ei'
  # Example: peira → pera
  if(re.findall('ei', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('ei', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_ei_to_e(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  # category_2_5 = 'Semivogal - Ditongo Fonético: ou'
  # Example: bouto → boto
  if(re.findall('ou', misspelled_word)):
    match_indexes = [(m.span()) for m in re.finditer('ou', misspelled_word)]
    for indexes in match_indexes:
      s, e = indexes
      correction = changes_ou_to_o(misspelled_word, s, e)
      if(correction):
        possible_corrections.append(correction)

  if(possible_corrections):
    return possible_corrections
  else:
    return False

# --------------------------------------------------------------------------
# Tests - Status: WIP

# category_2_1 = 'Semivogal - Ditongo Fonético: ei → e'
# Example: pexe → peixe
# print(category_3('pexe'))

# category_2_2 = 'Semivogal - Ditongo Fonético: ou → o'
# Example: poco → pouco
# print(category_3('poco'))

# category_2_3 = 'Semivogal - Ditongo Fonético: ᴓ → i'
# Example: ᴓ → i feis → fez
# print(category_3('feis'))

# category_2_4 = 'Semivogal - Ditongo Fonético: ei'
# Example: peira → pera
# print(category_3('peira'))

# category_2_5 = 'Semivogal - Ditongo Fonético: ou'
# Example: bouto → boto
# print(category_3('bouto'))
