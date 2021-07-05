from unittest import TestCase

from four.fourth_exercise import all_brackets_closed


class FourthExerciseTests(TestCase):
    def test_return_true_when_all_brackets_close(self):
        self.assertTrue(all_brackets_closed('[({})]'))

    def test_return_false_when_all_at_least_one_bracket_is_opened(self):
        self.assertFalse(all_brackets_closed('[({})'))
