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
            return str(self._elem)

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
                element_list.pop()
                if (len(element_list) > 0 and element_list[-1]._elem == elem):
                    element_list[-1]._count += 1
                else:
                    element_list.append(Element(elem))
            else:
                element_list.append(Element(elem))

    # this check is needed in order to remove last element in case there is no
    # different element in the end.
    if len(element_list) > 0 and element_list[-1]._count >= 3:
        element_list.pop()

    return [str(element) for element in element_list]


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

    def test_fourth_case(self):
        self.assertListEqual(solver(
            ["A", "B", "B", "C", "C", "C", "B", "B"]), ["A"])


if __name__ == "__main__":
    unittest.main()
