# -*- mode: python -*-

block_cipher = None


a = Analysis(['timetable_universal.py'],
             pathex=['/Volumes/Home Drive/Users/giancarlo/Git/Timetable-Parser'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('icons/left-arrow.png', 'icons/left-arrow.png', 'DATA')]
a.datas += [('icons/right-arrow.png', 'icons/right-arrow.png', 'DATA')]
a.datas += [('style.qss', 'style.qss', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='timetable_universal',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='timetable_universal.app',
             icon=None,
             bundle_identifier=None)
