# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:/1GIT/pydetect-API-test/run.py'],
    pathex=[],
    binaries=[],
    datas=[('F:/1GIT/pydetect-API-test/detect', 'detect/'), ('F:/1GIT/pydetect-API-test/ui', 'ui/'), ('F:/1GIT/pydetect-API-test/pretrained_models', 'pretrained_models/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
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
    name='run',
)
