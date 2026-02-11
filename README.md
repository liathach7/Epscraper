# Epscraper


I have been clicking through the €p$tein files to look for pdfs with base64 text which can be decoded. Such pdfs have large number of pages so I am looking out for that.

I developed this to automate that so I can look at the results of a search in a master image later. This may help you as well!

#### Step 1
make sure you have python installed.

navigate to directory Epscraper in terminal

start a virtual environment by typing(if windows):

python -m venv venv


install dependencies:

pip install -r requirements.txt

#### Step 2
find a valid url. Take it from jmail.world e.g. https://www.justice.gov/epstein/files/DataSet%2010/EFTA01826982.pdf

go into screen.py to line 24 and change the url

#### step 3
start the program:

run screen.py

this starts the automation.
![image]('images/screenshot.png')

You can kick back and wait as it trawls through files by incrementing the url. I've set it to load a max of 500 pages and to stop incrementing after loading 10 pages without a pdf, and going to back to original url and decrementing until 10 page not founds. You can change these settings if you want longer

#### step 4 - read the results
go into images and click on the file named after the url you input plus filled
![image]('images/screenshot2.png')

Look for a number that's higher than the others
![image]('images/screenshot3.png')
here is a 6 that could be promising. count its position. there are 20 images in each row, so count down by 20, this one is position 182


open the txt file with the same url and find the url matched to that number
![image]('images/screenshot4.png')

search the url to check if there are any base64 dumps
![image]('images/screenshot5.png')

in this case there aren't any, but the next one may be!

happy trawling!





