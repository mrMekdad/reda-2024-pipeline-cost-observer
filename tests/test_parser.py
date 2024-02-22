import unittest
from pipeline_cost_observer.io_layer import parse_tabular


class ParserTest(unittest.TestCase):
    def test_tabular(self):
        rows = parse_tabular("sample\tstatus\nA\tready\n")
        self.assertEqual(rows[0]["sample"], "A")


if __name__ == "__main__":
    unittest.main()
