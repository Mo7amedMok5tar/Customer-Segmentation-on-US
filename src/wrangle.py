import pandas as pd 

def wrangle(file_path):
  '''
  Read SCF data file into ``DataFrame``.

  Parameters
    ----------
    filepath : str
        Location of CSV file.
  '''
  df= pd.read_csv(file_path)

  mask = (df["TURNFEAR"] ==1) & (df["NETWORTH"]<2e6)
  df=df[mask]
  return df