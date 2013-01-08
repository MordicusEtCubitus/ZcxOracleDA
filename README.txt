Z cxOracle DA

    This is a Zope Database Adaptor for cx_Oracle. It's currently only been
    tested with Zope 2.7 and above with cx_Oracle 4.3.1 and above.

    Installation

        You must install cx_Oracle before attempting to use this DA.

        You can find cx_Oracle at::

            http://cx-oracle.sourceforge.net/

        Then extract this product into your Zope instances Products directory.

    Connection Strings

        The connection string is passed directly to cx_Oracle.connect(). 

        The string is usually of the form username/password@TNS

    Known Issues

        cx_Oracle returns date types as python datetime.datetime types. The
        DA will check the queries description to see if any of the rows 
        being returned are of that type and if they are will convert them
        on the fly to Zopes DateTime type. Unfortunately this currently means
        the DA iterates through all the rows returned and modifies the 
        return values which is far from optimal.

        Also the DA currently doesn't handle returned datetime timezones 
        well. It currently converts all datetimes to UTC regardless of the
        timezone Oracle is using. Ideally the DA would query the current
        Oracle DBTIMEZONE and use that instead. If you want to change the
        timezone used for datetime conversion then edit db.py and modify
        CONVERSION_TIMEZONE.
        
        Bind variables are actually efficient when a ZSQL method is called
        many times in a same HTTP request.
        When the same HTTP request is called many times, no gain seems to appear
        if each ZSQL query is executed only once in the HTTP request.
        This is apparently due to an incomplete statement cache management in
        cx_Oracle library and is under investigation.

    Authors

        Andy Hird
        Ryan Hughes <ryan@linuxbox.com>
        Gael Pegliasco <gael.pegliasco@makina-corpus.com>
        Sylvain Boureliou <sylvain.boureliou@makina-corpus.com>
