import numpy as np
import re

def open_env_input(filename):
    """ Opens a file containing packages mamba or pip must install and returns contents

    Arguments:
    filename: filepath to .txt file with whitespace-separated columns package, version
    """

    with open(filename) as f:
        text = f.read()
    return text

def clean_text(text):
    """ 
    replaces all repeated whitespace to a single space
    """
    
    return re.sub("\s{2,}", " ", text)

def create_rows(content): 
    """ creates a row (package, version) for each line of content
    """

    return np.array([line.split() for line in content.split('\n')])[:, :2]

def concat_cols(row):
    """ reformats a row as a string <package>>=<column>
    """
    
    return row[0] + ">=" + ".".join(row[1].split('.')[:2])

def format_command_mamba(row):
    """ outputs a mamba command to download a package 
    given a string of a concatenated row
    """
    return "mamba install \"" + row + "\""

def format_command_pip(row):
    """ outputs a pip command to download a package 
    given a string of a concatenated row
    """
    return "pip install \"" + row + "\""

def extract_commands(text, create_rows_func, concat_cols_func, format_command_func):
    """ outputs a string command to install all correctly-versioned packages in text

    Arguments:
    text: string formatted as "<package> <version>\\n" repeated
    create_rows_func: creates a row for each line of text
    concat_cols_func: reformats a row as a string <package>>=<column>
    format_command_func: outputs a command to download a package 
        given a string <package>>=<column>
    """
    
    rows = create_rows_func(text)
    return [format_command_func(concat_cols_func(row)) for row in rows]

def join_commands(commands):
    """ Joins all install commands into a single command

    commands: iterable of string of pip or mamba install commands
    """
    return ' && '.join(commands)

def write_install_command(command, filename):
    """ writes command to install dependencies which need to <filename> 
    """

    with open(filename, "w") as f:
        content = f.write(command)