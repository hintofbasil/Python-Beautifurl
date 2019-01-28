import itertools
import operator
import os
import random

from functools import reduce

from shuffled import Shuffled

def get_nth_product(n, elements):
    """
    Get the nth product of a list without calculating any other products.
    The order is the same as itertools.product(x).

    Args:
        n: The number product to generate
        elements: The lists to generate the product from

    Returns:
        The nth product of elements
    """
    length = len(elements)
    demoninators = [reduce(operator.mul, (map(len, elements[x + 1:])), 1)
                    for x in range(length)]
    return [elements[x][(n // demoninators[x]) % len(elements[x])]
            for x in range(length)]

class Beautifurl:

    def __init__(self,
                 dictionary_path=None):
        self._cache = {}
        if dictionary_path is None:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            self._dict_path = os.path.join(dir_path, 'dictionaries')
        else:
            self._dict_path = os.path.abspath(dictionary_path)

    def _get_dictionary(self, key):
        if key not in self._cache:
            files = [os.path.join(self._dict_path, f) for f in os.listdir(self._dict_path)
                     if os.path.isfile(os.path.join(self._dict_path, f))]
            files = [f for f in files if os.path.basename(f)[:2] == key + '_']
            if files:
                with open(files[0], 'r') as input_file:
                    self._cache[key] = [s.strip() for s in input_file.readlines()]
            else:
                raise IOError("Unable to find dictionary in " +
                              self._dict_path + " with key " + key)
        return self._cache[key]

    def get_random_url(self, formt):
        """
        Generate a url based on a given format.

        Args:
            formt: The format of the url.

        Returns:
            The generated url.
        """
        rng = random.Random()
        # Keep track of selected items to figure out where
        # to swap values
        selected_counts = {}
        selected = []
        while formt:
            key, formt = formt[0], formt[1:]
            previous_selected = selected_counts.get(key, 0)
            selected_counts[key] = previous_selected + 1
            options = self._get_dictionary(key)
            swap = len(options) - previous_selected - 1
            choice = rng.randint(0, swap)
            # Add to selected
            selected.append(options[choice])
            # Swap choice with last selectable to ensure unique
            options[choice], options[swap] = options[swap], options[choice]
        return ''.join(selected)

    def count_permutations(self, formt):
        """
        Get the number of possible permutations for a given format.

        Args:
            formt: The format of the url.

        Returns:
            The number of permutations.
        """
        if not formt:
            return 0
        count = 1
        for key in formt:
            count = count * len(self._get_dictionary(key))
        return count

    def get_permutations(self, formt, shuffle=False):
        """
        Get all permutations for a given format

        Args:
            formt: The format of the url.
            shuffled (optional): Should the permutations be generated in a
                random order.  (Default: False)

        Returns:
            An iterator that yields the permutations
        """
        lists = [self._get_dictionary(x) for x in formt]
        if shuffle:
            iterator_length = self.count_permutations(formt)
            return map(
                lambda x: ''.join(get_nth_product(x, lists)),
                Shuffled(iterator_length)
            )
        return map(
            ''.join,
            itertools.product(*lists)
        )
