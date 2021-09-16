import numpy as np
import pandas as pd
from ecomplexity import ecomplexity
from ecomplexity import proximity


def calc_complexity(data: pd.DataFrame):
    trade_cols = {'time': 'year', 'loc': 'origin', 'prod': 'hs07', 'val': 'export_val'}
    data = data[['origin', 'hs07', 'export_val', 'year']]
    data = data.groupby(['origin', 'hs07', 'year'])['export_val'].sum().reset_index()

    cdata = ecomplexity(data, trade_cols, continuous=True)
    prox_df = proximity(data, trade_cols, continuous=False)

    return cdata, prox_df
