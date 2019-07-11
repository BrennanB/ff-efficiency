import os
import glob
import pandas as pd
import numpy as np

SCORE_DIR = "current_scoring"

if os.path.isdir(SCORE_DIR):
    pass
else:   # Make directory if it doesn't exist
    os.mkdir(SCORE_DIR)

draft_locations = glob.glob("{}/*.csv".format(SCORE_DIR))    # Gets all events to score

for draft_location in draft_locations:  # Scores all events that need to be scored
    df = pd.read_csv(draft_location)
    print(df)

    num_of_players = 0
    for i in range(0, len(df.index)):   # Find how many players are in the draft
        if df.at[i, "Player"] == "Available Teams" and num_of_players == 0:
            num_of_players = i
    print("There are {} players".format(num_of_players))

    ordered_picks = []
    index = ["Team 1", "Team 2", "Team 3"]
    for player in range(0, num_of_players):
        picked_team = df.at[player, index[0]]
        if type(picked_team) is np.float64:
            picked_team = int(picked_team)
        ordered_picks.append(picked_team)
    for player in range(num_of_players - 1, -1, -1):
        picked_team = df.at[player, index[1]]
        if type(picked_team) is np.float64:
            picked_team = int(picked_team)
        ordered_picks.append(picked_team)
    for player in range(0, num_of_players):
        picked_team = df.at[player, index[2]]
        if type(picked_team) is np.float64:
            picked_team = int(picked_team)
        ordered_picks.append(picked_team)

    unselected_picks = []
    for i in range(num_of_players+1, len(df.index)):
        headers = list(df)
        for header in headers:
            unpicked_team = df.at[i, header]
            if type(unpicked_team) is np.float64:
                unpicked_team = int(unpicked_team)
            if unpicked_team != "-":
                unselected_picks.append(unpicked_team)

    print(ordered_picks)
    print(unselected_picks)
