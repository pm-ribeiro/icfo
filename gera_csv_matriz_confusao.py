# Files, libs and packages needed

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
def write_to_csv(all_texts_folder_source, target_file, grade, results_file):
    begin_time = datetime.datetime.now()

    # -------------------------------------------------------

    # get all file names in folder that end with .txt
    all_files = []
    for file in os.listdir(all_texts_folder_source):
        if file.endswith(".txt"):
            all_files.append(file)

    # display the number of files inside the source folder
    print(len(all_files), 'Arquivos na pasta')

    with target_file:
        # headers
        fnames = [
                    'text_code', 'line_number', 'word_location_line',
                    'word', 'correto/incorreto (C/I)'
                ]
        writer = csv.DictWriter(target_file, fieldnames=fnames)
        writer.writeheader()  # write header

        # percorre todos os textos da pasta
        files_count = 0
        misspelled_word_count = 0
        words_count = 0
        line_number = 0
        word_location_line = 0

        for filename in all_files:
            print(filename)

            line_number = 0
            files_count += 1
            # abre o arquivo para leitura
            source_file = open(all_texts_folder_source + filename, "r")
            text_code = filename.strip('.txt')  # pega o codigo do texto
            for line in source_file:  # percorre as linhas do arquivo de texto
                line_number += 1 # conta as linhas do arquivo
                # deixa a linha lowercase e remove espaços brancos do começo e final da linha
                doc_line = nlp_spacy(line.lower().strip())

                word_location_line = 0
                for token in doc_line:  # percorre os tokens da linha

                    word_location_line += 1 # conta as palavras da linha atual
                    words_count += 1  # contagem de palavras nos textos

                    # se o token nao for uma pessoa
                    # pontuação, stopword, data ou hora
                    if(
                        token.text
                        not in (set(stopwords.words('portuguese') + list(punctuation)))
                        and not token.ent_type_
                        and not token.is_punct
                        and not token.like_num
                        and not token.is_stop
                        and not utils.is_date(token.text)
                        and not utils.is_time(token.text)
                        and not token.text.isdigit()
                    ):
                        if (dicio.search(token.text) == None):
                          misspelled_word_count += 1  # contagem de palavras erradas nos textos
                          print('Palavra incorreta:', token.text)

                          writer.writerow({
                              'text_code': text_code,
                              'line_number': line_number,
                              'word_location_line': word_location_line,
                              'word': token.text,
                              'correto/incorreto (C/I)': 'I'
                          })
                        else:
                          print('Palavra correta:', token.text)
                          writer.writerow({
                              'text_code': text_code,
                              'line_number': line_number,
                              'word_location_line': word_location_line,
                              'word': token.text,
                              'correto/incorreto (C/I)': 'C'
                          })
        source_file.close()
    target_file.close()

    end_time = datetime.datetime.now() - begin_time
    print('Total de arquivos processados: ', files_count)
    print('Tempo de execução:', end_time)

    # salva as infomações de tempo de execução em um arquivo CSV
    with results_file:
        # headers
        fnames = [
            'Folder name',
            'Grade',
            'Number of files',
            'Number of words',
            'Number of misspelled words',
            'Runtime'
        ]
        writer = csv.DictWriter(results_file, fieldnames=fnames)
        writer.writeheader()  # write header

        writer.writerow({
            'Folder name': all_texts_folder_source,
            'Grade': grade,
            'Number of files': files_count,
            'Number of words': words_count,
            'Number of misspelled words': misspelled_word_count,
            'Runtime': end_time
        })
    # encerra a execução

    results_file.close()


def main(grade, source_folder_name):
    current_dir = pathlib.Path(__file__).parent.absolute()
    # default paths to texts folders
    normalized_folder = str(current_dir) + '/texts/all_texts_normalized_v2'
    # processed_folder = path.relpath('texts/all_texts_processed')
    processed_folder = str(current_dir) + '/texts/all_texts_processed'

    # builds source file path
    path_to_source_folder = f"{str(normalized_folder)}/{str(grade)}_grade/{source_folder_name}/"

    # builds target file
    path_to_target_file = f"{str(processed_folder)}/matriz_confusao/"
    target_file_name = f"{str(grade)}_grade_matriz_confusao_{source_folder_name}.csv"

    # creates target file
    target_file = open(path_to_target_file + target_file_name, "w+")

    # time results file
    target_file_results = f"{str(grade)}_matriz_confusao_{source_folder_name}_results.csv"
    #creates target file
    results_file = open(path_to_target_file + target_file_results, "w+")

    write_to_csv(
        path_to_source_folder,
        target_file,
        grade,
        results_file
    )

# -----------------------------------------------------------------
# TEST - Status: OK
# process_texts(0, 'testes', 1)

# -----------------------------------------------------------------
# User input
grade = int(input('Digite a série [3 ou 4]: '))
source_folder = input('Digite o nome da pasta fonte: ')

# @param grade, 'source_folder_name'
main(grade, str(source_folder))
