Use Python 3.6 or Higher and set it in path, Using Windows 10 x-64 Version
Open Command Prompt
mkdir myadvo
cd myadvo
python -m venv myvenv
myvenv\Scripts\activate
pip install --upgrade pip
pip install django
pip install selenium
Install GeckoDriver for Firefox https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-win64.zip version v0.16.1
Extract the geckodriver.exe and paste in myadvo\myvenv\selenium\webdriver\firefox 
django-admin.py startproject mysite .
Extract the zip file downloaded from https://github.com/masterpranav/myadvo in myadvo folder.

TUI Version:
In CMD type
cd tui 
python run.py

GUI Version:
In CMD Type
python manage.py runserver
Open 127.0.0.1:8000 in your Browser