
import pandas as pd
import os
from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]
raw_dir = os.path.join(project_dir, 'data', 'raw')
interim_dir = os.path.join(project_dir, 'data', 'interim')
external_data_dir = os.path.join(project_dir, 'data', 'external')
processed_data_dir = os.path.join(project_dir, 'data', 'processed')


def getWorldDate(data: pd.DataFrame):
  trade_cols = {'year': 'year',
                'location_code': 'origin',
                'hs_product_code': 'hs07',
                'export_value': 'export_val',
                'partner_code': 'dest',
                'import_value': 'import_val'}
  data = data[['year', 'location_code', 'partner_code', 'hs_product_code', 'export_value', 'import_value']].copy()

  data.location_code = data.location_code.astype(str)
  data.partner_code = data.partner_code.astype(str)
  data.hs_product_code = data.hs_product_code.astype(str)
  data.export_value = data.export_value.astype(float)
  data.year = data.year.astype(int)

  # cols_map_inv = {v: k for k, v in trade_cols.items()}
  data = data.rename(columns=trade_cols)
#    data.export_val = pd.to_numeric(data[['year', 'origin', 'hs07', 'export_val']].export_val, errors='raise')
#    data.export_val.fillna(0, inplace=True)
#    data = data.groupby(['year', 'origin', 'hs07']).export_val.sum().reset_index()
#    data[data['year'].isin(['2017'])].to_csv(os.path.join(raw_dir, 'word_export_import_2017_4_.csv'), index=None)
#    data[data['year'].isin(['2018'])].to_csv(os.path.join(raw_dir, 'word_export_import_2018_4_.csv'), index=None)
#    data[data['year'].isin(['2019'])].to_csv(os.path.join(raw_dir, 'word_export_import_2019_4_.csv'), index=None)

  data.to_csv(os.path.join(raw_dir, 'world_export_import_2017_4.csv'), index=None)
  return data


if __name__ == '__main__':

  input_file = pd.read_csv(os.path.join(raw_dir, 'country_partner_hsproduct4digit_year_2019.tab'), sep="\t", low_memory=False)
  print(input_file.head())
  result = getWorldDate(input_file)
  print('Done')
  # data = pd.read_csv(os.path.join(raw_dir, 'word_export_import_2019_4.csv'))
  # data[data['year'].isin([2017])].to_csv(os.path.join(raw_dir, 'word_export_import_2017_4_.csv'), index=None)
  # data[data['year'].isin([2018])].to_csv(os.path.join(raw_dir, 'word_export_import_2018_4_.csv'), index=None)
  # data[data['year'].isin([2019])].to_csv(os.path.join(raw_dir, 'word_export_import_2019_4_.csv'), index=None)
# новый импорт очищенный от транзита
# старый импорт не очищен от транзита
