# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Main.py', 'Client.py', 'hostel.py', 'contract.py', 'reference.py', 'Add_Client.py', 'add_contract.py', 'add_cost.py', 'add_facility.py', 'add_hostel.py', 'add_room.py', 'cost.py', 'database.py', 'del_client.py', 'del_contract.py', 'del_cost.py', 'del_facility.py', 'del_hostel.py', 'del_room.py', 'facilities.py', 'list_client.py', 'list_contract.py', 'list_cost.py', 'list_facilities.py', 'list_hostel.py', 'list_rooms.py', 'red_client.py', 'red_client_2.py', 'red_contract.py', 'red_contract_2.py', 'red_contract_3.py', 'red_cost.py', 'red_cost_2.py', 'red_facility.py', 'red_facility_2.py', 'red_hostel.py', 'red_hostel_2.py', 'red_room.py', 'red_room_2.py', 'rooms.py'],
             pathex=['C:\\Users\\zausailovsasha\\Desktop\\Курсач\\test'],
             binaries=[],
             datas=[],
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
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
