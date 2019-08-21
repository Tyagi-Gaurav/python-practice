from html.parser import HTMLParser
import urllib.request
from events import Odd
from events import Event
from events import Events


class MyOddsParser(HTMLParser):
    def __init__(self, output=None, team=None):
        HTMLParser.__init__(self)
        if team is None:
            team = {}
        if output is None:
            output = []
        self.output = output
        self.team = team
        self.current_team = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            contains_bk_logo = any(attr[0] == 'class' and 'bk-logo-click' in attr[1] for attr in attrs)
            if contains_bk_logo:
                title = [attr for attr in attrs if attr[0] == 'title']
                if title:
                    # print("Tag Attributes:", attrs)
                    if title[0][1] not in self.output:
                        self.output.append(title[0][1])
        elif tag == 'tr':
            contains_team = any(attr[0] == 'class' and 'diff-row evTabRow' in attr[1] for attr in attrs)
            if contains_team:
                team_name = [attr for attr in attrs if attr[0] == 'data-bname']
                self.team[team_name[0][1]] = []
                self.current_team = team_name[0][1]
        elif tag == 'td':
            contains_odds = any(attr[0] == 'class' and 'bc bs o' in attr[1] for attr in attrs)
            contains_blank = any(attr[0] == 'class' and 'np o' in attr[1] for attr in attrs)
            if contains_odds:
                odds = [attr for attr in attrs if attr[0] == 'data-fodds']
                self.team[self.current_team].append(odds[0][1])
            elif contains_blank:
                self.team[self.current_team].append('0.0')

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        pass


def parse(uri, black_list):
    req = urllib.request.Request(uri, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    parser = MyOddsParser()
    parser.feed(content)
    betting_companies = parser.output
    teams = parser.team
    # print(betting_companies)
    # print(teams)
    events_list = []

    # print("Number of teams:", len(teams))
    # print("Teams Blacklisted:", black_list)

    for team in teams:
        if team not in black_list:
            print("Team: ", team, end=" ")
            odds_list = []
            for i in range(len(betting_companies)):
                # if teams[team][i] != '0.0':
                odds_list.append(Odd(betting_companies[i], teams[team][i], team))
            events_list.append(Event(team, odds_list))

    # print("Number of betting companies: ", len(betting_companies))
    # print("Number of events:", len(events_list))
    return Events(events_list)
