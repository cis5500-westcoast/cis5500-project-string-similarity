# string_similarity

Program (main.py) that calculates the similarity between two strings.

## Inputs
Compares the 'fullname' column of the players_uft8.csv file with the 'scorer' column of the goalscorers_uft8.csv file.
* goalscorers_uft8.csv
* players_uft8.csv

## Outputs
Outputs the player_uft8.csv file with the 'goalscorer' column added.  This column had the highest similarity using the difflib.SequenceMatcher class.
player_match.csv

## SequenceMatcher
https://github.com/python/cpython/blob/main/Lib/difflib.py
Class SequenceMatcher:
    A flexible class for comparing pairs of sequences of any type.

## Example Matches
```
scorer,                           full_name,                          similarity
Christia  Dannemann Eriksen,      Christian  Dannemann Eriksen,       0.9818181818181818
Kalido Koulibaly,                 Kalidou Koulibaly,                  0.9696969696969697
Kylian Mbappé,                    Kylian Mbappé,                      1.0
Lionel Andrés Messi Cuccittini,   Lionel Andrés Messi Cuccittini,     1.0
Lorenzo Insigne,                  Lorenzo Insigne,                    1.0
Paul Pogb,                        Paul Pogba,                         0.9473684210526315
Virgil Dijk,                      Virgil van Dijk,                    0.8461538461538461

```