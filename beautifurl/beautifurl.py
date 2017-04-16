import os

class Beautifurl:

    def __init__(self):
        dirPath = os.path.dirname(os.path.abspath(__file__))
        self._dictPath = os.path.join(dirPath, 'dictionaries')
