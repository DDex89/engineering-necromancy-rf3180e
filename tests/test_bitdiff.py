"""Read-only comparison tests with synthetic test data only."""
import tempfile
import unittest
from pathlib import Path
from tools.bitdiff import compare_files


class ComparisonTests(unittest.TestCase):
    def test_four_bit_demo(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / 'original.test', Path(d) / 'candidate.test'
            a.write_bytes(bytes([0, 0, 0, 0]))
            b.write_bytes(bytes([1, 2, 4, 8]))
            x = compare_files(a, b, chunk_size=3)
            self.assertEqual(x['flipped_bits'], 4)
            self.assertEqual(x['different_bytes'], 4)
            self.assertEqual(x['unpaired_bytes'], 0)

    def test_different_lengths(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / 'a.test', Path(d) / 'b.test'
            a.write_bytes(bytes([0, 1]))
            b.write_bytes(bytes([0, 1, 255]))
            x = compare_files(a, b, chunk_size=1)
            self.assertEqual(x['compared_bytes'], 2)
            self.assertEqual(x['unpaired_bytes'], 1)
            self.assertEqual(x['flipped_bits'], 0)


if __name__ == '__main__':
    unittest.main()
