#
# MLDB-1713-wildcard-groupby.py
# Mathieu Bolduc, 2016-08-15
# This file is part of MLDB. Copyright 2016 mldb.ai inc. All rights reserved.
#

from mldb import mldb, MldbUnitTest, ResponseException

class MLDB1713WildcardGroupby(MldbUnitTest):  # noqa

    def test_wildcard_groupby(self):
        msg = "Wildcard cannot be used with GROUP BY"
        with self.assertRaisesRegex(ResponseException, msg):
            mldb.query('select * from (select 1 as a) group by a')

if __name__ == '__main__':
    request.set_return(mldb.run_tests())
