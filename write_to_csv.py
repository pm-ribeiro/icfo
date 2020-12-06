# -----------------------------------------------------------------------------
# * Files, libs and packages needed

# Time related
import utils
from rules.category_6 import *
from rules.category_5 import *
from rules.category_4 import *
from rules.category_3 import *
from rules.category_2 import *
from rules.category_1 import *

from search_word_in_vop import *

from string import punctuation

import spacy
import time
import timeit
import datetime

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
import pathlib
from os import path
import os
import sys

current_dir = pathlib.Path(__file__).parent.absolute()

# sets path to VOP files
path_to_vop_set = str(current_dir) + '/resource_files/vop_set.csv'
path_to_vop = str(current_dir) + '/resource_files/vop.csv'


# -----------------------------------------------------------------------------

# percorre a cache a procura de palavras previamente corrigidas
def search_in_cache(misspelled_word, cache):
    possible_corrections = []

    for word in cache:
        if (word["misspelled_word"] == misspelled_word):
            possible_corrections.append(word)

    return possible_corrections

# adiciona palavras na cache
def add_to_cache(word_dict, cache):
    found = False

    for item in cache:
        if (
            item['misspelled_word'] != word_dict['misspelled_word'] and
            item['target_word'] != word_dict['target_word']
        ):
            found = True

    if(not found):
        cache.append(word_dict)

# escreve nos arquivos csv
def write_to_csv(all_texts_folder_source, target_file, error_category, grade, results_file):
    begin_time = datetime.datetime.now()

    categories = [
        category_1,
        category_2,
        category_3,
        category_4,
        category_5,
        category_6
    ]

    # -------------------------------------------------------
    # inicialização de variaveis
    cache = []
    possible_corrections = []
    word_dict = {}
    words_cached = []

    # pega todos os nomes de arquivos que terminanm em .txt
    all_files = []
    for file in os.listdir(all_texts_folder_source):
        if file.endswith(".txt"):
            all_files.append(file)

    # mostra o número de arquivos dentro da pasta fonte
    print(len(all_files), 'Arquivos na pasta')

    with target_file:
        # cabeçalho do arquivo .csv
        fnames = [
                    'text_code', 'line_number', 'word_location_line',
                    'misspelled_word', 'target_word', 'error_category',
                    'POS', 'syllabic_separation', 'cvs_encoding',  'vowel_meeting'
                ]
        writer = csv.DictWriter(target_file, fieldnames=fnames)
        writer.writeheader()  # escreve cabeçalho

        # variaveis de contagem
        files_count = 0
        misspelled_word_count = 0
        words_count = 0
        line_number = 0
        word_location_line = 0

        # percorre todos os textos da pasta
        for filename in all_files:
            print(filename)

            line_number = 0
            files_count += 1

            # abre o arquivo para leitura
            source_file = open(all_texts_folder_source + filename, "r")
            text_code = filename.strip('.txt')  # pega o codigo do texto

            # percorre as linhas do arquivo de texto
            for line in source_file:
                line_number += 1 # conta as linhas do arquivo

                # deixa a linha caixa baixa e remove espaços brancos do começo e final da linha
                doc_line = nlp_spacy(line.lower().strip())

                word_location_line = 0

                # percorre os tokens da linha
                for token in doc_line:
                    word_location_line += 1 # conta as palavras da linha atual
                    words_count += 1  # contagem de palavras nos textos

                    # se o token nao for NER
                    # pontuação, stopword, digito, data ou hora
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
                        print('token',token.text)
                        if(search_word_in_vop(path_to_vop_set, token.text) == False):
                            # se não encontrar no dicionario
                            if (dicio.search(token.text) == None):
                                print('Palavra incorreta:', token.text)
                                misspelled_word_count += 1  # contagem de palavras erradas nos textos
                                # procura na cache, se encontrar salva no array
                                # percorre o array e escrevre no CSV
                                words_cached = search_in_cache(token.text, cache)

                                if(words_cached):
                                    print('Palavra encontrada na cache \n')
                                    for item in words_cached:
                                        writer.writerow({
                                            'text_code': text_code,
                                            'line_number': line_number,
                                            'word_location_line': word_location_line,
                                            'misspelled_word': item['misspelled_word'],
                                            'target_word': item['target_word'],
                                            'error_category': item['error_category'],
                                            'POS': item['POS'],
                                            'syllabic_separation': item['syllabic_separation'],
                                            'cvs_encoding': item['cvs_encoding'],
                                            'vowel_meeting': item['vowel_meeting']
                                        })

                                # se nao encontrar na cache tenta corrigir pelas categorias
                                else:
                                    print('Não encontrada na cache - Corrigir pelas categorias \n')
                                    for index, category in enumerate(categories):
                                        print('Categoria: ', index + 1)

                                        possible_corrections = category(token.text)
                                        if(possible_corrections):
                                            # percorre as possiveis correções e escreve no arquivo csv de resultados
                                            for correction in possible_corrections:

                                                # adiciona a correcao na cache
                                                add_to_cache(correction, cache)

                                                # escreve a correcao no documento de resultados
                                                writer.writerow({
                                                    'text_code': text_code,
                                                    'line_number': line_number,
                                                    'word_location_line': word_location_line,
                                                    'misspelled_word': correction['misspelled_word'],
                                                    'target_word': correction['target_word'],
                                                    'error_category': correction['error_category'],
                                                    'POS': correction['POS'],
                                                    'syllabic_separation': correction['syllabic_separation'],
                                                    'cvs_encoding': correction['cvs_encoding'],
                                                    'vowel_meeting': correction['vowel_meeting']
                                                })
                                        else:
                                            print("-> Correção não encontrada para:", token.text)
        source_file.close()
    target_file.close()

    end_time = datetime.datetime.now() - begin_time
    print('Total de arquivos processados: ', files_count)
    print('Tempo de execução:', end_time)

    # salva infomações sobre os resultados em um arquivo dedicado
    with results_file:
        fnames = [
            'Folder name',
            'Grade',
            'Error category',
            'Number of files',
            'Number of words',
            'Number of misspelled words',
            'Runtime'
        ]
        writer = csv.DictWriter(results_file, fieldnames=fnames)
        writer.writeheader()

        writer.writerow({
            'Folder name': all_texts_folder_source,
            'Grade': grade,
            'Error category': error_category,
            'Number of files': files_count,
            'Number of words': words_count,
            'Number of misspelled words': misspelled_word_count,
            'Runtime': end_time
        })

    # encerra a execução
    results_file.close()
