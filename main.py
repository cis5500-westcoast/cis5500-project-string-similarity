import pandas as pd
from fuzzywuzzy import fuzz
import difflib

# define a function to calculate similarity using the SequenceMatcher method
def similarity(a, b):
    a = str(a)
    b = str(b)
    return difflib.SequenceMatcher(None, a, b).ratio()


# Load CSV file into a Pandas DataFrame
player1_df = pd.read_csv('goalscorers_utf8.csv', encoding='utf8', index_col=False)
player2_df = pd.read_csv('players_utf8.csv', encoding='utf8', index_col=False)
#print(player2_df.head())

player1_df.dropna(subset=['scorer'], inplace=True)
player1_df.drop_duplicates(subset=['scorer'], keep='first', inplace=True)
player1_df.sort_values(by='scorer', ascending=False).reset_index(drop=True)
player_1_sm_df = player1_df[['scorer']]
print("player_1_sm_df",player_1_sm_df.count())

player2_df.dropna(subset=['full_name'], inplace=True)
player2_df.drop_duplicates(subset=['full_name'], keep='first', inplace=True)
player2_df.sort_values(by='full_name', ascending=False).reset_index(drop=True)
player_2_sm_df = player2_df[['full_name']]
print("player_2_sm_df",player_2_sm_df.count())

player_match_df = pd.DataFrame(columns=['scorer', 'full_name', 'similarity'])
player_match_df['full_name'] = player_2_sm_df['full_name']
#print(player_match_df['full_name'])

# find the player name that is most similar to the full_name in player1_df
for i, row in player_match_df.iterrows():
    print(i)
    # compute similarity scores between scorer and all full_names
    similarity_scores = player_1_sm_df['scorer'].apply(lambda x: similarity(x, row['full_name']))
    # print(similarity_scores)
    #player_match_df.loc[i,'full_name'] = player_match_df.loc[i, 'full_name']
    print("Full_name: ",player_match_df.loc[i, 'full_name'])  # !!!!  full_name
    player_match_df.loc[i,'similarity'] = similarity_scores.max()
    print("Similarity: ",similarity_scores.max())
    
    if max(similarity_scores) > 0.5:
        #similarity_list = similarity_scores.tolist()
        # find index of highest similarity score
        max_index = similarity_scores.idxmax()
        #print(max_index)
        print("Scorer: ",player1_df.loc[max_index, 'scorer'])  # !!!! scorer
        player_match_df.loc[i,'scorer'] = player1_df.loc[max_index, 'scorer']

    else:
        player_match_df.loc[i,'scorer'] = 'No Match'
        print("Scorer: No Match")  # !!!! scorer


player_match_df.to_csv('player_match.csv')

print(player_match_df.head(10))
