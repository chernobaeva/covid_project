import pandas as pd

import config
from vizualization import vizualization
from get_data import get_data

url = config.url

data = get_data(url)

df = pd.DataFrame(data)

top_cases = df[['country', 'cases']].sort_values(by='cases', ascending=False).head(10)
top_cases.to_csv('top_10_countries_by_cases.csv', sep=';', index=False)

top_deaths = df[['country', 'deaths']].sort_values(by='deaths', ascending=False).head(10)
top_cases.to_csv('top_10_countries_by_deaths.csv', sep=';', index=False)

continent_cases = df.groupby('continent')['cases'].sum().reset_index().sort_values(by='cases', ascending=False)
top_cases.to_csv('top_10_continents_by_cases.csv', sep=';', index=False)

data = top_cases['cases']
categories = top_cases['country']
explode = [0.1 if i == max(data) else 0 for i in data]

plt = vizualization("Cases by Countries", data, categories)
plt.show()

data = top_deaths['deaths']
categories = top_deaths['country']
explode = [0.1 if i == max(data) else 0 for i in data]

plt = vizualization("Deaths by Countries", data, categories)
plt.show()

data = continent_cases['cases']
categories = continent_cases['continent']
explode = [0.1 if i == max(data) else 0 for i in data]

plt = vizualization("Continent", data, categories)
plt.show()
