from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import os
import math




chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument("window-size=1280,720")

driver = webdriver.Chrome()
url='https://www.justice.gov/epstein/files/DataSet%2011/EFTA02583925.pdf'

def placer(pdfs):
    x = 5 + (pdfs * 35)
    y = 5
    if x > 700:
        row = math.floor(x/700)
        y = 5 + (row * 55)
        x = 5 + (pdfs * 35) - (row * 700)
    return (x,y)

def scrape(url):
    #time.sleep(3)
    counter = ''
    orig_url = ''
    for l in url:
        orig_url += l
    adding = '+'
    pdfs = 0

    # max number of page loads before stopping. can be changed from 500
    for i in range(500):
        driver.get(url)

        # gets past robot button
        try:

            # somehow stops from clicking on search button
            page_source = driver.page_source
            with open('{url}.html', 'w') as f:
                f.write(page_source)
            
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'usa-button')]"))).click()
        except:
            #print('didnt find robot button')
            pass

        # gets past age button
        try:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='age-button-yes']"))).click()
        except:
           # print('didnt find age button')
            pass
        
        # checks page not found is being displayed
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//body[@class = 'below-desktop']")))
            #print('page not found')
            counter+='0'
        except:

            #checks if anything else is loaded
            
            WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//head")))

            # include this if you want more time on the pdfs
            #time.sleep(5)
            counter+='1'
            
            print('found pdf')
            if counter[-1] == '1':
                file_name = url[-12:-4] + '.png'
                driver.save_screenshot(file_name)
                
                with Image.open(file_name) as im:
                    im = im.crop((530,20,560,70))
                    im.save('crop.png')
                os.remove(file_name)
                #crop_name = url[-12:-4] + 'crop' + '.png'
                #im.save(crop_name)
                
                if pdfs == 0:
                    pdfs+=1
                    with Image.new('RGB',(763,2000),(255,255,255)) as filled:
                        my_name = orig_url[-19:-17] + '-' + orig_url[-12:-4] + 'filled.png'
                        crop = Image.open('crop.png')
                        filled.paste(crop,(5,5))
                        filled.save(my_name)
                    txt_name = orig_url[-19:-17] + '-' + orig_url[-12:-4]+'.txt'
                    with open(txt_name,'w') as f:
                        f.write(str(pdfs) + ' - '+ url[-12:-4])
                    
                    
                else:
                    coords = placer(pdfs)
                    print('coords: ',coords)
                    with Image.open(my_name) as filled:
                        my_name = orig_url[-19:-17] + '-' + orig_url[-12:-4] + 'filled.png'
                        crop = Image.open('crop.png')
                        filled.paste(crop, coords)
                        filled.save(my_name)
                    txt_name = orig_url[-19:-17] + '-' + orig_url[-12:-4]+'.txt'
                    with open(txt_name,'a') as f:
                        f.write('\n' + str(pdfs+1) + ' - ' + url[-12:-4])
                    pdfs+=1
                    
                os.remove('crop.png')
                
                
                
            # except:
            #     print('didnt work')
            #     pass

        #increments the url by 1
        my_num=int(url[-11:-4])
        if adding == '+':
            my_num+=1
        else:
            my_num-=1
        my_str=str(my_num)
        for i in range(10):
            if len(my_str) < 8:
                my_str = '0' + my_str
            if len(my_str) == 8:
                break
        my_url1=url[:-12]
        url = my_url1 + my_str + '.pdf'

        #checks if the last 10 pages have been page not found, this number can be change
        if counter[-10:] == '0000000000':

            # goes back to original url and then repeats the process but decreeasing url
            if adding == '+':
                adding = '-'
                url = ''
                for l in orig_url:
                    url += l 
                my_num=int(url[-11:-4])
                my_num-=1
                my_str=str(my_num)
                for i in range(10):
                    if len(my_str) < 8:
                        my_str = '0' + my_str
                    if len(my_str) == 8:
                        break
                my_url1=url[:-12]
                url = my_url1 + my_str + '.pdf'

            # once another 10 page not founds is loaded program stops
            else:
                break


        #time.sleep(3)
    
    driver.close()


scrape(url)