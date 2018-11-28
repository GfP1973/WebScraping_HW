
# coding: utf-8

# In[1]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

driver = webdriver.Chrome()


# In[3]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
#response = requests.get(url) didn't return the full page for some reason, so I used webdriver as suggested on StackOverflow...
#reason presumed the Nasa page uses some Java elements that breaks requests  

driver.get(url)


# In[4]:


soup1 = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


# In[5]:


#print(soup1.prettify())


# In[5]:


news_title = soup1.find_all('div', class_='list_text')

headlines = []
teaser = []

for news in news_title:
    head = news.find('a').text.strip('\n')
    headlines.append(head)
    tease = news.find('div', class_='article_teaser_body').text
    teaser.append(tease)
    


# In[154]:


#len(headlines)
#print(teaser)


# In[6]:


nasa_news_dic = dict(zip(headlines,teaser))


# In[175]:


#nasa_news_dic


# In[7]:


url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_jpl)


# In[8]:


html = browser.html
soup2 = BeautifulSoup(html, 'html.parser')


# In[9]:


featured_image = soup2.find('a', class_='button fancybox')
image_link = featured_image['data-fancybox-href']


# In[10]:


print(image_link)


# In[11]:


featured_image_url = ("https://www.jpl.nasa.gov" + image_link)


# In[12]:


featured_image_url


# In[13]:


url_twit = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url_twit)


# In[14]:


html = browser.html
soup3 = BeautifulSoup(html, 'html.parser')


# In[15]:


mars_weather = soup3.find('div', class_='js-tweet-text-container').text


# In[16]:


print(mars_weather)


# In[17]:


url_facts = 'http://space-facts.com/mars/'
mars_table = pd.read_html(url_facts)


# In[27]:


#mars_table


# In[18]:


mars_df = mars_table[0]
mars_df.columns = ['Profile', 'Facts & Stats']


# In[28]:


#mars_df


# In[19]:


mars_facts = mars_df.to_html()
#mars_facts


# In[20]:


mars_facts.replace('\n', " ")


# In[21]:


url_usgs ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url_usgs)


# In[22]:


html=browser.html
soup4 = BeautifulSoup(html, 'html.parser')


# In[23]:


mars_hemihead = soup4.find_all('h3')


# In[24]:


headers = []

for hemi in mars_hemihead:
    head = hemi.text
    headers.append(head)


# In[25]:


headers


# In[36]:


hemi_clicks = soup4.find_all('div',class_='item')


# In[61]:


#hemi_clicks


# In[45]:


hemi_urls =[]

for urls in hemi_clicks:
    hemis = urls.a['href']
    hemi_urls.append(hemis)


# In[48]:


#hemi_urls


# In[49]:


second_scrape = ['https://astrogeology.usgs.gov' + hemi for hemi in hemi_urls]

#second_scrape
    


# In[59]:


full_hemi_url = []

for seconds in second_scrape:
    browser.visit(seconds)
    html=browser.html
    soup5 = BeautifulSoup(html, 'html.parser')
    pic_element = soup5.find('a', target="_blank")
    centerfold = pic_element['href']
    full_hemi_url.append(centerfold)


# In[60]:


full_hemi_url


# In[173]:





# In[147]:


headers_dic = []

for head in headers:
    headers_dic.append({'title': head})
    
url_dic = []

for url in full_hemi_url:
    url_dic.append({'img': url})



# In[159]:


headers_dic 


# In[160]:


url_dic

