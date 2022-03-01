# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:10:58 2021

@author: jvasq
"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


path = "C:/Users/jvasq/PythonProjects/Realtor Home Data/chromedriver"

#url = 'https://www.zillow.com/'
url = 'https://www.zillow.com/mchenry-il-60051/sold/house,townhouse_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2260051%22%2C%22mapBounds%22%3A%7B%22west%22%3A-88.44443099756683%2C%22east%22%3A-88.04308669825042%2C%22south%22%3A42.279663758860636%2C%22north%22%3A42.3806802921054%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A84314%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1988%7D%2C%22doz%22%3A%7B%22value%22%3A%2212m%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

source = requests.get(url)

#print(dir(source))
#print('Status code: ', source.status_code)
#print(source.ok)
#print(source.headers)

source = requests.get(url).text # requests.get().text returns the HTML source code 
# for the URL that is passed through to it

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify)


# Initializing the webdriver
# = webdriver.ChromeOptions()

# Uncomment the line below if you'd like to scrape without a new Chrome window every time.
# options.add_argument('headless')

# Change the path to where chromedriver is in your home folder.
#driver = webdriver.Chrome(
#    executable_path=path, options=options)
#driver.set_window_size(1000, 1000)

#driver.get(url)
print('')
#print(driver.title)
print(' ')
#driver.quit()

#houses = driver.find_elements_by_class_name("list-card-info")

#def get_houses(keyword, num_houses, verbose, path, slp_time):
def get_houses(num_houses, verbose, path, slp_time):
    '''Gathers homes as a dataframe, scraped from Zillow'''

    # Initializing the webdriver
    options = webdriver.ChromeOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(
        executable_path=path, options=options)

#    keyword = 'x'
    url      = 'https://www.zillow.com/mchenry-il-60051/sold/house,townhouse_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2260051%22%2C%22mapBounds%22%3A%7B%22west%22%3A-88.44443099756683%2C%22east%22%3A-88.04308669825042%2C%22south%22%3A42.279663758860636%2C%22north%22%3A42.3806802921054%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A84314%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1988%7D%2C%22doz%22%3A%7B%22value%22%3A%2212m%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
#    url_base = 'https://www.zillow.com'+keyword+'?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%2260051%22%2C%22mapBounds%22%3A%7B%22west%22%3A-88.44443099756683%2C%22east%22%3A-88.04308669825042%2C%22south%22%3A42.279663758860636%2C%22north%22%3A42.3806802921054%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A84314%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1988%7D%2C%22doz%22%3A%7B%22value%22%3A%2212m%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
    driver.get(url)
    houses = []
    driver.set_window_size(1000, 1440)
    
    time.sleep(5)
     
#    for i in range(5):
#        driver.execute_script("window.scrollTo(0,((document.body.scrollHeight)/2))")
#        time.sleep(1)
#        print('Scrolled', i, 'time(s)')
    
#    driver.execute_script("window.scrollTo(0,((document.body.scrollHeight)/1.3))")    
#    time.sleep(1)     
#    driver.execute_script("window.scrollTo(0,((document.body.scrollHeight)/2))")   
#    time.sleep(1)    
#    driver.execute_script("window.scrollTo(0,((document.body.scrollHeight)/2))")   
#    time.sleep(1)
#    driver.execute_script("window.scrollTo(0,((document.body.scrollHeight)/2))")   
#    time.sleep(1)

    # Zillow will only load home results as you scroll, so we need to scroll 
    # the page in order for selenium to pull the html for all of the houses. 
    # Referenced this site for help getting the correct scroll code to work
    # https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7

    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1
    
    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break

#    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#    next_pg = driver.find_element_by_class_name('PaginationJumpItem-c11n-8-37-0__sc-18wdg2l-0 eGOQHk')
#    next_pg.send_keys(Keys.END)  

    print('Scrolled')

    soup = BeautifulSoup(driver.page_source, 'lxml')
   

    while len(houses) < num_houses:  # If true, should be still looking for new jobs.

        # Let the page load. Change this number based on your internet speed.
        # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)
        
#        driver.execute_script('window.scrollTo(0, document.body.scdrollHeight);')

        # Going through each job in this page
#        house_buttons = driver.find_elements_by_class_name(
#            "list-card-info")  # Specifies the information portion of a listing (not the photo)
#        house_buttons = driver.find_elements_by_class_name(
#            "list-card-addr")

        #scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        #screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        #i = 1
        
        #while True:
            # scroll one screen height each time
        #    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        #    i += 1
        #    time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        #    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            # Break the loop when the height we need to scroll to is larger than the total scroll height
        #    if (screen_height) * i > scroll_height:
        #        break
        #print('Scrolled')

        prices = soup.find_all('div', class_='list-card-price')
        #prices = soup.find('span', class_='hdp__sc-xvht8h-0 gDztRH ds-status-details').text
        details = soup.find_all('ul', class_='list-card-details')
        addresses = soup.find_all('address', class_='list-card-addr')
        #house_buttons = soup.find_all('a', class_='list-card-link list-card-link-top-margin')
        house_buttons = driver.find_elements_by_class_name('list-card-info') # code ran and clicked the listing with this linelist-card-link list-card-link-top-margin

        print('')
        print('Prices', len(prices))
        print('Details', len(details))
        print('Addresses', len(addresses))
        print('House buttons', len(house_buttons))
