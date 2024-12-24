import unittest
import tests_12_1_1
import tests_12_2_1

tests = unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1_1.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2_1.TournamentTest))

text_runner = unittest.TextTestRunner(verbosity=2)
text_runner.run(tests)
