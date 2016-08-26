<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

<p align="center">
    <b>fullpath(path) - get fullpath</b>
</p>

#### Install

`[sudo] pip install fullpath`

#### Usage

```python
>>> from fullpath import fullpath

>>> fullpath("~")
```

#### Example

```python
>>> fullpath("~")
'/Users/username'

>>> fullpath(".")
'/path/to/current/directory'

>>> fullpath("..")
'/path/to/current'
```

[Examples/](https://github.com/russianidiot/fullpath.py/tree/master/Examples)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/fullpath.py.svg)](https://github.com/russianidiot/fullpath.py/issues)
[![Join the chat at https://gitter.im/russianidiot/fullpath.py](https://badges.gitter.im/russianidiot/fullpath.py.svg)](https://gitter.im/russianidiot/fullpath.py)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)
