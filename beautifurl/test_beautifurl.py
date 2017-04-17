from .beautifurl import Beautifurl

import itertools

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

def test_count_permutations():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    perms = beatifurl.count_permutations('tat')
    assert perms == 3 * 1 * 3

def test_get_permutations():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    expected = itertools.product(['hello', 'world', 'test'],
                                 ['hello'],
                                 ['hello', 'world', 'test'])
    actual = beatifurl.get_permutations('tat')
    assert is_iterator(actual)
    for (a, e) in zip(actual, expected):
        assert a == e

def test_get_permutations_shuffle():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    expected = itertools.product(['hello', 'world', 'test'],
                                 ['hello'],
                                 ['hello', 'world', 'test'])
    expected = list(expected)
    actual = beatifurl.get_permutations('tat', shuffle=True)
    assert is_iterator(actual)
    # TODO make test deterministic.
    # Can sometimes fail as shuffled list may be the same as
    # unshuffled list
    outOfOrder = False
    for a in actual:
        if expected.index(a) > 0:
            outOfOrder = True
        expected.remove(a)
    assert expected == []
    assert outOfOrder

def test_get_random_url_camel_case():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    url = beatifurl.get_random_url('abc', camelCase=True)
    assert url[:5] == 'Hello'
    assert url[5:10] == 'World'
    assert url[10:] == 'Test'

def test_get_permutations_camel_case():
    beatifurl = Beautifurl(dictionaryPath='test/dictionaries')
    expected = itertools.product(['Hello', 'World', 'Test'],
                                 ['Hello'],
                                 ['Hello', 'World', 'Test'])
    actual = beatifurl.get_permutations('tat', camelCase=True)
    assert is_iterator(actual)
    for (a, e) in zip(actual, expected):
        assert a == e

def is_iterator(obj):
    # Checks if object is an iterator.  Does not return true for list.
    try:
        obj.next
        return True
    except AttributeError:
        pass
    try:
        obj.__next__
        return True
    except AttributeError:
        pass
    return False
