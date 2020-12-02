from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    step1 = soup.find('ul', class_='item_list')
    step2 = step1.find('li', class_='slide')
    news_title = step2.find('div', class_='content_title').text

    news_p = step2.find('div', class_='article_teaser_body').get_text()
    url_images = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_images)

    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('figure', class_='lede').a["href"]
    featured_image_url = "https://www.jpl.nasa.gov" + results

    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)

    tables = pd.read_html(url_facts)
    df = tables[0]
    df.columns = ['Mars', 'Profile']
    df

    df.set_index('Mars', inplace=True)
    df.head()

    html_table = df.to_html()


    html_table.replace('\n', '')

    df.to_html('table.html')

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='description')

    title_list = []
    for result in results:
        title = result.find('h3').text
        print(title)
        title_list.append(title)


    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus = soup.find('img', class_='wide-image')["src"]
    cerberus_hr = "https://astrogeology.usgs.gov" + cerberus

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    schiap = soup.find('img', class_='wide-image')["src"]
    schiap_hr = "https://astrogeology.usgs.gov" + schiap

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    syrtis = soup.find('img', class_='wide-image')["src"]
    syrtis_hr = "https://astrogeology.usgs.gov" + syrtis

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    valles = soup.find('img', class_='wide-image')["src"]
    valles_hr = "https://astrogeology.usgs.gov" + valles