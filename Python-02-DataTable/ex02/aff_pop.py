from load_csv import load
import matplotlib.pyplot as plt

def main():
    data = load("population_total.csv")
    morocco_data = data[data["country"] == "France"].iloc[0,1:]
    zimbabwe_data = data[data["country"] == "Belgium"].iloc[0,1:]
    years_data = data.columns.values[1:].astype(int)
    plt.plot(years_data , morocco_data, label='Morocco')
    plt.plot(years_data, zimbabwe_data , label='canada')
    plt.title('Population Projections')
    plt.xticks(years_data[::40])
    plt.xlim(1800,2040)
    plt.ylabel('Population')
    plt.yticks(range(300, 700, 100))
    plt.xlabel('Year')
    plt.legend()
    plt.show() 

if __name__ == '__main__':
    main()