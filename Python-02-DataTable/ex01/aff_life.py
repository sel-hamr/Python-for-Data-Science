from load_csv import load
import matplotlib.pyplot as plt

def main():
    data = load("life_expectancy_years.csv")
    morocco_data = list(data[data["country"] == "Morocco"].values[0][1:])
    years_data = list(data.columns.values[1:])
    plt.plot(years_data, morocco_data, label='Morocco')
    plt.title('Life Expectancy in Morocco Over the Years')
    plt.xticks(years_data[::40])
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 70, 10))
    plt.xlabel('Year')
    plt.show() 

if __name__ == '__main__':
    main()