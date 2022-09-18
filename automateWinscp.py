from turtle import title
import pywinauto ,time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import keyboard as kb

app = Application().start(cmd_line=r"C:\Program Files (x86)\WinSCP\WinSCP.exe")
app.Login.set_focus()
win = app.TLoginDialog
#win.print_control_identifiers()
time.sleep(2)

app1 = Application().connect(title=u'Login')
win2 = app1.TLoginDialog
win2.Login.click()

time.sleep(2)

send_keys("^o")
time.sleep(2)

#"/var/tmp/csv_files"
kb.send_keys(r"/var/tmp/csv_files", with_spaces=True)
time.sleep(5)

send_keys("{ENTER}")
send_keys("{DOWN}")
send_keys("^a")
send_keys("{F5}")
time.sleep(3)

dest_path=r"C:\Users\almo9\Desktop\flaskapp\csv_files\\"
kb.send_keys(dest_path, with_spaces=True)
time.sleep(5)

send_keys("{ENTER}")
#win.print_control_identifiers()
#app.Application().log
send_keys("{ENTER}")
time.sleep(3)

send_keys("{F10}")
time.sleep(2)
send_keys("{ENTER}")
print("********** Updating csv files from the server is done **********")
