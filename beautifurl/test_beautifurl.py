import os
import re
import itertools

from collections import defaultdict

from .beautifurl import Beautifurl, get_nth_product

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
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    key = 't'
    words = beautifurl._get_dictionary(key)
    assert len(words) == 3
    # Ensure reads from cache
    beautifurl._dict_path = '/dev/null'
    words = beautifurl._get_dictionary(key)
    assert len(words) == 3

def test_get_random_url():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    url = beautifurl.get_random_url('ttt')
    assert 'Hello' in url
    assert 'World' in url
    assert 'Test' in url
    assert '\n' not in url

def test_get_random_url_key_position():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    url = beautifurl.get_random_url('abc')
    assert url == 'HelloWorldTest'

def test_count_permutations():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    perms = beautifurl.count_permutations('tat')
    assert perms == 3 * 1 * 3

def test_get_permutations():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    expected = itertools.product(['Hello', 'World', 'Test'],
                                 ['Hello'],
                                 ['Hello', 'World', 'Test'])
    expected = [''.join(x) for x in expected]
    actual = beautifurl.get_permutations('tat')
    assert is_iterator(actual)
    for (x, y) in zip(actual, expected):
        assert x == y

def test_get_permutations_shuffle():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    expected = itertools.product(['Hello', 'World', 'Test'],
                                 ['Hello'],
                                 ['Hello', 'World', 'Test'])
    expected = [''.join(x) for x in expected]
    actual = beautifurl.get_permutations('tat', shuffle=True)
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

def test_get_permutations_with_shuffle_keeps_map_order():
    test_key = 'tat'

    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    shuffled = beautifurl.get_permutations(test_key, shuffle=True)
    for url in shuffled:
        # Divide into words by capital letter
        split_url = re.findall('[A-Z][a-z]+', url)
        for (word, key) in zip(split_url, test_key):
            assert word in beautifurl._cache[key]

def test_get_permutations_with_shuffle_is_suffiently_shuffled():
    """
    Catches the case where urls are shuffled one index after the other

    e.g
    LightCalmSloth
    LightCalmFerret
    LightCalmToad
    ...
    """
    test_key = 'aaA' # Use the real dictionaries as the tests ones are too small
    min_count = 70 # If there are less than 70 unique words per position then fail

    beautifurl = Beautifurl()
    shuffled = beautifurl.get_permutations(test_key, shuffle=True)
    urls_as_lists = map(lambda x: re.findall('[A-Z][a-z]+', x), itertools.islice(shuffled, 100))
    words_by_position = defaultdict(list)
    for url in urls_as_lists:
        for (i, word) in enumerate(url):
            words_by_position[i].append(word)

    for i in range(len(test_key)): # Test dictionary in order
        count = len(set(words_by_position[i]))
        assert count > min_count

def test_get_permutations_elements_are_string():
    beautifurl = Beautifurl(dictionary_path='test/dictionaries')
    actual = beautifurl.get_permutations('tat')
    for element in actual:
        assert element.__class__ == str

def test_get_nth_product_with_three_elements():
    elements = [list(range(x + 1)) for x in range(3)]

    for (i, element) in enumerate(itertools.product(*elements)):
        assert get_nth_product(i, elements) == list(element)

def test_get_nth_product_with_four_elements():
    elements = [list(range(x + 1)) for x in range(4)]

    for (i, element) in enumerate(itertools.product(*elements)):
        assert get_nth_product(i, elements) == list(element)

def is_iterator(obj):
    # Checks if object is an iterator.  Does not return true for list.
    if hasattr(obj, 'next'):
        return True
    if hasattr(obj, '__next__'):
        return True
    return False
