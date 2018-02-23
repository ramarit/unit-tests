# -*- coding: utf-8 -*-
#testLang2.py
#pip install selenium
#pip install langdetect
#brew install phantomjs
#pip install unidecode


# langdetect supports 55 languages out of the box ([ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)):
# af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, 
# nl, no, pa, pl, pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw

from selenium import webdriver
from langdetect import detect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains
from unidecode import unidecode
import re

url = 'http://live-igcommerce.pantheonsite.io/fr-fr/produit/outils-d-etalonnage/calibrateurs-de-pression/fluke-700g'
#elementID = 'fluke-product-display-features'

def is_Lang_by_id(URL):	
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	driver.set_window_size(2000, 1500)
	elem = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_id('fluke-product-display-features'))
	#print elem.text[:160]
	lang = detect(elem.text[:160])
	driver.quit()
	#print lang
	return lang
#is_Lang_by_id(url, elementID)

#ffc20e
def is_background_color(URL):	
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	driver.set_window_size(2000, 1500)
	rgba = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_css_selector('#fluke-product-display-ctas a:nth-child(1)').value_of_css_property('background-color'))
	hex = Color.from_string(rgba).hex
	driver.quit()
	#hex = str(hex)
	print (hex)
	return hex
	
#is_background_color('http://live-igcommerce.pantheonsite.io/cs-cz/produkt/kalibracni-pristroje/tlakove-kalibratory/fluke-700g')


bread_crumb_url = 'https://live-igcommerce.pantheonsite.io/cs-cz/produkt/kalibracni-pristroje/tlakove-kalibratory/fluke-700g'
def is_bread_crumb(URL):
	pageNav = []
	urlNav = []
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	driver.set_window_size(2000, 1500)

	#traverse DOM and get breadcrumb nav
	elem = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_css_selector('#fluke-product-display-breadcrumbs'))
	children = elem.find_elements_by_xpath("//span[@itemprop='name']")
	#loop through span elements, decode ASCII characters, replace ' ' with '-', append to list
	for child in children:
		decoded_string = unidecode(child.text)
		decoded_string = re.sub(' ', '-', decoded_string)
		pageNav.append(decoded_string.lower())

	#remove first and last element from list
	pageNav.pop(len(pageNav)-1)
	pageNav.pop(0)

	#split URL and remove first part of URL(http://live-igcommerce.pantheonsite.io/cs-cz) and last nav element
	urlNav = URL.split('/')
	del urlNav[:4]
	del urlNav[-1]

	driver.quit()

	#compare lists
	if pageNav == urlNav:
		#print 'true'
		return True
	else:
		#print 'false'
		return False

#bread_crumb(bread_crumb_url)

#fluke-product-display-breadcrumbs li:nth-last-child(1)
def is_product_breadcrumb_bold(URL):
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	bold = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_css_selector('#fluke-product-display-breadcrumbs li:nth-last-child(1)').value_of_css_property('font-weight'))
	driver.set_window_size(2000, 1500)
	driver.quit()
	#print (bold)
	return bold


def mouseover_color(URL):
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	driver.set_window_size(2000, 1500)
	navElement = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_css_selector('.nav a:nth-child(1)'))
	Hover = ActionChains(driver).move_to_element(navElement)
	Hover.perform()

	navColor = WebDriverWait(driver, timeout=10).until(
		lambda drive: drive.find_element_by_css_selector('#block-igcommerce-utility-ig-primary-nav ul.nav li.dropdown:hover a').value_of_css_property('color'))
	#print (navColor)
	hex = Color.from_string(navColor).hex
	#print (hex)
	driver.quit()
	return hex

#mouseover_color('https://live-igcommerce.pantheonsite.io/cs-cz/produkt/kalibracni-pristroje/tlakove-kalibratory/fluke-700g')

def title_h1(URL):
	driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
	driver.get(URL)
	driver.set_window_size(2000, 1500)
	title = WebDriverWait(driver, timeout=10).until(
		lambda br: br.find_element_by_css_selector('#fluke-product-display-title'))
	#print (title.tag_name)
	driver.quit()
	return title.tag_name

#title_h1('https://live-igcommerce.pantheonsite.io/cs-cz/produkt/kalibracni-pristroje/tlakove-kalibratory/fluke-700g')



