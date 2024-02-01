import requests

class Consts:
    REGIONS = {
        'europe_nordic_and_east': 'eun1',
        'north_america': 'na1',
    }
    URL = {
        'base': 'https://{region}.api.riotgames.com/lol/',
        'summoner_by_name': 'summoner/v4/summoners/by-name/{summonerName}',
    }

class RiotAPI:
    def __init__(self, api_key, region='na1'):
        self.api_key = api_key
        self.region = region

    def request(self, url, params={}):
        params['api_key'] = self.api_key
        full_url = url + f"?api_key={self.api_key}"
        for key, value in params.items():
            full_url += f"&{key}={value}"
        print(f"Requesting URL: {full_url}")  # Debug print to check the constructed URL
        response = requests.get(full_url, verify=False)  # 'verify=False' for self-signed certs, remove for production
        response.raise_for_status()
        return response.json()

    def get_summoner_by_name(self, summonerName):
        url = Consts.URL['base'].format(region=self.region) + Consts.URL['summoner_by_name'].format(summonerName=summonerName)
        return self.request(url)
