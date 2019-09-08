import requests

base_api = 'https://api.sleeper.app/v1/'

def get_user(userid):
    endpoint = 'user/'
    url = f'{base_api}{endpoint}{userid}'
    print(f'Getting user info for {userid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_rosters(leagueid):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/rosters'
    print(f'Getting league info for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_users(leagueid):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/users'
    print(f'Getting users for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_matchups(leagueid,week):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/matchups/{week}'
    print(f'Getting matchups for {leagueid} week {week}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_playoffs_winners(leagueid):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/winners_bracket'
    print(f'Getting winners bracket for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_playoffs_losers(leagueid):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/losers_bracket'
    print(f'Getting losers bracket for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_transactions(leagueid,week):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/transactions/{week}'
    print(f'Getting transactions for {leagueid} week {week}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_trades(leagueid):
    endpoint = 'league/'
    url = f'{base_api}{endpoint}{leagueid}/traded_picks'
    print(f'Getting traded picks for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_players(leagueid):
    endpoint = 'players/nfl'
    url = f'{base_api}{endpoint}'
    print(f'Getting all players for {leagueid}')
    resp = requests.get(url)
    data = resp.json()
    return data

# type              Either add or drop
# lookback_hours    Number of hours to look back (default is 24) - optional
# limit             Number of results you want, (default is 25) - optional
def get_trends(type,lookback,limit):
    endpoint = 'players/nfl/trending/'
    url = f'{base_api}{endpoint}{type}?lookback_hours={lookback}&limit={limit}'
    print(f'Getting top {limit} players {type} trends for the past {lookback} hours')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_season_stats():
    endpoint = '/stats/nfl/regular/2019'
    url = f'{base_api}{endpoint}'
    print(f'Getting season stats')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_week_stats(week):
    endpoint = '/stats/nfl/regular/2019/'
    url = f'{base_api}{endpoint}{week}'
    print(f'Getting week {week} stats')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_season_projections():
    endpoint = '/projections/nfl/regular/2019'
    url = f'{base_api}{endpoint}'
    print(f'Getting season projections')
    resp = requests.get(url)
    data = resp.json()
    return data

def get_week_projections(week):
    endpoint = '/projections/nfl/regular/2019/'
    url = f'{base_api}{endpoint}{week}'
    print(f'Getting week {week} projections')
    resp = requests.get(url)
    data = resp.json()
    return data
