from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup
import re


class Parser:

    def __init__(self, link):
        self.page = self.page_to_html(link)

    def page_to_html(self, link):
        temp_page = requests.get(link)
        return BeautifulSoup(temp_page.content, 'html.parser')

class TeamParser(Parser):

    def __init__(self, link):
        super().__init__(link)

    def parse_teams(self):
        result = []
        team_list = self.page.find('table', class_='main-tournament-table')
        items = team_list.find_all('tr')
        for item in items:
            try:
                team = item.find('td', class_='team').find('a').text
                print(team)
                num = item.find('td', class_='num').text
                print(num)
                games = item.find('td', class_='games').text
                win = item.find('td', class_='win').text
                draw = item.find('td', class_='draw').text
                lose = item.find('td', class_='lose').text
                goal = item.find('td', class_='goal').text
                miss = item.find('td', class_='miss').text
                diff = item.find('td', class_='diff').text
                score = item.find('td', class_='score').text
            except AttributeError:
                pass


class GameParser(Parser):

    def __init__(self, link):
        super().__init__(link)

    def parse_games(self):
        result = []
        games_list = self.page.find('div', class_='table-block')
        games = games_list.find_all('div', class_='match')
        for game in games:
            try:
                time = game.find('td', class_='time').find('a').text
                first_team = game.find('td', class_='left-team').find('a').text
                second_team = game.find('td', class_='right-team').find('a').text
                try:
                    score = game.find('td', class_='score ended').find('a').text
                except AttributeError:
                    score = game.find('td', class_='score').find('a').text
                date = game.find_previous('p', class_='match-date').text
                num_of_tour = game.find_previous('div', class_='match-name').find('h4').text
                num_of_tour = re.findall(r'\d+', num_of_tour)[0]
            except AttributeError:
                pass



example = TeamParser('https://football.ua/ukraine/table.html')
print(example.parse_teams())
example1 = GameParser('https://football.ua/ukraine/results/761/')
example1.parse_games()


