#
# try_except_builtin_fct.py
# Francois-Michel L Heureux, 2016-07-11
# This file is part of MLDB. Copyright 2016 mldb.ai inc. All rights reserved.
#

if False:
    mldb_wrapper = None
from mldb import mldb, MldbUnitTest, ResponseException

class TryExceptBuiltinFct(MldbUnitTest):  # noqa

    def test_it(self):
        res = mldb.query("""
            SELECT parse_json('{"a" : 5}')
        """)
        self.assertEqual(res[1][1], 5)

        msg = 'Executing builtin function parse_json'
        with self.assertRaisesRegex(ResponseException, msg):
            res = mldb.query("""
                SELECT parse_json('coco')
            """)

        res = mldb.query("""
            SELECT try(parse_json('{"a" : 5}'), 'err')
        """)
        self.assertEqual(res[1][1], 5)

        res = mldb.query("""
            SELECT try(parse_json('coco'), 'err')
        """)
        self.assertEqual(res[1][1], 'err')

        res = mldb.query("""
            SELECT try(parse_json('coco'))
        """)
        self.assertRegex(
            res[1][1],
            "JSON passed to parse_json must be an object or an array")


if __name__ == '__main__':
    request.set_return(mldb.run_tests())
