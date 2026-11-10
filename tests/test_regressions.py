import random
import unittest
from unittest.mock import patch
from Dijkstra import dijkstra
from HeapSort import minHeapSort, maxHeapSort
from Knapsack import knapsack
from MatrixProduct import matrixproduct

class RegressionTests(unittest.TestCase):
    def test_zero_cost_and_disconnected(self):
        result = dijkstra(["a", "b", "c", "d"], "a", {"a": {"b": 0}, "b": {"c": 2}, "c": {}})
        self.assertEqual(result[1], {"a": 0, "b": 0, "c": 2})

    def test_heap_sorts(self):
        rng = random.Random(5)
        for size in range(100):
            values = [rng.randrange(-100, 101) for _ in range(size)]
            self.assertEqual(minHeapSort(values[:]), sorted(values, reverse=True))
            self.assertEqual(maxHeapSort(values[:]), sorted(values))

    def test_knapsack_selection_matches_value(self):
        for seed in range(30):
            random.seed(seed)
            for capacity in range(15):
                result = knapsack(6, capacity)
                value, values, selection = result[1], result[3], result[5]
                self.assertEqual(len(selection), len(set(selection)))
                self.assertLessEqual(sum(selection), capacity)
                self.assertEqual(sum(values[item-1] for item in selection), value)
        self.assertEqual(knapsack(0, 5)[5], [])

    def test_matrix_cost_exceeds_old_sentinel(self):
        with patch("MatrixProduct.randint", return_value=49):
            self.assertEqual(matrixproduct(2)[3], 49 ** 3)
            self.assertEqual(matrixproduct(3)[3], 2 * 49 ** 3)

if __name__ == "__main__":
    unittest.main()
