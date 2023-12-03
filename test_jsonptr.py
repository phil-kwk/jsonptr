import unittest
import jsonptr


test_data = {
    "foo": ["bar", "baz"],
    "": 0,
    "a/b": 1,
    "c%d": 2,
    "e^f": 3,
    "g|h": 4,
    "i\\j": 5,
    "k\"l": 6,
    " ": 7,
    "m~n": 8
}

class Test_get(unittest.TestCase):

    def test_get_negIndex(self):
        ptrexpr = "/foo/-1"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, "baz")
    
    def test_get_negIndex2(self):
        ptrexpr = "/foo/-2"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, "bar")

    def test_get_emptyString(self):
        ptrexpr = ""
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, test_data)

    def test_get_foo(self):
        ptrexpr = "/foo"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, ["bar", "baz"])
    
    def test_get_foo0(self):
        ptrexpr = "/foo/0"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, "bar")

    def test_get_foo1(self):
        ptrexpr = "/foo/1"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, "baz")

    # def test_get_foo2(self):
    #     ptrexpr = "/foo/2"
    #     res = jsonptr.get(ptrexpr, test_data)
    #     self.assertEqual(res, "baz")
    
    def test_get_empty(self):
        ptrexpr = "/"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 0)

    def test_get_aslashb(self):
        ptrexpr = "/a~1b"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 1)

    def test_get_cmodulod(self):
        ptrexpr = "/c%d"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 2)

    def test_get_eexpf(self):
        ptrexpr = "/e^f"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 3)

    def test_get_gorh(self):
        ptrexpr = "/g|h"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 4)

    def test_get_idslashh(self):
        ptrexpr = "/i\\j"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 5)

    def test_get_hquotel(self):
        ptrexpr = "/k\"l"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 6)

    def test_get_space(self):
        ptrexpr = "/ "
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 7)

    def test_get_mtilden(self):
        ptrexpr = "/m~0n"
        res = jsonptr.get(ptrexpr, test_data)
        self.assertEqual(res, 8)

data = [
    {
        "A":[1,2,3],
        "B":{
            "C":4
        }
    },
    "D"
]

class Test_get_data(unittest.TestCase):

    def test_get(self):
        self.assertEqual(jsonptr.get('/0/A',data), [1,2,3])
        self.assertEqual(jsonptr.get('/0/A/0',data), 1)
        self.assertEqual(jsonptr.get('/0/A/1',data), 2)
        self.assertEqual(jsonptr.get('/0/A/-1',data), 3)
        self.assertEqual(jsonptr.get('/0/B/C', data), 4)
        self.assertEqual(jsonptr.get('/1', data), "D")

if __name__ == '__main__':
    unittest.main()
