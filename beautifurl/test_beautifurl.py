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

def test_load_dictionary_from_key():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    key = 't'
    words = beatifurl._get_dictionary(key)
    assert len(words) == 3
    # Ensure reads from cache
    beatifurl._dictPath = '/dev/null'
    words = beatifurl._get_dictionary(key)
    assert len(words) == 3

def test_get_random_url():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    url = beatifurl.get_random_url('ttt')
    assert 'hello' in url
    assert 'world' in url
    assert 'test' in url
    assert '\n' not in url

def test_get_random_url_key_position():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    url = beatifurl.get_random_url('abc')
    assert url[:5] == 'hello'
    assert url[5:10] == 'world'
    assert url[10:] == 'test'
