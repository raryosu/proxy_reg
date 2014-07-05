import winreg

reg_proxy = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0,winreg.KEY_ALL_ACCESS)

print('Proxy Server')
print(winreg.QueryValueEx(reg_proxy,'ProxyServer')[0])

if(winreg.QueryValueEx(reg_proxy,'ProxyEnable')[0] == 0) :
  print('\nプロキシサーバが無効です。有効にしますか？(y/n)')
  if(str(input()) == 'y') :
    flag = 1
  else :
    flag = 0
else :
  print('プロキシサーバは有効です。無効にしますか？(y/n)')
  if(str(input()) == 'y') :
    flag = 0
  else :
    flag = 1

winreg.SetValueEx(reg_proxy, 'ProxyEnable', 0 ,winreg.REG_DWORD, flag)
