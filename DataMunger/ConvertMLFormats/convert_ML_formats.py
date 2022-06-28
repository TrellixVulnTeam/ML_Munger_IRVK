import numpy as np
import pandas as pd

# numpy files.
# 1d or 2d array
def numpy_to_text(arr, filename):
    np.savetxt(filename, arr,  delimiter=",")

def string_numpy_to_text(arr, filename, format = '%s'):
    np.savetxt(filename, arr, delimiter=",", fmt =format)

# Can store 3d arrays
def numpy_to_csv(arr, filename):
    np.savetxt(filename, arr, delimiter=",")

def numpy_to_npy(arr, filename):
    np.save(filename, arr, allow_pickle=False)

def numpy_to_npz(arr, filename):
    np.savez(filename, arr)
    pass

# Takes .npy files
def npy_to_numpy(filename):
    return np.load(filename)

def csv_to_numpy(filename):
    data = np.genfromtxt(filename, delimiter = ',' )


# Data prep formats

def csv_to_hdf5(filename):
    df = pd.DataFrame()

    pass

def csv_to_netcdf():
    pass

def csv_to_json():
    pass

def hdf5_to_csv():
    pass

def hdf5_to_netcdf():
    pass

def hdf5_to_json():
    pass

# extension is .nc
def netcdf_to_csv():
    pass

def netcdf_to_hdf5():
    pass

def netcdf_to_json():
    pass

def json_to_csv():
    pass

def json_to_hdf5():
    pass

def json_to_netcdf():
    pass

# Training file formats

def petastorm_to_npy():
    pass

def petastorm_to_tfrecords():
    pass

def npy_to_petastorm():
    pass

def npy_to_tfrecords():
    pass

def tfrecords_to_petastorm():
    pass

def tfrecords_to_npy():
    pass


def csv_to_petastorm():
    pass

def csv_to_npy():
    pass

def csv_to_tfrecords():
    pass

def hdf5_to_petastorm():
    pass

def hdf5_to_npy():
    pass

def hdf5_to_tfrecords():
    pass

def netcdf_to_petastorm():
    pass

def netcdf_to_npy():
    pass

def netcdf_to_tfrecords():
    pass

def json_to_petastorm():
    pass

def json_to_npy():
    pass

def json_to_tfrecords():
    pass

# Model serving serialization formats.

def pb_to_mlmodel():
    pass

def pb_to_onnx():
    pass

def pb_to_pkl():
    pass

def mlmodel_to_pb():
    pass

def mlmodel_to_onnx():
    pass

def mlmodel_to_pkl():
    pass

def onnx_to_pb():
    pass

def onnx_to_mlmodel():
    pass

def onnx_to_pkl():
    pass

def pkl_to_pb():
    pass

def pkl_to_mlmodel():
    pass

def pkl_to_onnx():
    pass

# Training file formats to model serving serialization formats

def petastorm_to_pb():
    pass

def petastorm_to_mlmodel():
    pass

def petastorm_to_onnx():
    pass

def petastorm_to_pkl():
    pass

def petastorm_to_h5():
    pass

def petastorm_to_pmml():
    pass


def npy_to_pb():
    pass

def npy_to_mlmodel():
    pass

def npy_to_onnx():
    pass

def npy_to_pkl():
    pass

def npy_to_h5():
    pass

def npy_to_pmml():
    pass


def tfrecords_to_pb():
    pass

def tfrecords_to_mlmodel():
    pass

def tfrecords_to_onnx():
    pass

def tfrecords_to_pkl():
    pass

def tfrecords_to_h5():
    pass

def tfrecords_to_pmml():
    pass


def csv_to_pb():
    pass

def csv_to_mlmodel():
    pass

def csv_to_onnx():
    pass

def csv_to_pkl():
    pass

def csv_to_h5():
    pass

def csv_to_pmml():
    pass


def hdf5_to_pb():
    pass

def hdf5_to_mlmodel():
    pass

def hdf5_to_onnx():
    pass

def hdf5_to_pkl():
    pass

def hdf5_to_h5():
    pass

def hdf5_to_pmml():
    pass


def h5_to_pmml():
    pass

def pmml_to_h5():
    pass


def h5_to_pb():
    pass

def h5_to_mlmodel():
    pass

def h5_to_onnx():
    pass

def h5_to_pkl():
    pass


def pmml_to_pb():
    pass

def pmml_to_mlmodel():
    pass

def pmml_to_onnx():
    pass

def pmml_to_pkl():
    pass


def pb_to_h5():
    pass

def pb_to_pmml():
    pass

def mlmodel_to_h5():
    pass

def mlmodel_to_pmml():
    pass

def onnx_to_h5():
    pass

def onnx_to_pmml():
    pass

def pkl_to_h5():
    pass

def pkl_to_pmml():
    pass