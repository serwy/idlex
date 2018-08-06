
import sys
import os


head, tail = os.path.split(__file__)
if sys.version >= '3.6':
    sys.path.insert(0, os.path.join(head, 'idlefork'))

try:
    
    import idlelib
except ImportError:
    print("** IdleX can't import IDLE. Please install IDLE. **")
    sys.exit(1)

from .idlexMain import version as __version__
from .extensionManager import extensionManager
