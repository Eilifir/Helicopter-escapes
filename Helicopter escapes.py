import pandas as pd
dict = {"Country": ["Australia", "Belgium", "Brazil", "Canada", "Chile", "France", "Greece", "Ireland", "Italy", 
                    "Mexico", "Netherlands", "Puerto Rico","Russia", " UK", "USA"], 
        "Continent": ["Oceania", "Europe", "South America", "North America", "South America", 
                      "Europe", "Europe", "Europe", "Europe", "North America", "Europe", "North America", "Europe", 
                      "Europe", "North America"],
        "Number of escapes":          [2, 4, 2, 4, 1, 15, 4, 1, 1, 1, 1, 1, 1, 2, 8], 
        "Number of succeded escapes": [1, 2, 2, 3, 1, 11, 2, 1, 1, 1, 0, 1, 1, 1, 6],
        "%. of succes":["50%", "50%", "100%", "75%", "100%", "73.33%", "50%", "100%", "100%", "100%", "0%", "100%", "100%", "50%", "85.71%"]}
brics = pd.DataFrame(dict)
print(brics)