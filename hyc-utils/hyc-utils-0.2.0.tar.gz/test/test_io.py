import utils
import pathlib

def test_save_load(tmp_path):
    A = {'a': 'b', 'c': 'd'}
    
    # data_path = pathlib.Path('/home/hc3190/utils/test/data')
    # utils.io.save_data(data_path, A)
    
    utils.io.save_data(tmp_path, A)
    new_A = utils.io.load_data(tmp_path)
    assert A == new_A
    
def test_save_load_2(tmp_path):
    A = {'a': 'b', 'c': 'd'}
    
    # data_path = pathlib.Path('/home/hc3190/utils/test/data')
    # data_path = data_path / 'test_data.pkl'
    # utils.io.save_data(data_path, A)
    
    tmp_path = tmp_path / 'test_data.pkl'
    utils.io.save_data(tmp_path, A)
    new_A = utils.io.load_data(tmp_path)
    assert A == new_A