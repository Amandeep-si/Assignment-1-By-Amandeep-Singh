'''Write the code to list all the datasets available in seaborn library.Load the 'mpg' dataset'''
import seaborn as sns
print("Datasets available in seaborn:\n",sns.get_dataset_names())
mpg=sns.load_dataset('mpg')
print("*****Dataset mpg loaded:*****\n",mpg)