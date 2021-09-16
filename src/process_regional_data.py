import os
from pathlib import Path
import numpy as np
import pandas as pd


from src.models.ecomplexity_model import calc_complexity

project_dir = Path(__file__).resolve().parents[1]
raw_dir = os.path.join(str(project_dir), 'data', 'raw')
interim_dir = os.path.join(str(project_dir), 'data', 'interim')
external_data_dir = os.path.join(str(project_dir), 'data', 'external')
processed_data_dir = os.path.join(str(project_dir), 'data', 'processed')


if __name__ == '__main__':
    
    special = ''
    year = 2019
 
    world_region_data = pd.read_csv(os.path.join(processed_data_dir, str(year) + '_world_data'  + special + '.csv'),
                                    dtype={'hs07': str}, low_memory=False)
    
  
    print(world_region_data.head())
    
    cdata, prox = calc_complexity(world_region_data)
    cdata.to_csv(os.path.join(processed_data_dir, str(year) + '_world_result'  + special + '.csv'), index=None)
    prox.to_csv(os.path.join(processed_data_dir, str(year) + '_mock_proximity_matrix'  + special + '.csv'.format(year)), index=None)
    cdata.to_csv(os.path.join(processed_data_dir, '{}_cdata_wo_1507_8703.csv'.format(year )), index=None)
    prox.to_csv(os.path.join(processed_data_dir, '{}_prox_wo_1507_8703.csv'.format(year )), index=None)
