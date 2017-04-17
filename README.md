# BeautifURL

## Installation

BeautifURL can be installed from pip

    pip install beautifurl

## Usage

    >>> from beautifurl import Beautifurl
    >>> beautifurl = Beautifurl

    >>> b.get_random_url('aaA', camelCase=True)
    'BeautifulAdventurousGiraffe'

    >>> b.count_permutations('aaA')
    10492819

    >>> for url in b.get_permutations('aaA', shuffle=True, camelCase=True):
    ...     print(url)
    ... 
    ('Annoyed', 'Worrisome', 'Curlew')
    ('Annoyed', 'Worrisome', 'Urchin')
    ('Annoyed', 'Worrisome', 'Hyena')
    ('Annoyed', 'Worrisome', 'Herring')
    ('Annoyed', 'Worrisome', 'Moose')
    ...

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
