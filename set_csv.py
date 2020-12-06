# Files, libs and packages needed
import pandas as pd

# Time related
import utils
import time
import timeit
import datetime

# String
from string import punctuation

# Spacy
import spacy

# CSV related
import csv

# Dicio related
from dicio import Dicio  # import the dictionary
dicio = Dicio()  # Create a Dicio object

# spaCy related
nlp_spacy = spacy.load("pt_core_news_sm")
pt_stopwords = nlp_spacy.Defaults.stop_words

# NLTK related
import nltk
from nltk.corpus import stopwords

# os and sys
import sys
import os
from os import path
import pathlib

current_dir = pathlib.Path(__file__).parent.absolute()

# sets path to VOP files
path_to_vop_set = str(current_dir) + '/resource_files/vop_set.csv'
path_to_vop = str(current_dir) + '/resource_files/vop.csv'

# -----------------------------------------------------------------------------

'''
  percorre todas as palavras dos textos
  idenfica como C/I salva no CSV
'''

# @param source_folder, target_file.csv, grade
def write_to_csv(all_texts_folder_source, target_file, grade):
    begin_time = datetime.datetime.now()
    print('all_texts_folder_source', all_texts_folder_source)

    # -------------------------------------------------------

    # pega todos os arquivos da pasta terminados em .csv
    all_files = []
    for file in os.listdir(all_texts_folder_source):
        if file.endswith(".csv"):
            all_files.append(file)

    # Printa o número de arquivos na pasta
    print(len(all_files), 'Arquivos na pasta')

    with target_file:
        # define o  para o arquivo destino
        fnames = [
                    'text_code', 'line_number', 'word_location_line',
                    'misspelled_word', 'target_word', 'error_category',
                    'POS', 'syllabic_separation', 'cvs_encoding',  'vowel_meeting'
                ]
        writer = csv.DictWriter(target_file, fieldnames=fnames)
        writer.writeheader()  # escreve o cabeçalho

        files_count = 0

        # percorre todos os arquivos dap pasta
        for filename in all_files:
          files_count += 1
          print('Nome do arquivo: ',filename)
          source_file = open(all_texts_folder_source + filename, "r")

          # define o dataframe
          df = pd.read_csv(all_texts_folder_source + filename)
          uniques = df.drop_duplicates(subset = ["misspelled_word", "target_word", "error_category"]) #remove todas as linhas duplicadas

          # percorre todos os itens contidos em unique e
          # escreve o resultado no arquivo de saida
          # observar a chave/valor utilizada nos arquivos fonte/destino
          for index, row in uniques.iterrows():
            writer.writerow({
                  'text_code': row['text_code'],
                  'line_number': row['line_number'],
                  'word_location_line': row['word_location_line'],
                  'misspelled_word': row['misspelled_word'],
                  'target_word': row['target_word'],
                  'error_category': row['error_category'],
                  'POS': row['POS'],
                  'syllabic_separation': row['syllabic_separation'],
                  'cvs_encoding': row['cvs_encoding'],
                  'vowel_meeting': row['vowel_meeting']
            })

          # fecha o arquivo de entrada
          source_file.close()

    target_file.close()

    print('Total de arquivos processados: ', files_count)

# @param grade, 'source_folder_name'
def main(grade, source_folder_name):
    current_dir = pathlib.Path(__file__).parent.absolute()

    # pasta origem
    source_folder = f"{str(current_dir)}/texts/all_texts_processed/{str(grade)}_grade/{source_folder_name}/set/"

    # pasta destino
    target_folder = f"{str(current_dir)}/texts/all_texts_processed/{str(grade)}_grade/{source_folder_name}/set_2/"

    # arquivo destino
    target_file_name = f"set_error_category_x_{str(grade)}_grade.csv"

    # cria o arquio de destino
    target_file = open(target_folder + target_file_name, "w+")

    # chama o método que percorre os arquivos csv e escreve no arquivo destino
    write_to_csv(
        source_folder,
        target_file,
        grade
    )

#-----------------------------------------------------------------
main(3, 'error_category_x') # executa para a 3ª série
# main(4, 'error_category_x') # executa para a 4ª série
