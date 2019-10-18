#!/usr/bin/python3
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest as ut

from Controller import prog_input

class TestInput(ut.TestCase):
    def test_f_param(self):
        with open('input_test.txt', 'r') as f:
            f_string = f.readline().strip()
            data = prog_input.get_f_parameter(f_string)
        
        self.assertEqual(data['f_params'][1], 1)


    def test_input_from_file(self):
        with open('input_test.txt', 'r') as f:
            data = prog_input.read_from_file(f)
        
        print(data)
        self.assertEqual(data['func'], 'min')