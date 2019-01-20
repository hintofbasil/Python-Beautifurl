import os

import itertools

from .beautifurl import Beautifurl

def test_default_dictonary_path():
    beautifurl = Beautifurl()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    expected = os.path.join(current_dir + '/dictionaries')
    assert beautifurl._dict_path == expected

def test_overwrite_dictionary_path_abs():
    beautifurl = Beautifurl(dictionary_path='/fake')
    assert beautifurl._dict_path == '/fake'

def test_overwrite_dictionary_path_rel():
    beautifurl = Beautifurl(dictionary_path='fake')
    expected = os.path.abspath('fake')
    assert beautifurl._dict_path == expected
    assert beautifurl._dict_path[0] == '/'

def test_load_dictionary_from_key():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    key = 't'
    words = beatifurl._get_dictionary(key)
    assert len(words) == 3
    # Ensure reads from cache
    beatifurl._dict_path = '/dev/null'
    words = beatifurl._get_dictionary(key)
    assert len(words) == 3

def test_get_random_url():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    url = beatifurl.get_random_url('ttt')
    assert 'Hello' in url
    assert 'World' in url
    assert 'Test' in url
    assert '\n' not in url

def test_get_random_url_key_position():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    url = beatifurl.get_random_url('abc')
    assert url == 'HelloWorldTest'

def test_count_permutations():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    perms = beatifurl.count_permutations('tat')
    assert perms == 3 * 1 * 3

def test_get_permutations():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    expected = itertools.product(['Hello', 'World', 'Test'],
                                 ['Hello'],
                                 ['Hello', 'World', 'Test'])
    expected = [''.join(x) for x in expected]
    actual = beatifurl.get_permutations('tat')
    assert is_iterator(actual)
    for (x, y) in zip(actual, expected):
        assert x == y

def test_get_permutations_shuffle():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    expected = itertools.product(['Hello', 'World', 'Test'],
                                 ['Hello'],
                                 ['Hello', 'World', 'Test'])
    expected = [''.join(x) for x in expected]
    actual = beatifurl.get_permutations('tat', shuffle=True)
    assert is_iterator(actual)
    # TODO make test deterministic.
    # Can sometimes fail as shuffled list may be the same as
    # unshuffled list
    out_of_order = False
    for element in actual:
        if expected.index(element) > 0:
            out_of_order = True
        expected.remove(element)
    assert expected == []
    assert out_of_order

def test_get_permutations_elements_are_string():
    beatifurl = Beautifurl(dictionary_path='test/dictionaries')
    actual = beatifurl.get_permutations('tat')
    for element in actual:
        assert element.__class__ == str

def is_iterator(obj):
    # Checks if object is an iterator.  Does not return true for list.
    if hasattr(obj, 'next'):
        return True
    if hasattr(obj, '__next__'):
        return True
    return False
