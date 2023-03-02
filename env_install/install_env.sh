#!/bin/bash
python3 create_mamba_cmd.py
python3 create_pip_cmd.py
mamba_cmd=`cat env_install_data/mamba_install_outp.txt`
pip_cmd=`cat env_install_data/pip_install_outp.txt`
eval $mamba_cmd
eval $pip_cmd