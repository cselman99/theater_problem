import theater
import test
import unittest
import sys

def execute_build():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
    else:
        theater.run(sys.argv[1], True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)

    print('\n======================================================================\n\n')
    theater.resetSeating()
    execute_build()

    