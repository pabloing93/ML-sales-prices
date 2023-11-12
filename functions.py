import pandas
import numpy
#Step 1: getting the data
#Step 2: Normalizing
#Step 3: cleaning
#Step 4: Transforming the data
#Step 5: Data split for Training

def json_to_df(data: pandas.DataFrame) -> pandas.DataFrame:
  df = pandas.DataFrame()
  for column in data.columns:
    column_normalized = pandas.json_normalize(data[column])
    df = pandas.concat([df, column_normalized], axis=1)
  return df


def clean_and_normalize(param: pandas.DataFrame) -> pandas.DataFrame:
  dataframe = param.copy()
  dataframe.drop(columns=['customerID', 'source', 'address.location.lon', 'address.location.lat'], inplace=True)
  dataframe = dataframe.astype({
    'prices.price': 'float',
    'prices.tax.iptu': 'float',
    'prices.tax.condo': 'float',
    'features.usableAreas': 'int',
    'features.totalAreas': 'int'
  })
  dataframe['prices.tax.iptu'].fillna(0, inplace=True)
  dataframe['prices.tax.condo'].fillna(0, inplace=True)
  
  return dataframe