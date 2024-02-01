from api_handler import RiotAPI
from data_processor import DataProcessor
from visualizer import Visualizer

def get_recent_match_id(api, summoner_puuid):
    """
    Fetches the most recent match ID for the given summoner's PUUID.
    
    Parameters:
    - api: An instance of RiotAPI.
    - summoner_puuid: PUUID of the summoner to fetch recent match for.
    
    Returns:
    A string representing the most recent match ID.
    """
    matches_url = f"https://{api.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?start=0&count=1"
    match_ids = api.request(matches_url)
    return match_ids[0] if match_ids else None

from api_handler import RiotAPI
# Ensure other imports are correctly defined

def main():
    api_key = "RGAPI-33eef6bc-dfb5-4651-b1cf-4257674334cd"
    region = "na1"  # Adjust based on the actual region
    summoner_name = "ActualSummonerNameHere"  # Replace with the actual summoner name

    riot_api = RiotAPI(api_key, region)
    summoner_data = riot_api.get_summoner_by_name(summoner_name)
    if not summoner_data:
        print("Failed to fetch summoner data. Please check the summoner name and your API key.")
        return

    # Fetch the most recent match ID
    recent_match_id = get_recent_match_id(riot_api, summoner_data['puuid'])
    if not recent_match_id:
        print("Failed to fetch recent match ID. Please ensure the summoner has recent matches.")
        return

    # Fetch match details
    match_data = riot_api.get_match_by_id(recent_match_id)
    if not match_data:
        print("Failed to fetch match data.")
        return

    # Process and visualize match data
    processor = DataProcessor()
    processed_data = processor.process_match_data(match_data)
    
    visualizer = Visualizer()
    visualizer.visualize_match_data(processed_data)

if __name__ == "__main__":
    main()
