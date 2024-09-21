import unittest
import test_12_1_1
import test_12_2_1

runnST = unittest.TestSuite()

runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1_1.RunnerTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2_1.TournamentTest))


testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(runnST)