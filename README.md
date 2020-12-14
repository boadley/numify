# Numify
Numify is a Python (2 and 3) library for converting alphanumeric characters into integers.

Numify is the opposite of Numerize (another python library, that can be found [here](https://github.com/davidsa03/numerize)).

## Installation
You can install the Numify from PyPI:

`$ pip install numify`

The library is supported on Python 2.7, as well as Python 3.4 and above.

## How to use
numify(alphanumeric_to_numify)
`
>>> from numify import numify
>>> numify('12K')
12000
>>> numify('15   k')
15000
`
This will convert the alphanumeric string '15   k' into an integer like 15000 (ignoring the spaces between).

## Example
| Command | Output |
|------|:---------:|
|`numify("1K")     `|// 1000|
|`numify("1k")     `|// 1000|
|`numify("1   K")  `|// 1000|
|`numify("1.5K)    `|// 1500|
|`numify("1M)      `|// 1000000|
|`numify("1.5m)    `|// 1500000|
|`numify("1B)      `|// 1000000000|
|`numify("1.5b)    `|// 1500000000|
|`numify("1T)      `|// 1000000000000|


## Testing
`$ python numerize/numify_test.py`

