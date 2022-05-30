from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import time
import pyuac
def main():
    path = "C:\\Users\\Cesar\\Desktop\\Python installer\\openvpn-connect-3.3.6.2752_signed.msi"
    app = Application().start(r'msiexec /i ' + path)

if __name__=="__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()


time.sleep(1)
send_keys("{ENTER}")
time.sleep(1)
send_keys("{SPACE}")
time.sleep(1)
send_keys("{ENTER}")
time.sleep(1)
send_keys("{ENTER}")
time.sleep(180)
send_keys("{ENTER}")

