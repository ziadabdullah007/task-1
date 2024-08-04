import pandas as pd
import matplotlib.pyplot as plt


file_path = 'G:\API_SP.POP.TOTL.MA.IN_DS2_en_csv_v2_459939.csv'
population_data = pd.read_csv(file_path, skiprows=4)


print(population_data.head())

countries = ['United States', 'China', 'India', 'Brazil']
selected_data = population_data[population_data['Country Name'].isin(countries)]

selected_data.set_index('Country Name', inplace=True)

selected_data = selected_data.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])

selected_data = selected_data.transpose()

selected_data.columns = countries

plt.figure(figsize=(14, 7))
for country in countries:
    plt.plot(selected_data.index, selected_data[country], label=country)

plt.title('Population Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Population')

plt.legend()
plt.show()


