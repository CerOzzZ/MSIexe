from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import time
import pyuac
def main():
    path = "\\Path\\"
    app = Application().start(r'msiexec /i ' + path)

if __name__=="__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()

#example of key sents
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

