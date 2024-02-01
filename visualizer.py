class Visualizer:
    def visualize_match_data(self, processed_data):
        print(f"Match ID: {processed_data['matchId']}")
        print(f"Game Duration: {processed_data['gameDuration']}")
        print("Participants:")
        for participant in processed_data['participants']:
            print(f"Champion: {participant['championName']}, K/D/A: {participant['kills']}/{participant['deaths']}/{participant['assists']}, Win: {participant['win']}")
