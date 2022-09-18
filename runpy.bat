@echo off

cd C:\Users\almo9\Desktop\flaskapp
rmdir /s csv_files
python3 automateWinscp.py
python3 attendance.py C:\Users\almo9\Desktop\flaskapp\csv_files
python3 runAttendance.py
python3 hello.py
del attendance.csv

