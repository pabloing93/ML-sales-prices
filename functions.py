import pandas
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