# getfilehash

A program to get the hash of a file easily.

## Why?

This program was made for quickly checking file hashes for verifying files.

## Supported algorithms

- sha1
- sha256
- sha512
- md5

## Installation

### External dependencies

- git
- python3
- make
- sudo

### Installing

- Copy and paste this into your terminal (bash)

```bash
git clone https://github.com/Simoso68/getfilehash.git && cd getfilehash && sudo make build install && cd .. && rm -rf getfilehash
```

## Usage

```
getfilehash <hashing-algorithm> <files>
```

## Example

```
getfilehash sha256 app.py another_app.py some_script.sh my_stuff.zip
```

## License

[getfilehash](https://github.com/Simoso68/getfilehash) by [Simoso68](https://github.com/Simoso68) is licensed under the [GNU General Public License Version 3](https://gnu.org/licenses/gpl-3.0). \
Click [here](https://github.com/Simoso68/getfilehash/blob/main/LICENSE) to view the LICENSE file.