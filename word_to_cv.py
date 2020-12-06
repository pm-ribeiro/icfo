'''
  receives a word in string format
  returns a string with the C/V encoding (consonant/vowel) of the word
'''

def word_to_cv(word):
  # vowel and consonant arrays
  vogals = [
            'a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê',
            'i', 'í', 'o','ó', 'ô', 'u', 'ú', 'y'
          ]

  consonants = [
                'b', 'c', 'ç', 'd', 'f', 'g', 'h',
                'j', 'k', 'l', 'm', 'n', 'p', 'q',
                'r', 's', 't', 'v', 'w', 'x', 'z'
              ]

  word_copy = word.lower() #copies the original and leave word in lower case
  for c in word_copy: #loop through the word characters
    if(c in consonants): #if it is in consonants, changes the character for C (uppercase)
      word_copy = word_copy.replace(c, 'C', 1)
    elif(c in vogals): #if it is in vowels, changes the character for V (uppercase)
      word_copy = word_copy.replace(c, 'V', 1)
  return word_copy #returns the encoded word


#Test - Status = OK
# example = "mês"
# print('_____Word: %s\n__Enconde: %s' %  (example, word_to_cv(example)) )