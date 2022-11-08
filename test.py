Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
... import programm
... import algo 
... 
... class TestStringMethods(unittest.TestCase):
...     def test1(self):
...      line_1_point_start = Point (0,0)
...      line_1_point_end = Point (100,100)
... 
...      line_2_point_start = Point (0,100)
...      line_2_point_end = Point (100,0)
...      result = intersect(line_1_point_start,line_1_point_end, \
...         line_2_point_start, line_2_point_end)
...      self.assertTrue(True)
... 
...     def test2(self):
...      line_1_point_start = Point (0,0)
...      line_1_point_end = Point (100,0)
... 
...      line_2_point_start = Point (0,100)
...      line_2_point_end = Point (100,100)
...      result = intersect(line_1_point_start,line_1_point_end, \
...         line_2_point_start, line_2_point_end)
...      self.assertFalse(False)
... 
... if __name__ == '__main__':
...     # generate_data()
