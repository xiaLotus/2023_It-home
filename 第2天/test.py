import unittest

def PlusNumber(a, b):
        return a + b

class ForMyTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_ReturnMyName(self):
        name = "xia"
        self.assertIn(list(name), ['x', 'i', 'a'])
        with self.assertRaises(TypeError):
            print("check")

    def test_number_add(self):
        answer = PlusNumber(1, 3)
        self.assertEqual(answer, 4)
    
    


if __name__ == '__main':
    unittest.main()


