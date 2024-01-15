import numpy as np
import pandas as pd
from functions import group_by_count
import unittest
from pandas.testing import assert_frame_equal

class TestGroupByMethods(unittest.TestCase):
    
    def test_group_by_count(self):
        res_gen = pd.DataFrame({'group':[0,1,2], 'other':['la','la','la']})
        res_gen = res_gen.groupby('group').count()
        res_gen = group_by_count(pd.DataFrame({'id':[0,0,0,2,2,1], 'grouped':['a','a','a','a','a','a']}),res_gen,'grouped','a','grouped')
        res_true = pd.DataFrame({'grouped':[3.0, 1.0, 2.0]})
        res_gen = res_gen.drop(columns = ['other'])
        assert_frame_equal(res_true, res_gen, check_dtype=False, check_names=False)
