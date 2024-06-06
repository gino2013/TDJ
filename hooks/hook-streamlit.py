from PyInstaller.utils.hooks import copy_metadata, collect_submodules

# Collect metadata for streamlit
datas = copy_metadata('streamlit')

# Collect all submodules of streamlit
hiddenimports = collect_submodules('streamlit')
