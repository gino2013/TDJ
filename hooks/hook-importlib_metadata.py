from PyInstaller.utils.hooks import copy_metadata, collect_submodules

# Collect metadata for importlib_metadata
datas = copy_metadata('importlib_metadata')

# Collect all submodules of importlib_metadata
hiddenimports = collect_submodules('importlib_metadata')
