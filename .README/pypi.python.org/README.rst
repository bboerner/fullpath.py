.. README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)

Install
```````

:code:`[sudo] pip install fullpath`

Usage
`````

.. code:: python

	>>> from fullpath import fullpath
	
	>>> fullpath("~")

Example
```````

.. code:: python

	>>> fullpath("~")
	'/Users/username'
	
	>>> fullpath(".")
	'/path/to/current/directory'
	
	>>> fullpath("..")
	'/path/to/current'

`Examples/`_

.. _Examples/: https://github.com/russianidiot/fullpath.py/tree/master/Examples

Feedback |github_issues| |gitter| |github_follow|

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/fullpath.py.svg
	:target: https://github.com/russianidiot/fullpath.py/issues

.. |github_follow| image:: https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow
	:target: https://github.com/russianidiot

.. |gitter| image:: https://badges.gitter.im/russianidiot/fullpath.py.svg
	:target: https://gitter.im/russianidiot/fullpath.py
