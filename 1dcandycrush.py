"""
Solution for 1D Candy Crush challenge.

Task:
Remove adjacent elements if they have same value and there is 3 or more of them

Example:
Input -> Output
A B C C C D -> A B D
A B B C C C B D -> A D
A B B C C C B B D -> A D
"""
from typing import List
import unittest


def solver(input_list: List[str]) -> List[str]:

    class Element():
        def __init__(self, elem):
            self._elem = elem
            self._count = 1

        def __str__(self):
            return f"{self._elem}:{self._count}"

    element_list: List[Element] = []

    # Algorithm:
    # Iterate over list and check last element in element_list. If current
    # element is same as last element in element_list then increment element's
    # counter. Check next elements if element is same as previous one.
    # When elements differ, then check last elements counter and if counter is
    # equal or bigger than 3 then delete elements.

    for elem in input_list:
        if (len(element_list) > 0 and element_list[-1]._elem == elem):
            element_list[-1]._count += 1
        else:
            if (len(element_list) > 0 and element_list[-1]._count >= 3):
                # delete elements
                pass
            else:
                element_list.append(Element(elem))

    print(element_list)

    return [element._elem for element in element_list]


class Test1DCandyCrushSolver(unittest.TestCase):

    def test_first_case(self):
        self.assertListEqual(solver(["A", "B", "C", "C", "C", "D"]),
                                    ["A", "B", "D"])

    def test_second_case(self):
        self.assertListEqual(solver(["A", "B", "B", "C", "C", "C", "B", "D"]),
                                    ["A", "D"])

    def test_third_case(self):
        self.assertListEqual(solver(
            ["A", "B", "B", "C", "C", "C", "B", "B", "D"]), ["A", "D"])


if __name__ == "__main__":
    unittest.main()
