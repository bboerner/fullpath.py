	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/b'russianidiot'/fullpath.py.git`

pypi.python.org_: :code:`pip install fullpath`

download_: :code:`python setup.py install` or :code:`setup/.setup.py develop.command`

.. _github.com: http://github.com/b'russianidiot'/fullpath.py
.. _pypi.python.org: https://pypi.python.org/pypi/fullpath
.. _download: https://github.com/b'russianidiot'/fullpath.py/archive/master.zip

	

	

	

Usage 
'''''
.. code-block::

	from fullpath import *

	fullpath("~")
	>>> '/Users/username'

	fullpath(".")
	>>> '/path/to/current/directory'

	fullpath("..")
	>>> '/path/to/current'

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/b'russianidiot'/fullpath.py/issues`__

__ https://github.com/b'russianidiot'/fullpath.py/issues