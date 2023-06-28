# Exchange Dollar to Argentine Peso Analysis and Prediction

This script allows you to analyze the historical trends of the exchange rate between the US Dollar and the Argentine Peso, visualize the fluctuations over time, and make predictions for future rates using an ARIMA model.

## Installation

1. Clone the repository: `git clone https://github.com/vicxdev/exch_usdxars_analysis_pred.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the script: `python exch_usdxars_analysis_pred.py`
2. The script will fetch historical exchange rate data, visualize the trends, and provide a prediction for the next month's exchange rate.

## Output

The script generates two plots: 
- `exchange_rate_plot.png`: Shows the exchange rate trends over the entire historical period.
- `average_exchange_rate_plot.png`: Displays the average exchange rate per year.

It also provides summary statistics and correlation analysis between the buying and selling rates.

Finally, it prints the predicted exchange rate for the next month.

## Requirements

- Python 3.7 or higher
- Requests library
- Pandas library
- Matplotlib library
- Statsmodels library

## Plot examples

### exchange_rate_plot.png
![exchange_rate_plot](https://github.com/vicxdev/exch_usdxars_analysis_pred/blob/master/exchange_rate_plot.png?raw=true)

### average_exchange_rate_plot.png
![average_exchange_rate_plot](https://github.com/vicxdev/exch_usdxars_analysis_pred/blob/master/average_exchange_rate_plot.png?raw=true)
