''' Unit test file 1'''

import unittest
import code

# Greater unit test
class greater_test(unittest.TestCase):

    def greater(self):
        data = [[Course, Student Number, Mark, Comment], [ELEN3020, 1230942, 31], [ELEN3020, 1230942, 20], [ELEN3020, 1230942, 76] ]
        low_mark = getbest.getCols(data)
        high_mark = getbest.findTop(data, num_col, mark_col)
        self.assertGreater(low_mark, high_mark, 'Not greater than ')

    def greater_than_or_equal(self):
        data = [[Course, Student Number, Mark, Comment], [ELEN3020, 1230942, 31], [ELEN3020, 1230942, 20], [ELEN3020, 1230942, 76] ]
        low_mark = getbest.getCols(data)
        high_mark = getbest.findTop(data, num_col, mark_col)
        self.assertGreaterEqual(high_mark, low_mark, 'Not greater than or equal to')

if __name__ == '__main__':
    unittest.main()
