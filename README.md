![IdlexX logo](idlex_logo.png)
==================================

Version 1.22 - released 2022-01-15

IdleX works with Python 3.4+.

Its website and download information can be found at: http://idlex.sourceforge.net


Installing IdleX
================

This is optional. You may run idlex.py directly without installing.

    python setup.py install --user


Running IdleX
=============

If IdleX is installed, you can launch it with:

    python -m idlexlib.launch


On Windows:
1) Extract the contents of the idlex-x.x.zip file.
2) Double-click "idlex.py" to launch IdleX.
3) Run "scripts/EditWithIdleX.py" if you want 'Edit with IdleX' in the right-click context menu.

On Linux/MacOS:
1) Open a terminal.
2) Change into the idlex directory.
3) Run: `$ python idlex.py`


Demos
=====

The "demos" directory has several .py files that detail the
functionality of some of these extensions.

Acknowledgements
================

Acknowledgements may be found in idlexlib/ACKS.txt


History
=======

IdleX started as a set of extensions in 2008, beginning with my first Python
patch: [issue2704](https://bugs.python.org/issue2704) (which is still open).
I packaged and released a set of extensions in 2011, working on top of IDLE
that shipped with Python 2.6 and 3.2.

[PEP434](https://www.python.org/dev/peps/pep-0434/) allowed for IDLE to receive
updates without the strict requirements of a standard library module.
Python 3.6 contained a patch which renamed the internals of `idlelib` (see [issue24225](https://bugs.python.org/issue24225)), which required IdleX to become a fork from the 3.5 branch.
