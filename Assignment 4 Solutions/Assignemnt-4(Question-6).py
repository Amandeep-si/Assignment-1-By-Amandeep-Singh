'''Extract the part of the dataframe which contains cars belonging to "usa"'''
import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg[mpg['origin']=='usa'])
