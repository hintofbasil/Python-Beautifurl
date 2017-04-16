from .beautifurl import Beautifurl

import os

def test_default_dictonary_path():
    beautifurl = Beautifurl()
    currentDir = os.path.dirname(os.path.abspath(__file__))
    expected = os.path.join(currentDir + '/dictionaries')
    print(expected)
    print(beautifurl._dictPath)
    assert beautifurl._dictPath == expected

def test_overwrite_dictionary_path_abs():
    beautifurl = Beautifurl(dictionaryPath='/fake')
    assert beautifurl._dictPath == '/fake'

def test_overwrite_dictionary_path_rel():
    beautifurl = Beautifurl(dictionaryPath='fake')
    expected = os.path.abspath('fake')
    assert beautifurl._dictPath == expected
    assert beautifurl._dictPath[0] == '/'
