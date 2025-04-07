''' Unit test file 2'''

import unittest
import code

# Equal test with message
class greater_test(unittest.TestCase):

    def start():
        self.sample_data = getbest.inputData(os.path.join(current_dir, "bestdat0.csv"))

    def equal(self):
        best = getbest.findTop(self.sample_data[0],self.sample_data[1],self.sample_data[2])
        index = getbest.findTop(self.sample_data[0],self.sample_data[1],self.sample_data[2])
        self.assertEqual(best, index)

    def not_equal(self):
        best = getbest.findTop(self.sample_data[0],self.sample_data[1],self.sample_data[2])
        index = getbest.findTop(self.sample_data[0],self.sample_data[1],self.sample_data[2])
        self.assertNotEqual(best, index)

if __name__ == '__main__':
    unittest.main()
