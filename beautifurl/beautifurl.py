import os
import random

class Beautifurl:

    _cache = {}

    def __init__(self,
                dictionaryPath=None):
        if dictionaryPath is None:
            dirPath = os.path.dirname(os.path.abspath(__file__))
            self._dictPath = os.path.join(dirPath, 'dictionaries')
        else:
            self._dictPath = os.path.abspath(dictionaryPath)

    def _get_dictionary(self, key):
        if key not in self._cache:
            files = [os.path.join(self._dictPath, f) for f in os.listdir(self._dictPath)
                     if os.path.isfile(os.path.join(self._dictPath, f))]
            files = [f for f in files if os.path.basename(f)[:2] == key + '_']
            if files:
                with open (files[0], 'r') as f:
                    self._cache[key] = [s.strip() for s in f.readlines()]
            else:
                raise IOError("Unable to find dictionary in " +
                                  self._dictPath + " with key " + key)
        return self._cache[key]

    def get_random_url(self, formt):
        rng = random.Random()
        # Keep track of selected items to figure out where
        # to swap values
        selectedCounts = {}
        selected = []
        while formt:
            key, formt = formt[0], formt[1:]
            previousSelected = selectedCounts.get(key, 0)
            selectedCounts[key] = previousSelected + 1
            options = self._get_dictionary(key)
            swap = len(options) - previousSelected - 1
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
