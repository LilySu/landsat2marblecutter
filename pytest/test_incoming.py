import sys
sys.path.insert(1, './flask/app')
import view

import pytest


def test_len_tif():
    """
    Asserts if each url parsed are the same length required to generate
    image rendering for Marblecutter.
    """
    tif_list = view.parseXML('https://landsat-pds.s3.amazonaws.com/')
    for i in range(len(tif_list)):
        assert len(tif_list[i]) == 5
