.. image:: https://img.shields.io/pypi/v/fullpath.svg
   :target: https://pypi.python.org/pypi/fullpath

.. image:: https://img.shields.io/pypi/pyversions/fullpath.svg
   :target: https://pypi.python.org/pypi/fullpath

.. image:: https://img.shields.io/pypi/dm/fullpath.svg
   :target: https://pypi.python.org/pypi/fullpath

	

Install
~~~~~~~

github.com_: :code:`pip install git+git://github.com/russianidiot/fullpath.py.git`

pypi.python.org_: :code:`pip install fullpath`

download_: :code:`[ -e requirements.txt ] && pip install -r requirements.txt; python setup.py install`

.. _github.com: http://github.com/russianidiot/fullpath.py
.. _pypi.python.org: https://pypi.python.org/pypi/fullpath.py
.. _download: https://github.com/russianidiot/fullpath.py/archive/master.zip

	

	

	

Usage
~~~~~

.. code-block:: python

	from fullpath import *

	>>> fullpath("~")
	'/Users/username'

	>>> fullpath(".")
	'/path/to/current/directory'

	>>> fullpath("..")
	'/path/to/current'

----

Feedback
~~~~~~~~

|github_issues| - Github Issues

.. |github_issues| image:: https://img.shields.io/github/issues/russianidiot/fullpath.py.svg
	:target: https://github.com/russianidiot/fullpath.py/issues

|gitter| - **Chat** with me (english/russian) 

.. |gitter| image:: https://badges.gitter.im/russianidiot/fullpath.py.svg
	:target: https://gitter.im/russianidiot/fullpath.py

`russianidiot.github.io/python/`_  - my Python packages

.. _russianidiot.github.io/python/: http://russianidiot.github.io/python/