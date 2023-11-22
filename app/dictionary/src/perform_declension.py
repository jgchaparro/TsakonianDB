import pandas as pd
import numpy as np
import re

def perform_declension(word: str, 
                       paradigm: str,
                       paradigm_master: pd.DataFrame) -> dict:
    """
    This function performs the declension of a given word
    based on the paradigm taxonomy described in the PDF
    Συμπυκνωμένη γραμματική της Τσακώνικης γλώσσας σε πίνακες
    """

    if re.match(r'^[ΑΘΥ][1-9]$', paradigm) is None:
        return {}

    ### Article ###
    article_dict_master = {
        'Α': 
            {'nom_sing' : 'ο',
             'nom_plur' : 'οι',
             'gen_sing' : 'του',
             'acc_sing' : 'το',
             'acc_plur' : 'τους'
            },
        'Θ': {
            'nom_sing' : 'α',
            'nom_plur' : 'οι',
            'gen_sing' : 'τα',
            'acc_sing' : 'τα',
            'acc_plur' : 'τουρ'
        },
        'Υ': {
            'nom_sing' : 'το',
            'nom_plur' : 'τα',
            'gen_sing' : 'του',
            'acc_sing' : 'το',
            'acc_plur' : 'τα'
        } 
    }
    article_dict = article_dict_master[paradigm[0]]

    # Add letters when the word starts with a vowel
    vowels = 'αάεέηήιίοόυύωώ'
    if word[0] in vowels:
        if paradigm[0] == 'Α':
            article_dict['acc_sing'] = 'τον'
            article_dict['acc_plur'] = 'τουρ'
        elif paradigm[0] == 'Θ':
            article_dict['gen_sing'] = 'ταρ'
            article_dict['acc_sing'] = 'ταν'

    ### Noun ###
    # Get the plural and genitive marks of the word
    paradigm_row = paradigm_master.loc[paradigm]
    genitive_mark = paradigm_row['gen_sing']
    plural_mark = paradigm_row['plural']

    # Get the word stem
    if word[-2:] in ['ου', 'ού', 'μα', 'μο']:
        stem = word[:-2]
    else:
        stem = word[:-1]

    # Compute plural if it is recorded
    plural = None
    if plural_mark is not np.nan:
        plural = stem + plural_mark
        
        # Handle special cases
        #  1) When the root ends in κ, λ or ν and the plural mark is ε or οι
        if plural_mark in ['ε', 'οι']:
            if stem[-1] == 'κ':
                plural = stem[:-1] + 'τσ̇' + plural_mark
            elif stem[-1] == 'λ':
                plural = stem[:-1] + 'λ̣' + plural_mark
            elif stem[-1] == 'ν':
                plural = stem[:-1] + 'ν̇' + plural_mark

    # Compute genitive if it is recorded
    gen_sing = word
    if genitive_mark is not np.nan:
        gen_sing = stem + genitive_mark 

    ### Handle irregular nouns ###
    if '0' in paradigm:
        try:
            irregular_row = paradigm_master.loc[word]
            plural = irregular_row['plural']
            gen_sing = irregular_row['gen_sing'] if irregular_row['gen_sing'] is not np.nan else word
        except KeyError:
            plural = None

    ### Build final dictionary ###
    final_dict = {
        'nom_sing' : article_dict['nom_sing'] + ' ' + word
    }

    # Add plural and genitive if they exist
    if plural is not None:
        final_dict['nom_plur'] = article_dict['nom_plur'] + ' ' + plural
        final_dict['gen_sing'] = article_dict['gen_sing'] + ' ' + gen_sing
        final_dict['acc_sing'] = article_dict['acc_sing'] + ' ' + word
        final_dict['acc_plur'] = article_dict['acc_plur'] + ' ' + plural

    return final_dict    