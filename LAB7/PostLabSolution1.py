import csv
import matplotlib.pyplot as plt

def load_and_clean_data(filename):
    years = []
    avg_prices = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  

        for row in reader:
            year = int(row[0])
            prices = []

            for value in row[1:]:
                try:
                    price = float(value)
                    prices.append(price)
                except ValueError:
                    continue

            if prices:
                average = sum(prices) / len(prices)
                years.append(year)
                avg_prices.append(average)

    return years, avg_prices

def plot_average_prices(years, avg_prices):
    plt.figure(figsize=(10, 6))
    plt.plot(years, avg_prices, marker='o', linestyle='-', color='b')
    plt.title('Average Bread Price per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    filename = 'breadprice.csv'
    years, avg_prices = load_and_clean_data(filename)
    plot_average_prices(years, avg_prices)

if __name__ == '__main__':
    main()
