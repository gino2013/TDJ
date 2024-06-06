from PyInstaller.utils.hooks import copy_metadata, collect_submodules

datas = copy_metadata('encodings')
hiddenimports = collect_submodules('encodings')
