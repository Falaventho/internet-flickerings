from django.test import TestCase
import sys

# Create your tests here.


class TestExample(TestCase):

    def test_example(self):
        sys.stdout.write("Running example test...\n")
        assert True
