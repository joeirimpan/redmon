Redmon
======

Monitor a Redis key

Installation
------------

Redmon requires a working Redis connection.

To install Redmon from pip,

::

      pip install redmon

Or from source,

::

      python setup.py install

Setup
-----

Redmon connects to your Redis connection with the following environment
variables. If none are set, default values are used. -
REDMON\_REDIS\_HOST (default, ``localhost``) : Set it to where your
Redis is running from. - REDMON\_REDIS\_PORT (default, ``6379``) : Set
it to where your Redis is running on. - REDMON\_TIME\_INT (default,
``1.0``) : Set refresh interval for your Redis key

Get Started
-----------

To watch a Redis key, just simply

::

      >> redmon monitor -k sample
      >> * Watching 'sample' every 1.0 seconds (Press CTRL+C to quit)
      >> 18:30:08 - 5
      >> 18:30:09 - 5
      >> 18:30:10 - 5

Redmon now watches a key called ``sample`` every second.

Setting Refresh Intervals
~~~~~~~~~~~~~~~~~~~~~~~~~

Changing the refresh interval for your monitor is very simple. You can
either set it with an environment variable or by passing it as an
argument.

::

    REDMON_TIME_INT=2 redmon monitor -k sample

::

    redmon monitor -k sample -i 2

Redmon now watches a key called ``sample`` every two seconds.

**Intervals passed as arguments take precedence.**

::

    REDMON_TIME_INT=2 redmon monitor -k sample -i 3

Redmon now watches a key called ``sample`` every three seconds.

Setting expected value
~~~~~~~~~~~~~~~~~~~~~~

You can set an expected value for your monitor, and Redmon will warn you
when your key is not set to it.

::

    redmon monitor -k sample -t 6

Now, Redmon will watch ``sample`` and expect its value to be 6. If it is
not, Redmon will print its value in red.

Running Tests
-------------

Redmon uses ``pytest`` to write/run test cases. To run the test cases,

::

      cd tests
      py.test

Contributing
------------

1. `Fork <https://help.github.com/articles/fork-a-repo/>`__ this repo
2. [Clone] (https://help.github.com/articles/cloning-a-repository/) your
   newly forked repo
3. Write relevant test cases
4. Raise pull requests to
   `swaathi/redmon <https://github.com/swaathi/redmon>`__

Coming Up
---------

-  Monitor multiple keys
-  Set the values your Redis key should be compared against
