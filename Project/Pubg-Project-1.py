'''Letsupgrade DataScience Essentials Project'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Task-1:Read the dataset
print("----Task-1----\n")
df = pd.read_csv('pubg - Dr. Darshan Ingle.csv')
print(df)
print()
#Task-2: Check the datatype of all the columns
print("-------task-2--------\n")
print(df.dtypes)
print()
#Task:3 Find the summary of all the numerical columns and write your findings about it
print("--------Task-3--------\n")
print(df.describe())
print()
#task-4: The average person kills how many players?
print("----------Task-4-----------\n")
average = df['kills'].mean()
print("\nThe average person kills :", average,"player")
print()
#Task-5: 99% of people have how many kills?
print("----------Task-5------------\n")
print("99% of people have",np.percentile(df.kills,99),"kills")
print()
#task-6: The most kills ever recorded are how much?
print("----------Task-6-----------\n")
print("\nThe most kill ever recorded are :",df.kills.max())
print()
#Task-7: Print all the columns of the dataframe
print("--------Task-7---------\n")
print(df.columns)
print()
#Task-8: Comment on distribution of the match's duration. Use seaborn.
print("-----------Task-8-----------\n")
a=sns.distplot( df['matchDuration'] )
print(a)
plt.title("Task-8")
plt.xticks(rotation=70);
plt.show()
print()
#Task-9: Comment on distribution of the walk distance. Use seaborn.
print("-----------Task-9-----------\n")
print(sns.distplot( df['walkDistance'] ))
plt.title("task-9")
plt.xticks(rotation=70);
plt.show()
print()
#Task-10: Plot distribution of the match's duration vs walk distance one below the other.
print("-----------Task-10----------\n")
plt.style.use('classic')
plt.figure()
plt.subplot(2,1,1)
plt.plot(df["matchDuration"],"+")
print(plt.xlabel("Match Duration"))
plt.subplot(2,1,2)
plt.plot(df["walkDistance"],"--")
print(plt.xlabel("Walk Distance"))
plt.title("task-10")
plt.xticks(rotation=70);
plt.show()
print()
#Task-11: Plot distribution of the match's duration vs walk distance side by side.
print("--------Task-11----------")
plt.style.use('classic')
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(df["matchDuration"])
print(plt.xlabel("Match Duration"))
plt.subplot(1,2,2)
plt.plot(df["walkDistance"])
print(plt.xlabel("Walk Distance"))
plt.title("Task-11")
plt.xticks(rotation=70);
plt.show()
#Task-12: Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups
print("----------Task-12----------")
print(sns.pairplot(df.head(500)));
plt.title("Task-12")
plt.xticks(rotation=70);
plt.show()
print("Kills and Damage dealt have linear relationship\n")
print("Kills and Damagae dealt numGroups have linear relationship")
print()
#Task-13: How many unique values are there in 'matchType' and what are their counts?
print("----------Task-13-----------")
uni = pd.unique(df['matchType'])
print("\nUnique value in matchType is :",uni)
n_uni = len(uni)
print("\nCount of unique value in matchType is :",n_uni)
print()
#Task-14: Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.
print("---------Task-14----------")
print(sns.barplot(df['matchType'],df['killPoints']));
plt.title("Task-14")
plt.xticks(rotation=70);
plt.show()
print("normal-squad-fpp and normal-squad-fpp match types has the most kill points\n",
    "solo-fpp and solo match types has the less kill points")
print()
#Task-15:Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences
print("-----------Task-15-------------")
print(sns.barplot(df['matchType'],df['weaponsAcquired']));
plt.title("task-15")
plt.xticks(rotation=70);
plt.show()
print("In crashtpp and crashfpp match types weapons acquired by players are very less\n,"
      "In normal-solo-fpp and normal-squad-fpp match types weapons acquired by players are more")
print()
#Task-16: Find the Categorical columns.
print("-------------Task-16--------------")
print(df.select_dtypes(exclude=['number']))
print()
#Task-17: Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences
print("-------------Task-17---------------")
print(sns.boxplot(x='matchType', y='winPlacePerc', data=df));
plt.title("Task-17")
plt.xticks(rotation=70);
plt.show()
print()
#Task-18: Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences.
print("-------------Task-18---------------")
print(sns.boxplot(x='matchType', y='matchDuration', data=df));
plt.title("Task-18")
plt.xticks(rotation=70);
plt.show()
#Task-19: Change the orientation of the above plot to horizontal
print("-------------Task-19---------------")
print(sns.boxplot( x='matchDuration', y='matchType',data=df));
plt.title("Task-19")
plt.xticks(rotation=70);
plt.show()
#Task-20:Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills, teamKills, roadKills.
print("-------------Task-20---------------")
df['KILL'] = df['headshotKills'] + df['teamKills'] + df['roadKills']
print(df['KILL'])
print()
#Task-21: Round off column ‘winPlacePerc’ to 2 decimals.
print("-------------Task-21---------------")
print(df['winPlacePerc'].round(decimals=2))
print()
#Task-22: Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram and comment on its distribution
print("-------------Task-22---------------")
x = []
for i in range(100):
    mean1=df['damageDealt'].sample(50).mean()
    x.append(mean1)
print("the mean of the 50 sample will:\n",x)
means = np.array(x)
print(sns.histplot(means));
plt.title("Task-22")
plt.xticks(rotation=70);
plt.show()
print("********************* THE END *************************")
