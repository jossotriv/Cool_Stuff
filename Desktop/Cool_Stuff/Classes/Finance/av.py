from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ai_key = 'S0QB41LKUI4Y2THE'
ts = TimeSeries(key=ai_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
print (data)
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()