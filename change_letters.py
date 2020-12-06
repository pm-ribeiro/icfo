'''
  receives a word in string format, the letters to be exchanged 
  and the letter's index, returns the word with the letters exchanged
  parameters: original word, original char, start index, end index, char to change
'''

def change_letters(sample_str, original_char, s, e, target_char):
  splited_str = sample_str[:s], sample_str[s:e], sample_str[e:]
  splited_str_copy = list(splited_str)
  
  for index, c in enumerate(splited_str):
    if (c == original_char):
      splited_str_copy[index] = target_char
      
  sample_str_correct = ''.join(splited_str_copy)
  return sample_str_correct


# Tests - Status = OK
# print(change_letters("diredor", 'd' , 4, 5, 't')) #target diretor
# print(change_letters("brato", 'b', 0, 1, 'p')) #target prato