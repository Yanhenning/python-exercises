from unittest import TestCase

from one.first_exercise import return_duplicated_items


class FirstExerciseTests(TestCase):
    def test_return_empty_list_given_an_empty_list(self):
        duplicated_items = return_duplicated_items([])

        self.assertEqual([], duplicated_items)

    def test_return_empty_list_given_an_array_without_duplicated_items(self):
        duplicated_items = return_duplicated_items(list(range(20)))

        self.assertEqual([], duplicated_items)

    def test_should_return_the_duplicated_items(self):
        duplicated_items = return_duplicated_items([1, 2, 1, 2, 3, 4])

        self.assertEqual([1, 2], duplicated_items)

    def test_return_duplicated_item_if_it_is_a_dict(self):
        a = {'a': 1}
        b = {'b': 2}

        duplicated_items = return_duplicated_items([a, b, a])

        self.assertEqual([a], duplicated_items)

    def test_return_duplicated_item_if_it_is_a_object(self):
        class foo:
            def __init__(self):
                self.a = 1
                self.b = 2

        a = {'a': 1}
        b = {'b': 2}
        c = foo()

        duplicated_items = return_duplicated_items([a, b, a])

        self.assertEqual([a], duplicated_items)
