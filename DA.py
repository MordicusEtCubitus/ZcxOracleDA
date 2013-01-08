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
database_type='cxOracle'
__doc__='''%s Database Connection''' % database_type
__version__='$Revision: 0.6 $'[11:-2]

from db import DB
import sys, DABase, os.path
from Globals import HTMLFile
from ImageFile import ImageFile
from ExtensionClass import Base

manage_addZcxOracleConnectionForm=HTMLFile('connectionAdd', globals())

def manage_addZcxOracleConnection(self, id, title,
                                  connection_string,
                                  check=None, REQUEST=None):
    """Add a cxOracle DB connection to a folder"""
    self._setObject(id, Connection(
	id, title, connection_string, check))
    if REQUEST is not None: return self.manage_main(self, REQUEST)

class Connection(DABase.Connection):
    " "
    database_type = database_type
    id='%s_database_connection' % database_type
    meta_type=title='Z %s Database Connection' % database_type

    manage_properties=HTMLFile('connectionEdit', globals())

    # The TM that DB inherits from doesn't have a link back to its Connection,
    # and so can't tell those above when it discovers that the connection has
    # gone down, or when it has brought the connection back up again.
    # This replacement factory returns a modified DB that has a link back to
    # the Connection.
    def _factory(self, connection):
        ret = DB(connection)
        ret._Connection = self
        return ret

    def factory(self): 
        return self._factory

classes=('DA.Connection',)

meta_types=(
    {'name':'Z %s Database Connection' % database_type,
     'action':'manage_addZ%sConnectionForm' % database_type,
     },
    )

folder_methods={
    'manage_addZcxOracleConnection':
    manage_addZcxOracleConnection,
    'manage_addZcxOracleConnectionForm':
    manage_addZcxOracleConnectionForm,
    }

__ac_permissions__=(
    ('Add Z cxOracle Database Connections',
     ('manage_addZcxOracleConnectionForm',
      'manage_addZcxOracleConnection')),
    )


misc_={
    'conn': ImageFile(
        os.path.join('Shared','DC','ZRDB','www','DBAdapterFolder_icon.gif'))}

# vim:ts=4:sts=4:sw=4:expandtab
