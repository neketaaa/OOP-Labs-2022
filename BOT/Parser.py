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
        result = {
            'teams': []
        }
        team_list = self.page.find('table', class_='main-tournament-table')
        items = team_list.find_all('tr')
        for item in items:
            try:
                team_name = item.find('td', class_='team').find('a').text
                print(team_name)
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
                result['teams'].append(
                    {
                    'team_name': team_name,
                    'games': games,
                    'win': win,
                    'draw': draw,
                    'lose': lose,
                    'goal': goal,
                    'miss': miss,
                    'diff': diff,
                    'score': score
                    })


            except AttributeError:
                pass
        return result


class GameParser(Parser):

    def __init__(self, link):
        super().__init__(link)

    def parse_games(self):
        result = {
            'games': []
        }
        games_list = self.page.find('div', class_='table-block')
        games = games_list.find_all('div', class_='match')
        for game in games:
            try:
                time = game.find('td', class_='time').find('a').text
                first_team = game.find('td', class_='left-team').find('a').text
                second_team = game.find('td', class_='right-team').find('a').text
                date = game.find_previous('p', class_='match-date').text
                num_of_tour = game.find_previous('div', class_='match-name').find('h4').text
                num_of_tour = re.findall(r'\d+', num_of_tour)[0]
                try:
                    score = game.find('td', class_='score ended').find('a').text
                except AttributeError:
                    score = game.find('td', class_='score').find('a').text

                result['games'].append(
                    {
                    'time': time,
                    'first_team': first_team,
                    'second_team': second_team,
                    'date': date,
                    'num_of_tour': num_of_tour,
                    'score': score
                    })

            except AttributeError:
                pass
        return result


class PlayerParser(Parser):

    def __init__(self, link):
        super().__init__(link)

    def parse_player(self):
        result = None
        try:
            full_name = self.page.find('h1', class_='liga-header__title').text
            team_name = self.page.find('div', class_='alAb-dop-n1')
            nationality = team_name.find_next('div', class_='alAb-dop-n1')
            position = nationality.find_next('div', class_='alAb-dop-n1')
            age = position.find_next('div', class_='alAb-dop-n1')
            height = age.find_next('div', class_='alAb-dop-n1')

            statistics = self.page.find('td', class_='text-left fw-500')
            games_played = statistics.find_next('td')
            minutes_played = games_played.find_next('td')
            games_from_start = minutes_played.find_next('td')
            subtitles = games_from_start.find_next('td')
            games_missed = subtitles.find_next('td')
            goals = games_missed.find_next('td')
            assists = goals.find_next('td')
            positive_actions = assists.find_next('td')
            yellow_cards = positive_actions.find_next('td')
            red_cards = yellow_cards.find_next('td')
            print(games_played)
            result = {
            'full_name': full_name,
            'team_name': team_name.text,
            'nationality': nationality.text,
            'position': position.text,
            'age': age.text,
            'height': height.text,
            'games_played': games_played.text,
            'minutes_played': minutes_played.text,
            'games_from_start': games_from_start.text,
            'subtitles': subtitles.text,
            'games_missed': games_missed.text,
            'goals': goals.text,
            'assists': assists.text,
            'positive_actions': positive_actions.text,
            'yellow_cards': yellow_cards.text,
            'red_cards': red_cards.text
        }
        except AttributeError:
            pass

        print(result)

        return result


class ParserFabric:

    def parse_teams(self, link: str):
        return TeamParser(link).parse_teams()

    def parse_games(self, link: str):
        return GameParser(link).parse_games()

    def parse_player(self, link: str):
        return PlayerParser(link).parse_player()





example = TeamParser('https://football.ua/ukraine/table.html')
print(example.parse_teams())
example1 = GameParser('https://football.ua/ukraine/results/761/')
print(example1.parse_games())
example2 = PlayerParser('https://www.ua-football.com/ua/stats/player/65870-anatoliy-trubinua')
example2.parse_player()


