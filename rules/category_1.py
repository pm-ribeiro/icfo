'''
  [categoria 1]
  Vogal - Átona - Inicial/Medial/Final/Clítico
'''

# libraries and packages
# ------------------------------------------------------------
#Time related
import time
import timeit
import datetime

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

# ------------------------------------------------------------

# subcategories
category_1_1 = 'Vogal - átona - final: o -> u'
category_1_2 = 'Vogal - átona - medial: o -> u'

category_1_3 = 'Vogal - átona - inicial: u -> o'
category_1_4 = 'Vogal - átona - final: u -> o'

category_1_5 = 'Vogal - átona - inicial: e -> i'
category_1_6 = 'Vogal - átona - medial: e -> i'
category_1_7 = 'Vogal - átona - Clítico: e -> i'

category_1_8 = 'Vogal - átona - inicial: i -> e'

# ------------------------------------------------------------

#status = OK


def changes_e_i(misspelled_word, s, e):
    word_rule_dict = {}

    # change_letters(sample_str, original_char, s, e, target_char)
    target_word = change_letters(misspelled_word, 'e', s, e, 'i')
    word_rule_dict = validate_target_word(misspelled_word, target_word)

    if(word_rule_dict and misspelled_word[0] == 'e'):
        word_rule_dict.update({
            "error_category": category_1_8,
        })
        return word_rule_dict
    else:
        return False

#status = OK


def changes_u_o(misspelled_word, s, e):
    word_rule_dict = {}

    target_word = change_letters(misspelled_word, 'u', s, e, 'o')
    word_rule_dict = validate_target_word(misspelled_word, target_word)

    if(word_rule_dict and misspelled_word[-1] == 'u'):
        word_rule_dict.update({
            "error_category": category_1_1,
        })
        return word_rule_dict
    elif(word_rule_dict):
        word_rule_dict.update({
            "error_category": category_1_2,
        })
        return word_rule_dict
    else:
        return False

#status = OK


def changes_o_u(misspelled_word, s, e):
    word_rule_dict = {}

    target_word = change_letters(misspelled_word, 'o', s, e, 'u')
    word_rule_dict = validate_target_word(misspelled_word, target_word)

    if(word_rule_dict and misspelled_word[0] == 'o'):
        word_rule_dict.update({
            "error_category": category_1_3,
        })
        return word_rule_dict
    elif(word_rule_dict and misspelled_word[-1] == 'o'):
        word_rule_dict.update({
            "error_category": category_1_4,
        })
        return word_rule_dict
    else:
        return False

# Status = OK


def changes_i_e(misspelled_word, s, e):
    word_rule_dict = {}

    # change_letters(sample_str, original_char, s, e, target_char)
    target_word = change_letters(misspelled_word, 'i', s, e, 'e')
    word_rule_dict = validate_target_word(misspelled_word, target_word)

    # category_1_7 = 'Vogal - átona - Clítico: e -> i'
    # pronomes - pronoun - PRON
    # artigos - determiner DET
    # conjuncao - conjunction  CONJ
    # preposicao - adposition (?) ADP

    # pronomes oblíquos, preposições, conjunções, artigos
    # (monossílabas atonos, para a - pra)
    if(
        word_rule_dict and
        (
            word_rule_dict['POS'] == 'PRON' or
            word_rule_dict['POS'] == 'DET' or
            word_rule_dict['POS'] == 'CONJ' or
            word_rule_dict['POS'] == 'ADP'
        )
    ):
        syllables = word_rule_dict['syllabic_separation']
        syllables = syllables.split('-') #transforma em vetor de silabas
        if(len(syllables) == 1):
            word_rule_dict.update({
                "error_category": category_1_7,
            })
            return word_rule_dict

    # category_1_5 = 'Vogal - átona - inicial: e -> i'
    elif(word_rule_dict and misspelled_word[0] == 'i'):
        word_rule_dict.update({
            "error_category": category_1_5,
        })
        return word_rule_dict

    # category_1_6 = 'Vogal - átona - medial: e -> i'
    elif(word_rule_dict):
        word_rule_dict.update({
            "error_category": category_1_6,
        })
        return word_rule_dict

    # correção nao encontrada por essa regra
    else:
        return False


def category_1(misspelled_word):
    misspelled_word = misspelled_word.lower()
    possible_corrections = []
    correction = {}

    # Inicial: i → e  edeia ideia
    if(misspelled_word[0] == 'e'):
        correction = changes_e_i(misspelled_word, 0, 1)
        if(correction):
            possible_corrections.append(correction)

    # procura i na palavra
    i_found = re.findall('i', misspelled_word)
    if(i_found):
        i_indexes = [(m.span()) for m in re.finditer('i', misspelled_word)]
        for indexes in i_indexes:
            s, e = indexes
            correction = changes_i_e(misspelled_word, s, e)
            if(correction):
                possible_corrections.append(correction)

    # procura a letra 'u' na palavra
    u_found = re.findall('u', misspelled_word)
    if(u_found):
        u_indexes = [(m.span()) for m in re.finditer('u', misspelled_word)]
        for indexes in u_indexes:
            s, e = indexes
            correction = changes_u_o(misspelled_word, s, e)
            if(correction):
                possible_corrections.append(correction)

    # procura a letra 'o' na palavra
    o_found = re.findall('o', misspelled_word)
    if(o_found):
        o_found = [(m.span()) for m in re.finditer('o', misspelled_word)]
        for indexes in o_found:
            s, e = indexes
            correction = changes_o_u(misspelled_word, s, e)
            if(correction):
                possible_corrections.append(correction)

    if(possible_corrections):
        return possible_corrections
    else:
        return False

# --------------------------------------------------------
# Tests - status = OK
# misspelled_words = ['orina', 'museo', 'meninu', 'buneca', 'insino', 'minino', 'edeia', 'mi']
# for word in misspelled_words:
#     print(category_1(word))