#        print(house_buttons)
        print('')
        
        time.sleep(slp_time)
        
#        for button in house_buttons:
        for button in house_buttons:
            button.click()
            time.sleep(slp_time)
            scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
            screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
            i = 1
            
            
            
            while True:
                # scroll one screen height each time
                driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
                i += 1
                time.sleep(scroll_pause_time)
                # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
                scroll_height = driver.execute_script("return document.body.scrollHeight;")  
                # Break the loop when the height we need to scroll to is larger than the total scroll height
                if (screen_height) * i > scroll_height:
                    break
            print('Scrolled listing')
        
        for (price, detail, address, button) in zip(prices, details, addresses, house_buttons):

            print("Progress: {}".format("" + str(len(houses)) + "/" + str(num_houses)))
            if len(houses) >= num_houses:
                break

            #job_button.click()  # You might
            #driver.execute_script("arguments[0].click();", house)
            #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(.01)
            time.sleep(slp_time)
            collected_successfully = False

            while not collected_successfully:
                try:
                    price = price.text
                    address = address.text
                    detail = detail.text
                    page = button['href']
                    #price = driver.find_elements_by_class_name('list-card-price').text
                    #address = driver.find_element_by_class_name('list-card-addr').text
                    #job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    #job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    #time.sleep(.1)
                    pass
                    
#            try:
#                page = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/li[1]/article/div[1]/a').get_attribute('href')
#                page = driver.find_element_by_xpath('.//a[@href]').get_attribute('href')
#                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
#            except NoSuchElementException:
#                page = 'None'
#                salary_estimate = -1  # You need to set a "not found value. It's important."

#            try:
#                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
#            except NoSuchElementException:
#                rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging 
            if verbose:
                print("Price: {}".format(price))
#                print("Salary Estimate: {}".format(salary_estimate))
#                print("Job Description: {}".format(job_description[:500]))
#                print("Specs: {}".format(specs))
                print("Details: {}".format(detail))
                print("Address: {}".format(address))
                print("URL: {}".format(page))
#                print("URL: {}".format(button['href']))
#                print(button)
                
            houses.append({
                         "Price": price,
                         "Address": address,
                         "Details": detail,
                         "URL": page
                         })
            
            print('')
            print(len(houses))
            print('')
            
#        keyword = driver.find_elements_by_class_name('StyledButton-c11n-8-37-0__wpcbcc-0 cyhUbV PaginationButton-c11n-8-37-0__si2hz6-0 eIcuqd[-1]').get_attribute('href')
#        keyword = soup.find(attrs={'title':'Next page'})['href']
#        print(keyword)
#        next_page = url_base
        print('')
#            print(len(next_page))
#        print(next_page)
         
        try:
            #next_page = soup.find(attrs={'title':'Next page'})
            #next_page = soup.find_all('a', 'StyledButton-c11n-8-37-0__wpcbcc-0 cyhUbV PaginationButton-c11n-8-37-0__si2hz6-0 eIcuqd')
            #print(driver.find_element_by_xpath(".//a[@class='StyledButton-c11n-8-37-0__wpcbcc-0 cyhUbV PaginationButton-c11n-8-37-0__si2hz6-0 eIcuqd' and @title='Next page'"))
            #driver.find_element_by_xpath(".//a[@class='StyledButton-c11n-8-37-0__wpcbcc-0 cyhUbV PaginationButton-c11n-8-37-0__si2hz6-0 eIcuqd' and@title='Next page'").click()
            
            driver.find_element_by_class_name('StyledButton-c11n-8-37-0__wpcbcc-0 cyhUbV PaginationButton-c11n-8-37-0__si2hz6-0 eIcuqd[8]').click()
            
            #np = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[3]/nav/ul/li[10]")
            #np = driver.find_element_by_css_selector('li.PaginationJumpItem-c11n-8-37-0__sc-18wdg2l-0:nth-child(10) > a:nth-child(1)')
            #driver.execute_script("arguments[0].click();", np)
            
            #driver.find_element_by_css_selector('li.PaginationJumpItem-c11n-8-37-0__sc-18wdg2l-0:nth-child(10) > a:nth-child(1)').click()
                  
            #driver.get(next_page)
        except TimeoutError:
            print('Did not click next page')
            
#        try:
#            driver.find_element_by_xpath('.//li[@class="next"]//a').click()
#        except NoSuchElementException:
#            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs,
#                                                                                                         len(jobs)))
#            break
        
#    driver.quit()
    return pd.DataFrame(houses)


homes = get_houses(41, True, path, 5)