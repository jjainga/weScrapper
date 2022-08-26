import requests
import time
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

game_list = []

page=0
# source
#print(url)
while page <= 82:
    print(page)
    url = 'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?page='+str(page)
    try:
        source = requests.get(url, headers=headers, allow_redirects=True)
        source.raise_for_status()

    #time.sleep(5)

        soup = BeautifulSoup(source.content,'html.parser')
    #print(soup.prettify())
        all_list= soup.find_all('table', class_='clamp-list')
    #all_games = soup.find('table', class_='clamp-list').find_all(class_='clamp-summary-wrap')
    #print(all_games)
    
        for the_list in all_list:
            all_games = the_list.find_all(class_='clamp-summary-wrap')
            for game in all_games:
                new_game = {}
                new_game['title'] = game.find('h3').text
                new_game['position'] = game.find('span',class_='title numbered').get_text(strip=True).split(".")[0]
                new_game['rating'] = game.find(class_='metascore_w large game positive').text
                new_game['platform'] = game.find(class_='clamp-details').find('div', class_='platform').find(class_='data').get_text(strip=True)
                new_game['release_date'] = game.find(class_='clamp-details').find('span', class_='').text
                game_list.append(new_game)

        page = page + 1


    except Exception as e:
        print(e)


print(game_list)