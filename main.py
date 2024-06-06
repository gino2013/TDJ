import subprocess
import streamlit as st

# 确保PyInstaller检测到这些依赖项
import streamlit
import importlib_metadata

# 使用subprocess模块运行streamlit run命令
streamlit_path = "/Users/cfh00892977/anaconda3/envs/py39/bin/streamlit"
subprocess.run([streamlit_path, "run", "interface_adapters/streamlit_interface.py"])
