import numpy as np
import unittest
import convert_ML_formats as cmf



class TestCompress(unittest.TestCase):
    def test_numpy_to_text(self):
        a1D = np.array([1, 2, 3, 4])
        a2D = np.array([[1, 2], [3, 4]])
        a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        file1 = "./ExampleFiles/1d.txt"
        file2 = "./ExampleFiles/2d.txt"
        file3 = "./ExampleFiles/3d.txt"

        cmf.numpy_to_text(a1D, file1)
        cmf.numpy_to_text(a2D, file2)
       
    # def test_string_numpy_to_text(arr, filename, format):
    #     pass

    # 1d & 2d files
    def test_numpy_to_csv(self):
        a1D = np.array([1, 2, 3, 4])
        a2D = np.array([[1, 2], [3, 4]])
        a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        file1 = "./ExampleFiles/1d.csv"
        file2 = "./ExampleFiles/2d.csv"
        file3 = "./ExampleFiles/3d.csv"

        cmf.numpy_to_csv(a1D, file1)
        cmf.numpy_to_csv(a2D, file2)
        

    def test_numpy_to_npy(self):
        a1D = np.array([1, 2, 3, 4])
        a2D = np.array([[1, 2], [3, 4]])
        a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        file1 = "./ExampleFiles/1d.npy"
        file2 = "./ExampleFiles/2d.npy"
        file3 = "./ExampleFiles/3d.npy"

        cmf.numpy_to_npy(a1D, file1)
        cmf.numpy_to_npy(a2D, file2)
        cmf.numpy_to_npy(a3D, file3)

    def test_numpy_to_npz(self):
        a1D = np.array([1, 2, 3, 4])
        a2D = np.array([[1, 2], [3, 4]])
        a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        file1 = "./ExampleFiles/1d.npz"
        file2 = "./ExampleFiles/2d.npz"
        file3 = "./ExampleFiles/3d.npz"

        cmf.numpy_to_npz(a1D, file1)
        cmf.numpy_to_npz(a2D, file2)
        cmf.numpy_to_npz(a3D, file3)

    # def test_test_csv_to_numpy(filename):
    #     pass

    # # Data prep formats

    # def test_csv_to_hdf5():
    #     pass

    # def test_csv_to_netcdf():
    #     pass

    # def test_csv_to_json():
    #     pass

    # def test_hdf5_to_csv():
    #     pass

    # def test_hdf5_to_netcdf():
    #     pass

    # def test_hdf5_to_json():
    #     pass

    # def test_netcdf_to_csv():
    #     pass

    # def test_netcdf_to_hdf5():
    #     pass

    # def test_netcdf_to_json():
    #     pass

    # def test_json_to_csv():
    #     pass

    # def test_json_to_hdf5():
    #     pass

    # def test_json_to_netcdf():
    #     pass

    # # Training file formats

    # def test_petastorm_to_npy():
    #     pass

    # def test_petastorm_to_tfrecords():
    #     pass

    # def test_npy_to_petastorm():
    #     pass

    # def test_npy_to_tfrecords():
    #     pass

    # def test_tfrecords_to_petastorm():
    #     pass

    # def test_tfrecords_to_npy():
    #     pass


    # def test_csv_to_petastorm():
    #     pass

    # def test_csv_to_npy():
    #     pass

    # def test_csv_to_tfrecords():
    #     pass

    # def test_hdf5_to_petastorm():
    #     pass

    # def test_hdf5_to_npy():
    #     pass

    # def test_hdf5_to_tfrecords():
    #     pass

    # def test_netcdf_to_petastorm():
    #     pass

    # def test_netcdf_to_npy():
    #     pass

    # def test_netcdf_to_tfrecords():
    #     pass

    # def test_json_to_petastorm():
    #     pass

    # def test_json_to_npy():
    #     pass

    # def test_json_to_tfrecords():
    #     pass

    # # Model serving serialization formats.

    # def test_pb_to_mlmodel():
    #     pass

    # def test_pb_to_onnx():
    #     pass

    # def test_pb_to_pkl():
    #     pass

    # def test_mlmodel_to_pb():
    #     pass

    # def test_mlmodel_to_onnx():
    #     pass

    # def test_mlmodel_to_pkl():
    #     pass

    # def test_onnx_to_pb():
    #     pass

    # def test_onnx_to_mlmodel():
    #     pass

    # def test_onnx_to_pkl():
    #     pass

    # def test_pkl_to_pb():
    #     pass

    # def test_pkl_to_mlmodel():
    #     pass

    # def test_pkl_to_onnx():
    #     pass

    # # Training file formats to model serving serialization formats

    # def test_petastorm_to_pb():
    #     pass

    # def test_petastorm_to_mlmodel():
    #     pass

    # def test_petastorm_to_onnx():
    #     pass

    # def test_petastorm_to_pkl():
    #     pass

    # def test_petastorm_to_h5():
    #     pass

    # def test_petastorm_to_pmml():
    #     pass


    # def test_npy_to_pb():
    #     pass

    # def test_npy_to_mlmodel():
    #     pass

    # def test_npy_to_onnx():
    #     pass

    # def test_npy_to_pkl():
    #     pass

    # def test_npy_to_h5():
    #     pass

    # def test_npy_to_pmml():
    #     pass


    # def test_tfrecords_to_pb():
    #     pass

    # def test_tfrecords_to_mlmodel():
    #     pass

    # def test_tfrecords_to_onnx():
    #     pass

    # def test_tfrecords_to_pkl():
    #     pass

    # def test_tfrecords_to_h5():
    #     pass

    # def test_tfrecords_to_pmml():
    #     pass


    # def test_csv_to_pb():
    #     pass

    # def test_csv_to_mlmodel():
    #     pass

    # def test_csv_to_onnx():
    #     pass

    # def test_csv_to_pkl():
    #     pass

    # def test_csv_to_h5():
    #     pass

    # def test_csv_to_pmml():
    #     pass


    # def test_hdf5_to_pb():
    #     pass

    # def test_hdf5_to_mlmodel():
    #     pass

    # def test_hdf5_to_onnx():
    #     pass

    # def test_hdf5_to_pkl():
    #     pass

    # def test_hdf5_to_h5():
    #     pass

    # def test_hdf5_to_pmml():
    #     pass


    # def test_h5_to_pmml():
    #     pass

    # def test_pmml_to_h5():
    #     pass


    # def test_h5_to_pb():
    #     pass

    # def test_h5_to_mlmodel():
    #     pass

    # def test_h5_to_onnx():
    #     pass

    # def test_h5_to_pkl():
    #     pass


    # def test_pmml_to_pb():
    #     pass

    # def test_pmml_to_mlmodel():
    #     pass

    # def test_pmml_to_onnx():
    #     pass

    # def test_pmml_to_pkl():
    #     pass


    # def test_pb_to_h5():
    #     pass

    # def test_pb_to_pmml():
    #     pass

    # def test_mlmodel_to_h5():
    #     pass

    # def test_mlmodel_to_pmml():
    #     pass

    # def test_onnx_to_h5():
    #     pass

    # def test_onnx_to_pmml():
    #     pass

    # def test_pkl_to_h5():
    #     pass

    # def test_pkl_to_pmml():
    #     pass

if __name__ == '__main__':
    unittest.main()