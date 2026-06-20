import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print("Shape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("After Removing Duplicates:", df.duplicated().sum())
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x="type", data=df)

plt.title("Movies vs TV Shows")
plt.show()
import matplotlib.pyplot as plt

df['country'] = df['country'].fillna('Unknown')

df['country'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.savefig("top_countries.png")
plt.show()
df['release_year'].value_counts().sort_index().plot()

plt.title("Netflix Content by Release Year")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("release_year.png")
plt.show()