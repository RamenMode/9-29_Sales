import test as Arceus
import pandas as pd

SalesDataSet = pd.read_pickle('MarylandVehicleSales2002-2021') #load your pkl or use pd.read_csv #1
IndicatorDataSet = pd.read_csv('historical_country_United_States_indicator_Import_Prices.csv') #2 load ur indicator 
IndicatorDataSetDates = IndicatorDataSet['DateTime']
for x in range(0, IndicatorDataSetDates.size):
    IndicatorDataSetDates[x] = IndicatorDataSetDates[x][0:10]

IndicatorDataSet['DateTime'] = IndicatorDataSetDates
df = IndicatorDataSet.set_index('DateTime')
df1 = df.loc['2002-01-30':'2021-04-30']
df1.reset_index(drop=True, inplace = True)
IndexColumnOfIndicator = 2 #which index is your indicator columns #3
SalesColumnName = 'New' # specify your sales column. New is my sales in this case #4
TestYear = 2018 # prediction year #5
NumNodes = 153 # approx 2/3 of the number of your rows. Make this divisible by a three #6
startYear = 2002 # 7
endYear = 2021 # 8
startMonth = 1 # 9
endMonth = 4 # 10


# Message me on discord if you need help
# RamenMode#1200









Arceus.Arceus(SalesDataSet, df1, IndexColumnOfIndicator, SalesColumnName, TestYear, NumNodes, startYear, endYear, startMonth, endMonth)