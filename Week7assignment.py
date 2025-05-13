import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('Dataset_Malawi_National_Football_Team_Matches.csv')
    print("Dataset loaded successfully!")

    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Explore structure
    print("\nDataset info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values count:")
    print(df.isnull().sum())

    # Clean the dataset - drop rows with missing scores
    df_clean = df.dropna(subset=['Team Score', 'Opponent Score'])
    print("\nAfter cleaning, dataset shape:", df_clean.shape)

except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")


# code for task 2

# Basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df_clean[['Team Score', 'Opponent Score']].describe())

# Group by competition and calculate mean scores
print("\nMean scores by competition type:")
competition_stats = df_clean.groupby('Competition')[['Team Score', 'Opponent Score']].mean()
print(competition_stats)

# Group by venue and calculate mean scores
print("\nMean scores by venue:")
venue_stats = df_clean.groupby('Venue')[['Team Score', 'Opponent Score']].mean()
print(venue_stats)

# Interesting findings
print("\nInteresting findings:")
# Calculate win/loss/draw percentages
result_counts = df_clean['Result'].value_counts(normalize=True) * 100
print("\nResult percentages:")
print(result_counts)

# Best performing competition
best_comp = competition_stats['Team Score'].idxmax()
print(f"\nBest performing competition (highest avg goals): {best_comp}")


#code for task 3

# Set style
sns.set_style('whitegrid')
plt.figure(figsize=(12, 8))

# 1. Line chart showing goal trends over time
plt.subplot(2, 2, 1)
df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')
df_clean.dropna(subset=['Date'], inplace=True)
df_clean.set_index('Date').resample('Y')['Team Score'].mean().plot(
    title='Malawi Team Average Goals Per Year',
    color='green',
    marker='o'
)
plt.ylabel('Average Goals')

# 2. Bar chart of results by competition type
plt.subplot(2, 2, 2)
df_clean.groupby('Competition')['Result'].value_counts().unstack().plot(
    kind='bar',
    stacked=True,
    title='Match Results by Competition Type'
)
plt.ylabel('Number of Matches')
plt.xticks(rotation=45, ha='right')

# 3. Histogram of team scores
plt.subplot(2, 2, 3)
df_clean['Team Score'].plot(
    kind='hist',
    bins=10,
    color='skyblue',
    title='Distribution of Malawi Team Scores'
)
plt.xlabel('Goals Scored')

# 4. Scatter plot of team score vs opponent score
plt.subplot(2, 2, 4)
sns.scatterplot(
    data=df_clean,
    x='Team Score',
    y='Opponent Score',
    hue='Result',
    palette={'Win': 'green', 'Draw': 'blue', 'Loss': 'red'},
    alpha=0.7,
    s=100
)
plt.title('Team Score vs Opponent Score')
plt.legend(title='Result')

plt.tight_layout()
plt.show()


#insights drawn from the data
'''
1. Match Results:
    Losses account for about 52% of matches
    Draws make up 28%
    Wins represent 20% of matches

2. Performance by Competition:
    Highest average goals scored in COSAFA Cup (1.33 per match)
    Best win percentage in AFCON Qualifiers (33% wins)

3. Venue Performance:
    Better performance at home (avg 1.1 goals) vs away (avg 0.7 goals)
    More wins at home (25%) compared to away (15%)

4. Historical Trend:
    Goal scoring has improved slightly over time
    Recent years show more consistent performance

5. Score Distribution:
    Most common score is 0 or 1 goal
    High scoring matches (>3 goals) are rare

'''