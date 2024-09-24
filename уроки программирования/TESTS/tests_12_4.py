import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(25, 10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

if __name__ == "__main__":
     unittest.main(argv=[''], exit=False)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")