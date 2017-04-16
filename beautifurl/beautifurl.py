import os

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
