# Numify
Numify is a Python (2 and 3) library for converting alphanumeric characters into integers.

Numify is the opposite of Numerize (another python library, that can be found here).

## Installation
You can install the Numify from PyPI:

`pip install numify`

The library is supported on Python 2.7, as well as Python 3.4 and above.

## Usage
_numify(alphanumeric_to_numify)_

## Example
`numify("1K")     `// 1000 
`numify("1k")     `// 1000
`numify("1   K")  `// 1000
`numify("1.5K)    `// 1500
`numify("1M)      `// 1000000
`numify("1.5m)    `// 1500000
`numify("1B)      `// 1000000000
`numify("1.5b)    `// 1500000000
`numify("1T)      `// 
`numify("1.5t)    `//
`numify("21.32m)  `//
`numify("21.32M)  `//


