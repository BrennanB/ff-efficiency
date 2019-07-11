import os
import glob
import pandas as pd

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

    
