[![Build Status](https://drone.shadowmail.co.uk/api/badges/hintofbasil/Python-Beautifurl/status.svg)](https://drone.shadowmail.co.uk/hintofbasil/Python-Beautifurl)

# BeautifURL

## Installation

BeautifURL can be installed from pip

    pip install beautifurl

## Usage

    >>> from beautifurl import Beautifurl
    >>> beautifurl = Beautifurl()

    >>> beautifurl.get_random_url('aaA')
    'BeautifulAdventurousGiraffe'

    >>> beautifurl.count_permutations('aaA')
    9150136

    >>> for url in beautifurl.get_permutations('aaA', shuffle=True):
    ...     print(url)
    ...

    GloriousDeterminedPeafowl
    NiceSuccessfulJackal
    DepressedStupidPartridge
    StormyStrangeGiraffe
    AngryPleasantMonkey
    ...

### Url format

The examples above have a format string as their first argument.  This dictates which types of words the url should be made up of.  The examples all use `adjective adjective Animal`.  Any number or combination of keys may be used.  A full list of keys is available below.

### Custom dictionaries

The Beautifurl object `__init__` function takes an optional parameter `dictionaryPath`.  This allows the default dictionaries to be swapped for user specified dictionaries.

    >>> beautifurl = Beautifurl(dictionaryPath='~/dictionaries')

The dictionaries in this folder must be named `KEY_...` where `KEY` is a single character.  All keys should be unique.  Any characters after the underscore are ignored.  See `dictionaries` folder for examples.

## Dictionaries

| Key | Description | Size |
| --- | ----------- | ---- |
| a   | Adjectives  | 223  |
| A   | Animals     | 211  |

## Contributing

### Wordlists

Additional words and lists may be submitted in pull requests.  Please run the new lists through the organise script located in the dictionaries folder.

Please ensure you have permission to use any lists before submitting a pull request.  If a license is required please name the license file license.LIST_NAME.

    ./organise LIST_NAME [MAX_SIZE] > tmp
    mv tmp LIST_NAME

### Code

Pull requests are more than welcome.
