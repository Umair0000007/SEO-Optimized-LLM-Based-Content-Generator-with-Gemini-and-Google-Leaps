# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=['.'],  # Ensure the current directory is included in the path
    binaries=[],
    datas=[],
    hiddenimports=[
        'requests',
        'beautifulsoup4',
        'dotenv',  # python-dotenv
        'fastapi',
        'streamlit',
        'google.generativeai',
        'uvicorn',
        # 'pathlib' should not be included here as it is part of the standard library
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pathlib'],  # Exclude pathlib to avoid conflicts
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
