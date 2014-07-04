import winreg

reg_proxy = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0,)

print('Proxy Server')
print(winreg.QueryValueEx(reg_proxy,'ProxyServer')[0])

if(winreg.QueryValueEx(reg_proxy,'ProxyEnable')[0] == 0) :
  print('\nProxy Server is unable. Do you want to be able?(y/n)')
  if(str(input()) == 'y') :
    flag = 1
  else :
    flag = 0
else :
  print('Proxy Server is able. Do you want to be unable?(y/n)')
  if(str(input()) == 'y') :
    flag = 0
  else :
    flag = 1

if(flag==1):
  winreg.SetValueEx(reg_proxy, 'ProxyEnable', 0 ,winreg.REG_DWORD, 1)