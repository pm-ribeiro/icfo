'''
  searchs a word in VOP (Vocabulário Ortográfico do Português) files
  return word if found or false if not found
'''

#-----------------------------------------------------------------------------
#Files, libs and packages needed
import csv
import os
import os.path as path, sys
from inspect import getsourcefile

current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))

#sets path to VOP files 
path_to_vop_set = current_dir + '/resource_files/vop_set.csv'
path_to_vop = current_dir + 'resource_files/vop.csv'

#-----------------------------------------------------------------------------

def search_word_in_vop(source_file, word):
  found_word = {}
  with open(source_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if(row['palavra'] == word):
        found_word.update({
          "word": row['palavra'],
          "POS": row['categoria'],
          "syllabic_separation": row['separacao']
        })
        
  if(found_word):
    return found_word
  else:
    return False


#Test - Status = OK
# print(search_word_in_vop(path_to_vop_set, 'amanhã'))