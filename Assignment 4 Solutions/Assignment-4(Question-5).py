'''Which country origin cars are a part of this dataset?'''
import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg['origin'].unique())

