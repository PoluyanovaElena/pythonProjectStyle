from test_runner_and_tournament import TournamentTest
from test_runner import RunnerTest
import unittest

t_Suite = unittest.TestSuite()
t_Suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
t_Suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(t_Suite)