from .beautifurl import Beautifurl

import os

def test_default_dictonary_path():
    beautifurl = Beautifurl()
    currentDir = os.path.dirname(os.path.abspath(__file__))
    expected = os.path.join(currentDir + '/dictionaries')
    print(expected)
    print(beautifurl._dictPath)
    assert beautifurl._dictPath == expected
