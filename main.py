import subprocess
import os
import streamlit as st
import importlib_metadata

# 获取streamlit命令的绝对路径
streamlit_path = "/Users/cfh00892977/anaconda3/envs/py39/bin/streamlit"

# # 获取streamlit_interface.py的绝对路径
# script_path = os.path.abspath('/Users/cfh00892977/FM/TDJ/interface_adapters/streamlit_interface.py')

# 使用subprocess模块运行streamlit run命令
subprocess.run([streamlit_path, "run", '/Users/cfh00892977/FM/TDJ/interface_adapters/streamlit_interface.py'])
