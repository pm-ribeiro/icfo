from change_letters import *

# Regex
import re

# os and sys
import sys
import os
from os import path
import pathlib
 
current_dir = pathlib.Path(__file__).parent.absolute()

#----------------------------------------------------------------------------

def remove_dash_word(original_text, new_text, text_code):
  #regex paterns
  start_of_word_dash = re.compile(r'(^|\s)-\w+-?\w*') # OK
  end_of_word_dash = re.compile(r'(\w-)*\w+-\s(?!$)') # OK
  
  
  lines = original_text.readlines() #gets the lines of document and copy to array

  # loop through original document lines
  for i in range(0, len(lines)):

    # checks -word
    dash_word = start_of_word_dash.search(lines[i]) 
    if(dash_word):
      print('filename: ', text_code)
      fixed_word = dash_word.group().replace('-', '', 1)
      print(dash_word.group(),'->', fixed_word)
      lines[i] = lines[i].replace(dash_word.group(), fixed_word, 1)

    # checks word-
    dash_word = end_of_word_dash.search(lines[i]) 
    if(dash_word):
      print('filename: ', text_code)
      index = dash_word.group().rfind("-") #finds last ocurency
      fixed_word = change_letters(dash_word.group(), '-', index, index+1, '')
      print(dash_word.group(),'->', fixed_word)
      lines[i] = lines[i].replace(dash_word.group(), fixed_word, 1)
    

  # write lines to new document
  new_text.writelines(lines)

  # #close files
  new_text.close()
  original_text.close()

# --------------------------------------------------------------------------------
# Test with text
# text_code = '0060_100720_m_01_04_01_2002_tn_ba_4s_a.txt'
# original_text = open(all_texts + text_code , "r")
# new_text = open(normalized_folder + text_code , "w+") #create a normalized copy
# remove_dash_word(original_text, new_text, text_code)
# --------------------------------------------------------------------------------


def remove_dash_words_all_texts(source_folder, target_folder):
  # all file names in folder
  all_files = []
  for file in os.listdir(source_folder):
    if file.endswith(".txt"):
      all_files.append(file)

  print(len(all_files))
  i = 0
  for text in all_files:
    original_text = open(source_folder + text , "r") # open text
    new_text = open(target_folder + text , "w+") #create a copy
    remove_dash_word(original_text, new_text, text)
    i+=1
    # ---------------------------------------------------------
    # checking files
    # original_text = open(all_texts_folder + text , "r")
    # new_text = open(all_texts_folder_normalized + text , "r") #create a normalized copy
    # print("[" + text + "]")
    # check_texts(original_text, new_text)
  print(i)


#------------------------------------------------------------------------
grade = input('Digite a série [3 ou 4]: ')
folder_name = input('Digite o nome da pasta fonte: ')

all_texts_folder = str(current_dir) + f'/texts/all_texts_normalized/{str(grade)}_serie/{str(folder_name)}/'
normalized_folder_3_grade = str(current_dir) + f'/texts/all_texts_normalized_v2/{str(grade)}_grade/{str(folder_name)}/'

remove_dash_words_all_texts(all_texts_folder, normalized_folder_3_grade)