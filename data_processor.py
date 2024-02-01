class DataProcessor:
    def process_lcu_champion_select_data(self, session_data):
        """
        Processes LCU champion select session data to extract key details.

        Parameters:
        - session_data: The JSON response from the LCU API containing champion select session details.

        Returns:
        A dictionary with processed champion select details, focusing on picks and bans.
        """
        processed_data = {
            'bans': {
                'myTeamBans': session_data.get('bans', {}).get('myTeamBans', []),
                'theirTeamBans': session_data.get('bans', {}).get('theirTeamBans', []),
            },
            'picks': [],
            'isSpectating': session_data.get('isSpectating', False),
            'myTeam': [],
            'theirTeam': [],
        }

        # Process picks and roles
        for action in session_data.get('actions', []):
            for pick in action:
                if pick.get('type') == 'pick' and pick.get('completed', False):
                    processed_data['picks'].append({
                        'championId': pick.get('championId'),
                        'pickTurn': pick.get('pickTurn'),
                        'actorCellId': pick.get('actorCellId')
                    })

        # Distinguish between my team and their team based on actorCellId
        myTeamIds = [player.get('cellId') for player in session_data.get('myTeam', [])]
        theirTeamIds = [player.get('cellId') for player in session_data.get('theirTeam', [])]

        for pick in processed_data['picks']:
            if pick['actorCellId'] in myTeamIds:
                processed_data['myTeam'].append(pick)
            elif pick['actorCellId'] in theirTeamIds:
                processed_data['theirTeam'].append(pick)

        return processed_data

# Example usage:
if __name__ == "__main__":
    # Placeholder for the actual session data retrieval from the LCU API
    session_data = {}  # This should be replaced with the actual call to fetch the LCU champion select data

    processor = DataProcessor()
    processed_data = processor.process_lcu_champion_select_data(session_data)

    # Print the processed data for verification
    print(processed_data)
