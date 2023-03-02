import numpy as np
import re
from env_install_tools import *

def main():
    """takes dependencies installed by mamba and outputs a command to download all
    """

    text = open_env_input("./env_install_data/mamba_install_inp.txt")
    cleaned_text = clean_text(text)
    commands = extract_commands(cleaned_text, create_rows, concat_cols, \
        format_command_mamba)
    write_install_command(join_commands(commands), "./env_install_data/mamba_install_outp.txt")
    
main()
