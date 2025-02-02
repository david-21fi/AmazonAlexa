import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def barplot(data = 'data',column = 'column',rotation=False):
    fig, ax = plt.subplots(figsize=(8,6))
    counts = data[column].value_counts().sort_values()
    sns.barplot(x=counts.index,y=counts.values,)
    for i in ax.patches:
        height = i.get_height()
        plt.annotate(f'{height:.0f}', 
                    xy=(i.get_x() + i.get_width() / 2., height), 
                    xytext=(0, 3), 
                    textcoords='offset points', 
                    ha='center', 
                    va='bottom', 
                    fontsize=12)
    plt.title(rf'{column}',loc='left',)
    plt.ylabel('count')
    if rotation:
        plt.xticks(rotation=45,ha='right')
    plt.show()

