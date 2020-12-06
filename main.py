# -----------------------------------------------------------------------------
# Files, libs and packages needed

# os and sys
import sys
import os
from os import path
import pathlib

from write_to_csv import *

# -----------------------------------------------------------------------------

def process_texts(grade, source_folder_name, error_category):
    n_error_category = error_category
    current_dir = pathlib.Path(__file__).parent.absolute()
    # default paths to texts folders
    normalized_folder = str(current_dir) + '/texts/all_texts_normalized_v2'
    # processed_folder = path.relpath('texts/all_texts_processed')
    processed_folder = str(current_dir) + '/texts/all_texts_processed'

    # builds source file path
    path_to_source_folder = f"{str(normalized_folder)}/{str(grade)}_grade/{source_folder_name}/"

    # builds target file
    path_to_target_file = f"{str(processed_folder)}/{str(grade)}_grade/error_category_{str(error_category)}/"
    target_file_name = f"{str(grade)}_grade_error_category_{str(error_category)}_{source_folder_name}.csv"

    # creates target file
    target_file = open(path_to_target_file + target_file_name, "w+")

    # time results file
    target_file_results = f"{str(grade)}_grade_error_category_{str(error_category)}_{source_folder_name}_results.csv"
    #creates results file
    results_file = open(path_to_target_file + target_file_results, "w+")

    write_to_csv(
        path_to_source_folder,
        target_file,
        n_error_category,
        grade,
        results_file
    )

# -----------------------------------------------------------------
# TEST - Status: OK
# process_texts(0, 'testes', 1)

# -----------------------------------------------------------------
# User input
grade = int(input('Digite a série [3 ou 4]: '))
error_category = input('Digite a categoria de erro (x): ')
source_folder = input('Digite o nome da pasta fonte: ')

# grade, 'source_folder_name', error_category
process_texts(grade, str(source_folder), error_category)
