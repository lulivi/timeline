"""Global variables of tests."""

import os

TEST_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_DIRECTORY = os.path.realpath(os.path.join(TEST_DIRECTORY, 'data'))

TEST_DATA_FILE = os.path.join(TEST_DATA_DIRECTORY, 'test_input.txt')
TEST_FAIL_DATA_FILE = os.path.join(TEST_DATA_DIRECTORY, 'test_fail_input.txt')
