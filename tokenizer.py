import pandas as pd
import nltk
import spacy

nlp = spacy.load('en_core_web_lg')

# define a function to tokenize a string
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# define a function to calculate similarity using the SequenceMatcher method
def similarity(a, b):
    a = str(a)
    b = str(b)
    a1 = nlp(a)
    b1 = nlp(b)
    similarity = a1.similarity(b1)
    if similarity > 0.9:
        return True
    else:
        return False
    
def token_check(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if similarity(i, j):
                count += 1
                if count > 1:
                    return True
    return False


# Load CSV file into a Pandas DataFrame
players_df = pd.read_csv('player_match.csv', index_col=False)

# apply the function to the 'text' column and create a new 'tokens' column
players_df['fn_tokens'] = players_df['full_name'].apply(tokenize)
players_df['pl_tokens'] = players_df['scorer'].apply(tokenize)
players_df['token_compare'] = False

for i, row in players_df.iterrows():
    print(i)
    print("full_name: ",row['full_name']," fn_tokens: ",row['fn_tokens'])
    print("scorer: ",row['scorer'], " pl_tokens: ",row['pl_tokens'])
    players_df.loc[i,'token_compare'] = token_check(row['fn_tokens'], row['pl_tokens'])
    print("token_compare: ",players_df.loc[i,'token_compare'])

players_df.to_csv('player_match_token.csv')