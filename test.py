import theater
import unittest

# ** TESTING ** #
class TestSeatingFunctions(unittest.TestCase):

    def test_getSeats(self):
        self.assertEqual(theater.getSeats(['R001', '3']), 'R001 J1, J2, J3\n')
        self.assertEqual(theater.getSeats(['R002', '1']), 'R002 J7\n')
        self.assertEqual(theater.getSeats(['R003', '2']), 'R003 J11, J12\n')
        self.assertEqual(theater.getSeats(['R004', '4']), 'R004 J16, J17, J18, J19\n')

    def test_getSeats2(self):
        theater.resetSeating()
        self.assertEqual(theater.getSeats(['R001', '8']), 'R001 J1, J2, J3, J4, J5, J6, J7, J8\n')
        self.assertEqual(theater.getSeats(['R002', '9']), 'R002 J12, J13, J14, J15, J16, J17, J18, J19, J20\n')
        self.assertEqual(theater.getSeats(['R003', '2']), 'R003 H1, H2\n')

    def test_getSeats3(self):
        theater.resetSeating()
        with self.assertRaises(ValueError):
            theater.getSeats(['R001'])

        with self.assertRaises(ValueError):
            theater.getSeats([' 3'])

        with self.assertRaises(ValueError):
            theater.getSeats([])

        with self.assertRaises(ValueError):
            theater.getSeats(['R001 3 4 2'])


    def test_input(self):
        # * Test generic input file
        theater.resetSeating()
        theater.run('input/requests.txt', False)

        # * Test 5 filled rows (parties of 20)
        theater.resetSeating()
        theater.run('input/requests2.txt', False)

        # * Test empty input
        theater.resetSeating()
        theater.run('input/requests3.txt', False)

        # * Test seating requests filled with parties of 1
        theater.resetSeating()
        theater.run('input/requests4.txt', False)

        # * Test incorrect formatting of input file
        theater.resetSeating()
        with self.assertRaises(ValueError):
            theater.run('input/requests5.txt', False)
        
        # * Test detection of duplicate identifiers
        theater.resetSeating()
        with self.assertRaises(ValueError):
            theater.run('input/requests6.txt', False)


if __name__ == "__main__":
    unittest.main()