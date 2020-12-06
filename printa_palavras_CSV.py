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

# -----------------------------------------------------------------------------

'''
    percorre todas as palavras dos textos e conta
'''
def write_to_csv(all_texts_folder_source, target_file, grade):
    begin_time = datetime.datetime.now()

    # -------------------------------------------------------

    # get all file names in folder that end with .txt
    all_files = []
    for file in os.listdir(all_texts_folder_source):
        if file.endswith(".txt"):
            all_files.append(file)

    # display the number of files inside the source folder
    print(len(all_files), 'Arquivos na pasta')

    # variaveis para contagem
    files_count = 0
    misspelled_word_count = 0
    words_count = 0

    with target_file:
        # headers
        fnames = [
            'Palavras',
            'C/I',
        ]
        writer = csv.DictWriter(target_file, fieldnames=fnames)
        writer.writeheader()  # write header
        for filename in all_files:
            files_count += 1
            print(files_count, filename)
            # abre o arquivo para leitura
            source_file = open(all_texts_folder_source + filename, "r")
            text_code = filename.strip('.txt')  # pega o codigo do texto
            for line in source_file:  # percorre as linhas do arquivo de texto
                # deixa a linha lowercase e remove espaços brancos do começo e final da linha
                doc_line = nlp_spacy(line.lower().strip())

                print('processando tokens...')
                for token in doc_line:  # percorre os tokens da linha
                    if(
                        token.text
                        not in (list(punctuation))
                        and not token.is_punct
                    ):
                        print('TOKEM:', token)
                        # se não for pontuacao conta como token
                        words_count += 1  # contagem de palavras nos textos
                        # salva em um arquivo dedicado

                        # salva as infomações de tempo de execução em um arquivo CSV
                        writer.writerow({
                            'Palavras': token.text,
                            'C/I': '',
                        })
                        # encerra a execução
        source_file.close()

    end_time = datetime.datetime.now() - begin_time
    print('Total de arquivos processados: ', files_count)
    print('Tempo de execução:', end_time)

    target_file.close()


def main(grade):
    current_dir = pathlib.Path(__file__).parent.absolute()

    # default paths to texts folders
    normalized_folder = str(current_dir) + '/texts/contagem_final_textos'

    # processed_folder = path.relpath('texts/all_texts_processed')
    processed_folder = str(current_dir) + '/texts/contagem_final_textos/resultados'

    # =====================================================================================

    # builds source file path
    source_folder = f"{str(normalized_folder)}/{str(grade)}_grade/"

    # builds path to target file
    path_to_target_file = f"{str(processed_folder)}/"

    # builds target file
    target_file_name = f"{str(grade)}_grade_words.csv"

    # creates target file
    target_file = open(path_to_target_file + target_file_name, "w+")

    write_to_csv(
        source_folder,
        target_file,
        grade,
    )

# -----------------------------------------------------------------
# TEST - Status: OK
# process_texts(0, 'testes', 1)
grade = int(input('Digite a série [3 ou 4]: '))
main(grade)
