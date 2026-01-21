import unittest
from greeter import Greeter


class TestGreeter(unittest.TestCase):

    def test_say_hello(self):
        g = Greeter("Tejashree")
        self.assertEqual(g.say_hell0(),"Hello, Tejashree")

if __name__ == "__main__":
    unittest.main()