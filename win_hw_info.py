import os
import platform
import winreg as reg
# 윈도우 각 플랫폼에 맞게 레지스트리 구조가 변경 되는지 알아보고 그에 맞게 정보를 가져오는 코드를 짜봅시다.

key = reg.HKEY_CURRENT_USER
key_value = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"

open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)

value, type = reg.QueryValueEx(open,"User Agent")
print(value,"Type:",type)

try:
    value, type = reg.QueryValueEx(open,"AutoConfigURL")
    print("AutoConfigURL",value,"Type:",type)
except FileNotFoundError:
    print("AutoConfigURL not found")

try:
    value, type = reg.QueryValueEx(open,"ProxyServer")
    print("ProxyServer",value,"Type:",type)
except FileNotFoundError:
    print("ProxyServer not found")

# now close the opened key 
reg.CloseKey(open)