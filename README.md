# BeautifURL

## Installation

BeautifURL can be installed from pip

    pip install beautifurl

## Usage

    >>> from beautifurl import Beautifurl
    >>> beautifurl = Beautifurl()

    >>> beautifurl.get_random_url('aaA')
    'BeautifulAdventurousGiraffe'

    >>> beautifurl.get_random_url('aaA', camelCase=False)
    'foolishjoyoussquirrel'

    >>> beautifurl.count_permutations('aaA')
    10492819

    >>> for url in beautifurl.get_permutations('aaA', shuffle=True):
    ...     print(url)
    ... 
    ScaryJollyEchidna
    ScaryJollyPig
    ScaryJollyFlamingo
    ScaryJollyNewt
    ScaryJollyEmu

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

    ./organise LIST_NAME [MAX_SIZE] >> tmp
    mv tmp LIST_NAME

> There is currently a bug with the organise script which disallows writing to the read from file.  Please use a temporary file as above until this is fixed.

### Code

Pull requests are more than welcome.
