"""Test suite for historic_date module."""

import unittest
import os
from timeline import HistoricDate
from timeline import settings


INPUT_FILE = os.path.join(settings.DATA_DIR, 'test_input.txt')


class HistoricDateTest(unittest.TestCase):
    """HistoricDate test class."""

    hd = HistoricDate()

    def setUp(self) -> None:
        """Set up method."""
        self.hd = HistoricDate(1994, ['First event', 'Second event'])

    def test0_historic_date_magic_methods(self) -> None:
        """Test the historic date constructor."""
        expected_repr = "HistoricDate(1994, ['First event', 'Second event'])"
        expected_str = '1994\n*) First event\n*) Second event'

        returned_repr = repr(self.hd)
        returned_str = str(self.hd)

        self.assertEqual(expected_repr, returned_repr,
                         'Representation is different')
        self.assertEqual(expected_str, returned_str,
                         'Printable representation is different')

        def f() -> None:
            HistoricDate(year='1994')

        self.assertRaises(TypeError, f)

        def f() -> None:
            HistoricDate(event=('One event'))

        self.assertRaises(TypeError, f)

    def test1_set_get_year(self) -> None:
        """Test year setter and getter."""
        self.hd.year = 2015
        returned_value = self.hd.year

        self.assertEqual(2015, returned_value, 'Year returning is wrong')

        def f() -> None:
            self.hd.year = '2015'

        self.assertRaises(TypeError, f)

    def test2_set_get_events(self) -> None:
        """Test events setter and getter."""
        test_events = ['Third event', 'Forth event']
        self.hd.events = test_events
        returned_value = self.hd.events

        self.assertEqual(test_events, returned_value,
                         'Wrong events returned')

        def f() -> None:
            self.hd.events = ('First event', 'Second event')

        self.assertRaises(TypeError, f)

    def test3_event_amount(self) -> None:
        """Test events amount funciton."""
        returned_value = self.hd.events_amount()

        self.assertEqual(2, returned_value, 'message')
        self.assertTrue(isinstance(returned_value, int), 'message')

    def test4_add_event(self) -> None:
        """Test events addition."""
        self.hd.add_event('New event')
        returned_value = self.hd.events

        self.assertEqual(['New event'], returned_value, 'message')

        def f() -> None:
            self.hd.add_event(1994)

        self.assertRaises(TypeError, f)

    def test5_delete_event(self) -> None:
        """Test events deletion."""
        self.hd.events = ['New event']
        self.hd.delete_event('New ev')
        returned_value = self.hd.events

        self.assertEqual([], returned_value, 'message')

        def f() -> None:
            self.hd.delete_event(1994)

        self.assertRaises(TypeError, f)

    def test6_read_historic_date(self) -> None:
        """Test reading method."""
        fd = open(INPUT_FILE, 'r')
        repr_func = "HistoricDate(1900, ['Sherlock Holmes Baffled', "\
                    "'The Enchanted Drawing'])"
        null_pointer = None

        self.hd.read_historic_date(fd)
        returned_repr = repr(self.hd)

        self.assertEqual(repr_func, returned_repr, 'Wrong content')

        def f() -> None:
            self.hd.read_historic_date(null_pointer)

        self.assertRaises(TypeError, f)
