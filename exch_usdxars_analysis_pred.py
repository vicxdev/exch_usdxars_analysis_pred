import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter
from statsmodels.tsa.arima.model import ARIMA

def main():
    url = "https://mercados.ambito.com//dolar/informal/historico-general/2000-01-27/2023-06-27"
    response = requests.get(url)

    # Convert JSON data to a Python dictionary
    json_data = json.loads(response.text)

    # Assuming your data is stored in a variable called 'data_list'
    dates = []
    buy_values = []
    sell_values = []

    for entry in json_data[1:]:
        dates.append(entry[0])
        buy_values.append(entry[1].replace(',', '.'))
        sell_values.append(entry[2].replace(',', '.'))

    # Create a DataFrame from the extracted data
    data = pd.DataFrame({'Dates': dates, 'Buy Value': buy_values, 'Sell Value': sell_values})

    # Convert the 'Dates', 'Buy Value', and 'Sell Value' columns to appropriate data types
    data['Dates'] = pd.to_datetime(data['Dates'], dayfirst=True)
    data['Buy Value'] = pd.to_numeric(data['Buy Value'])
    data['Sell Value'] = pd.to_numeric(data['Sell Value'])

    # Sort the data in ascending order by 'Dates'
    data.sort_values('Dates', inplace=True)

    # Set the 'Dates' column as the index
    data.set_index('Dates', inplace=True)

    # Visualize exchange rate trends over time
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Buy Value'], label='Buy Value')
    plt.plot(data.index, data['Sell Value'], label='Sell Value')
    plt.xlabel('Dates')
    plt.ylabel('Exchange Rate')
    plt.title('Dollar-Peso Exchange Rate Over Time')
    plt.legend()

    # Format X-axis ticks to display only the year
    years = YearLocator()
    date_formatter = DateFormatter('%Y')
    plt.gca().xaxis.set_major_locator(years)
    plt.gca().xaxis.set_major_formatter(date_formatter)

    # Set the x-axis limits to display from the first date to the last date
    plt.xlim(data.index[0], data.index[-1])

    # Format the y-axis ticks to display from 1 to Sell Value max value + 100
    plt.ylim(1, data['Sell Value'].max() + 100)
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(100))
    plt.gca().yaxis.set_major_formatter('${x:1.2f}')
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(10))

    # Save the figure as an image file
    plt.savefig('exchange_rate_plot.png')

    # Calculate average exchange rate by year
    average_exchange_rate = data.groupby(data.index.year).mean()

    # Visualize average exchange rate trends over time
    plt.figure(figsize=(12, 6))
    plt.plot(average_exchange_rate.index, average_exchange_rate['Buy Value'], label='Buy Value')
    plt.plot(average_exchange_rate.index, average_exchange_rate['Sell Value'], label='Sell Value')
    plt.xlabel('Year')
    plt.ylabel('Exchange Rate')
    plt.title('Average Dollar-Peso Exchange Rate Over Time')
    plt.legend()

    # Save the figure as an image file
    plt.savefig('average_exchange_rate_plot.png')

    # Summary statistics
    print(data.describe())

    # Correlation analysis
    correlation = data[['Buy Value', 'Sell Value']].corr()
    print(correlation)

    # Generate prediction for the next month using the updated model and changing day to 1
    next_month_date = data.index[-1].replace(day=1) + pd.DateOffset(months=1)  # Specify the next month date

    # Retrieve the last date in the dataset
    last_date = data.index[-1]

    # Calculate the number of periods between the last date and the next month date
    periods = (next_month_date.year - last_date.year) * 12 + (next_month_date.month - last_date.month)

    # Train the model with the updated data range
    model = ARIMA(data['Sell Value'], order=(1, 0, 1), trend='c')
    model_fit = model.fit()

    # Generate prediction for the next month using the updated model
    next_month_prediction = model_fit.get_forecast(steps=periods + 1).predicted_mean

    # Retrieve the predicted value for the next month
    predicted_value = next_month_prediction.values[-1]

    # Print the predicted value for the next month
    print(f"Predicted sell value for {next_month_date.strftime('%m/%Y')}: {round(predicted_value, 2)}")


if __name__ == '__main__':
    main()
