
import pandas as pd

# Import CSV into Data Frame and select necessary columns

df = pd.read_csv('Batting.csv')
# df = pd.Dataframe(data)
df['1B'] = df['H'] - df['HR'] - df['3B'] - df['2B']
df['TrueHit'] = ((df['HR'] * 5) + (df['3B'] * 3) + (df['2B'] * 2) + (df['1B'] * 2) + df['BB'] -
                 df['SO']) / df['AB']
df.to_csv('Truehit.csv')

















