import requests
import time
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

game_list = []

page = 1
  
url = 'https://opencritic.com/browse/all?page='+str(page)
try:
    source = requests.get(url, headers=headers, allow_redirects=True)
    source.raise_for_status()

    #time.sleep(5)

    soup = BeautifulSoup(source.content,'html.parser')
    #print(soup.prettify())
    all_list= soup.find('div', class_='desktop-game-display')
    #all_games = soup.find('table', class_='clamp-list').find_all(class_='clamp-summary-wrap')
    
    #print(all_list.prettify())
    for the_list in all_list:
        all_games = the_list.find_all('div',class_='row no-gutters py-2 game-row align-items-center')
        #print(all_games)
        for game in all_games:
            
            new_game = {}
            new_game['title'] = game.find('div',class_='game-name col').get_text(strip=True)
            new_game['position'] = game.find('div',class_='rank').get_text(strip=True).split(".")[0]
            new_game['rating'] = game.find('div',class_='score col-auto').get_text(strip=True)
            new_game['platform'] = game.find('div',class_='platforms col-auto').get_text(strip=True)
            new_game['release_date'] = game.find('div',class_='first-release-date col-auto show-year').get_text(strip=True)
            game_list.append(new_game)

except Exception as e:
    print(e)


print(game_list)