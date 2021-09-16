import pandas as pd

IndicatorDataSet = pd.read_csv('historical_country_United_States_indicator_Inflation_Rate.csv')

print(IndicatorDataSet.iloc[2, 2])

