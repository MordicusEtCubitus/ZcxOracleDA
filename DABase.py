##############################################################################
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
__doc__='''Database Connection adaptor for cxOracle'''
__version__='$Revision: 0.6 $'[11:-2]

import Shared.DC.ZRDB.Connection, sys
from Globals import HTMLFile
from ImageFile import ImageFile
from ExtensionClass import Base
import Acquisition

class Connection(Shared.DC.ZRDB.Connection.Connection):
    _isAnSQLConnection=1

    manage_options=Shared.DC.ZRDB.Connection.Connection.manage_options

    info=None
        
    # No browsing for you....
    def tpValues(self):
        return []

    def __getitem__(self, name):
        raise KeyError, name

