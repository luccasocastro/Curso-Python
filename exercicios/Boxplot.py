import seaborn as sns

iris = sns.load_dataset("iris")
ax = sns.boxplot(x = "sepal_lenght",y = "species", data = iris)

