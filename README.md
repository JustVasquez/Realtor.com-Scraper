# Zillow.com-Scraper
Scraper for home data from Realtor.com

# Purpose
This is a Zillow.com scaper for home data where I will use regression models to predict what price my parents should list the home for when they are ready to sell it. 
As of the latest update to this project, the user will go to Zillow and search for the specific parameters they are looking for, then input the URL into the code to launch chromedriver instance through Selenium to scrape the data for their query. The scraper goes through the page of search results and pulls relevant information like price, # of beds, # of baths, available on the listing's card. 

# Current Issue
The scraper runs as expected on the initial search page that is fed, but runs into Captcha issues when moving to the next page in the search results that I have been unable to get past. 
