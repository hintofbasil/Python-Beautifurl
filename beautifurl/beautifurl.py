import os

class Beautifurl:

    def __init__(self,
                dictionaryPath=None):
        if dictionaryPath is None:
            dirPath = os.path.dirname(os.path.abspath(__file__))
            self._dictPath = os.path.join(dirPath, 'dictionaries')
        else:
            self._dictPath = os.path.abspath(dictionaryPath)
