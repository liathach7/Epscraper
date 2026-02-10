# Epscraper


Automated trawling through the government Epstein files. Uses python and selenium. Feed it a url and it will open it in the browser, then increment it

I got fed up of clicking. This makes it easier to search through files as you can simply watch and look out any pdfs of interest.

![image](images/screenshot.png)

##### Step 1
make sure you have python installed.

navigate to directory Epscraper in terminal

start a virtual environment by typing(if windows):

python -m venv venv


install dependencies:

pip install -r requirements.txt

##### Step 2
find a valid url. Take it from jmail.world e.g. https://www.justice.gov/epstein/files/DataSet%2010/EFTA01826982.pdf

go into scrape.py to line 18 and change the url

##### step 3
start the program:

run scrape.py


close the browser at any time to stop. You change the time spent on each pdf by editing scrape.py

I hope you find it useful and let me know about any issues. happy trawling
