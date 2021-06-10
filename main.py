import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    data_url = 'Versuchspersonen.csv'
    data = pd.read_csv(data_url)

    sns.boxplot(y="Malzeit in Minuten", hue="Versuchsbedingung",x="Tage", data=data, palette='colorblind')
    plt.savefig('save.png')


if __name__ == '__main__':
    main()