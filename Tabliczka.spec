# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Tabliczka.pyw'],
             pathex=['C:\\Users\\Mozz\\Desktop\\tabliczka_nw'],
             binaries=[],
             datas=[('C:\\Users\\Mozz\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\pygame\\libmpg123.dll', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Tabliczka',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
