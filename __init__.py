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
__doc__="ZcxOracle Database Adaptor Registration."
__version__='$Revision: 0.6 $'[11:-2]

import DA
import FSORAMethod
from Products.CMFCore import utils

def initialize(context):
    context.registerClass(
        DA.Connection,
        permission = 'Add Z cxOracle Database Connections',
        constructors = (DA.manage_addZcxOracleConnectionForm,
                        DA.manage_addZcxOracleConnection),
        icon = SOFTWARE_HOME + '/Shared/DC/ZRDB/www/DBAdapterFolder_icon.gif')

    utils.registerIcon(FSORAMethod.FSORAMethod,
                       'fsoramethod.gif', globals())

