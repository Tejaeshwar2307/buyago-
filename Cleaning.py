import pandas as pd
import numpy as np



def cleanData(df): 
    df = df.drop('company', axis=1)
    df['agent'].fillna(0, inplace=True)
    df = df.dropna(subset=['country'])
    df['children'].fillna(0, inplace=True)
    return df
