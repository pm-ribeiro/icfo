'''
  receives a word in string format
  returns a string with the C/V encoding (consonant/vowel) of the word
'''

from word_syllables import *
from word_to_cv import *

def cv_syllables(word):

  word_copy = word.lower() #copies the original and leave word in lower case

  #split into syllables
  syllables = word_syllables(word_copy) #calls method to split word into syllables
  syllables_to_cv = [] #holds the CV enconded syllables

  #converts syllables to CV encoding
  for syllable in syllables:
    syllables_to_cv.append(word_to_cv(syllable)) #add marker (underline) at the beginning and end of the syllable

  syllables_cv = "-".join(syllables_to_cv)

  return syllables_cv

examples = [
            'menino', 'boneca', 'menino', 'boneca', 'ensino', 'vai', 'me',
            'idéia', 'urina', 'museu', 'saiu', 'céu', 'transformou', 'sal',
            'preto', 'branco', 'palhaço', 'canha', 'calha', 'peixe', 'pouco',
            'fez', 'pêra', 'boto', 'falta', 'contou'
          ]

for example in examples:
  print('_____Word: %s\n__Enconde: %s' %  (example, cv_syllables(example)) )
