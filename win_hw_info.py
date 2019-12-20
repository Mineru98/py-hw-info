import platform
import winreg as reg

if platform.system() == "Windows":
    key = reg.HKEY_LOCAL_MACHINE
    # 윈도우 각 플랫폼에 맞게 레지스트리 구조가 변경 되는지 알아보고 그에 맞게 정보를 가져오는 코드를 짜봅시다.
    if platform.release() == "10":
        # CPU Model Name Check
        key_value = "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0"
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
        value = reg.QueryValueEx(open,"ProcessorNameString")
        print("CPU Name:",value)
        
        # Mother Board Model Name Check
        key_value = "HARDWARE\\DESCRIPTION\\System\\BIOS"
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
        value = reg.QueryValueEx(open,"BaseBoardProduct")
        print("MainBaord Name:",value)

        # Drive Model Name Check
        key_value = "SYSTEM\\CurrentControlSet\\Enum\\SCSI\\[?]\\[?]"
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
        value = reg.QueryValueEx(open,"FriendlyName")
        print("Drive Name:",value)

        reg.CloseKey(open)