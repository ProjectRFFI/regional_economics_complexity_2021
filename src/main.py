import os
from pathlib import Path
import pandas as pd
from models.ecomplexity_model import EconomicDataModel
# import pickle as pkl
import numpy as np

project_dir = Path(__file__).resolve().parents[1]
raw_dir = os.path.join(project_dir, 'data', 'raw')
interim_dir = os.path.join(project_dir, 'data', 'interim')
external_data_dir = os.path.join(project_dir, 'data', 'external')
processed_data_dir = os.path.join(project_dir, 'data', 'processed')


if __name__ == '__main__':
    print(project_dir)
#    world_region_data = pd.read_csv(os.path.join(processed_data_dir, 'world_data_2019_.csv'),
    world_region_data = pd.read_csv(os.path.join(processed_data_dir, 'fake_tbl.csv'),
                                    low_memory=False)

    # world_region_data['year'] = 2019
    print(world_region_data.head())
    print('1 #####################################')
    processing_container = EconomicDataModel.getContrainer(world_region_data)
    print('2 #####################################')
    processing_container.rca()
    print('3 #####################################')
    processing_container.mcp()
    print('4 #####################################')
    processing_container.ubiquity()
    print('5 #####################################')
    processing_container.diversity()
    print('6 #####################################')
    processing_container.proximity()
    print('7 #####################################')
    processing_container.eci_pci()

    #  print(processing_container.mcp_data[2019])

    np.savetxt('mcc_eigen_vecs.csv', np.linalg.eig(processing_container.MCC[2019])[1], fmt='%.5f', delimiter=',')

    np.savetxt('mcc.csv', processing_container.MCC[2019], fmt='%.5f', delimiter=',')
    np.savetxt('mpp.csv', processing_container.MPP[2019], fmt='%.5f', delimiter=',')
    np.savetxt('eigen.csv', processing_container.eigen_kp[2019], fmt='%.5f', delimiter=',')
    mpp = processing_container.MPP[2019]
    mcc = processing_container.MCC[2019]
    eigenvals, eigenvec = np.linalg.eig(mcc)

    np.savetxt('mcc_eigenvec.csv', eigenvec, fmt='%.5f', delimiter=',')
    np.savetxt('mcc_eigenval.csv', eigenvals, fmt='%.5f', delimiter=',')
    np.savetxt('mpp_eigenvec.csv', np.linalg.eig(mpp)[1][1], fmt='%.5f', delimiter=',')
    np.savetxt('mpp_eigenval.csv', np.linalg.eig(mpp)[0], fmt='%.5f', delimiter=',')

    print(processing_container.eci_data)
    print(processing_container.pci_data)
    # eci_pci = processing_container.eci_pci[2019]
    # np.savetxt('eci_pci_eigenval.csv', np.linalg.eig(eci_pci)[0], fmt='%.5f', delimiter=',')

    # .to_csv('rca_data_.csv', index=None)
    np.savetxt('rca_2018.csv', processing_container.rca_data[2019], fmt='%.5f', delimiter=',')
    np.savetxt('ubiquity_2018.csv', processing_container.ubiquity_data[2019], fmt='%.5f', delimiter=',')

    # res_tbl = {}

    c_prox = processing_container.country_proximity()
    np.savetxt('country_proximity_data_.csv', processing_container.country_proximity_data[2019], fmt='%.5f', delimiter=',')
    tmp = processing_container.data[2019]\
        .insert(loc=1, column="year", value=2019)\
        .insert(loc=2, column="ubiquity", value=processing_container.ubiquity_data[2019])\
        .insert(loc=1, column="year", value=2019)

    processing_container.data[2019].to_csv("data_2.csv")
    # np.savetxt('data_.csv', tmp, fmt='%.5f', delimiter=',')

    #  with open(project_dir / 'data' / 'cprox.pkl', 'wb') as f:
    #     pkl.dump(processing_container.country_proximity_data, f)
