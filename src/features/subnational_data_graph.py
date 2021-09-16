# aux script for data forming


import numpy as np
import pandas as pd
import tqdm
import os
from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]
raw_dir = os.path.join(project_dir, 'data', 'raw')
interim_dir = os.path.join(project_dir, 'data', 'interim')
external_data_dir = os.path.join(project_dir, 'data', 'external')
processed_data_dir = os.path.join(project_dir, 'data', 'processed')


def merge_regional_data(world_data: pd.DataFrame,
                        region_foreign_export: pd.DataFrame,
                        region_foreign_import: pd.DataFrame,
                        region_domestic_export: pd.DataFrame,
                        region_domestic_import: pd.DataFrame,
                        base_country_name: str, verbose=1):
    world_data = world_data.drop('import_val', axis=1)

    if verbose > 0:
        data_rows = tqdm.tqdm(world_data.iterrows())
    else:
        data_rows = world_data.iterrows()

    for idx, row in data_rows:

        if row.origin != base_country_name and row.dest != base_country_name:
            continue
        if np.sum(region_foreign_export.hs07 == row.hs07) == 0:
            continue
        if row.origin == base_country_name:
            region_hs_export = region_foreign_export[region_foreign_export.dest == row.dest]
            if len(region_hs_export) > 0:
                row.export_val -= region_hs_export.export_val.values[0]
            continue

        if row.dest == base_country_name:
            region_hs_import = region_foreign_import[region_foreign_import.origin == row.origin]
            if len(region_hs_import) > 0:
                row.export_val -= region_hs_import.export_val.values[0]

    world_data_with_region = world_data\
        .append(region_foreign_import, sort=False)\
        .append(region_foreign_export, sort=False)\
        .append(region_domestic_export, sort=False)\
        .append(region_domestic_import, sort=False)

    print(world_data_with_region.head())
    return world_data_with_region


if __name__ == '__main__':
    
    special = ''
    year = 2019
    
    main_data = pd.read_csv(os.path.join(raw_dir, 'world_export_import_2019_4.csv'), low_memory=False)
    main_data['year'] = 2019
#    main_data = pd.read_csv(os.path.join(raw_dir, 'world_export_import_'+str(year)+'_4'  + special + '.csv'), low_memory=False)  
    region_foreign_export = pd.read_csv(os.path.join(interim_dir, str(year) + '_region_foreign_export'  + special + '.csv'))
    region_foreign_import = pd.read_csv(os.path.join(interim_dir, str(year) + '_region_foreign_import'  + special + '.csv'))
    region_domestic_export = pd.read_csv(os.path.join(interim_dir, str(year) + '_region_domestic_export'  + special + '.csv'))
    region_domestic_import = pd.read_csv(os.path.join(interim_dir, str(year) + '_region_domestic_import'  + special + '.csv'))
    
    
    special = ''
    
    
    print(main_data.head())
    modified_world_data = merge_regional_data(main_data,
                                              region_foreign_export,
                                              region_foreign_import,
                                              region_domestic_export,
                                              region_domestic_import,
                                              'RUS', 1)
    modified_world_data .to_csv(os.path.join(processed_data_dir, str(year) + '_world_data'  + special + '.csv'), index=None)
