from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import time
import threading 

class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""

def job(my_list):
	print("In Job")
	while len(my_list) != 0:
		print("In While")
		player = my_list.pop(0)
		get_nba_player_image_syn(player.link, player.name)
    	
def get_nba_player_image_syn(url, name):
	
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')
	driver.get(url)
	#time.sleep(2)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_ = 'player-summary__image-block')
	img = div.find('img')
	print (img['src'])
	f = open('nba_player\{0}.jpg'.format(name),'wb')
	f.write(requests.get(img['src']).content)
	f.close()
	driver.quit()


def get_player_list(player_list):
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	#url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'
	url = 'https://stats.nba.com/players/list/'
	# download html page
	driver.get(url)

	# create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_= 'stats-player-list players-list')   #'col-lg-12'
	for a in div.find_all('a'):
		# print (a.text)
		# print (a['href'])
		new_play = Player()
		new_play.name = a.text
		new_play.link = "https://stats.nba.com"+a['href']
		if new_play.name =="Run It":
			pass
		else:
			player_list.append(new_play)
	driver.quit()
	#player_list.pop(0)
	return True
	#return player_list

def get_detail_for_all_players(player_list):
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	for p in player_list[0:6]:
		url = p.link
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		Height = ""
		Weight = ""
		Born = ""
		divspan = soup.find_all('div', class_ = 'player-stats__stat-title')
		for divs in divspan:
			if divs.text =="HT":
				for span in divs.findNextSiblings():
					Height = Height + span.text

			elif divs.text =="WT":
				for span in divs.findNextSiblings():
					Weight = Weight + span.text

			elif divs.text =="BORN":
				for span in divs.findNextSiblings():
					Born = Born + span.text
	
		p.Height = Height
		p.Weight = Weight
		p.Born = Born #Born
		

	driver.quit()

	return player_list

def get_nba_player_image(player_list):
	
	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')

	
	for player in player_list[0:4]:

		# url = 'http://www.nba.com/playerfile/tony_allen/'

		url = player.link

		driver.get(url)

		time.sleep(2)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		# print (driver.page_source)

		div = soup.find('div', class_ = 'player-summary__image-block')

		img = div.find('img')

		print (img['src'])

		f = open('nba_player\{0}.jpg'.format(player.name),'wb')

		f.write(requests.get(img['src']).content)

		f.close()

	driver.quit()

if __name__ == '__main__':
    list_links = []
    flag = get_player_list(list_links)
    links = list_links[0:40]
    t1 = threading.Thread(target=job, args=(links,))
    t2 = threading.Thread(target=job, args=(links,))
    t3 = threading.Thread(target=job, args=(links,)) 
    t4 = threading.Thread(target=job, args=(links,)) 
    t5 = threading.Thread(target=job, args=(links,)) 
    #get_nba_player_image( get_player_list() )

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    #print(list_links[0:7])
    #print(flag)

