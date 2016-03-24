from __future__ import print_function
import os
import unittest

from airflow import configuration
from airflow.configuration import conf

configuration.test_mode()

class ConfTest(unittest.TestCase):
    def setup(self):
        configuration.test_mode()

    def test_env_var_config(self):
        opt = conf.get('testsection', 'testkey')
        self.assertEqual(opt, 'testvalue')

    def test_conf_as_dict(self):
        cfg_dict = conf.as_dict()

        # test that configs are picked up
        self.assertEqual(cfg_dict['core']['unit_test_mode'], 'True')

        # test env vars
        self.assertEqual(cfg_dict['testsection']['testkey'], '< hidden >')

        # test defaults
        conf.remove_option('core', 'load_examples')
        cfg_dict = conf.as_dict()
        self.assertEqual(cfg_dict['core']['load_examples'], 'True')

        # test display_source
        cfg_dict = conf.as_dict(display_source=True)
        self.assertEqual(cfg_dict['core']['unit_test_mode'][1], 'airflow.cfg')
        self.assertEqual(cfg_dict['core']['load_examples'][1], 'default')
        self.assertEqual(
            cfg_dict['testsection']['testkey'], ('< hidden >', 'env var'))

        # test display_sensitive
        cfg_dict = conf.as_dict(display_sensitive=True)
        self.assertEqual(cfg_dict['testsection']['testkey'], 'testvalue')

        # test display_source and display_sensitive
        cfg_dict = conf.as_dict(display_sensitive=True, display_source=True)
        self.assertEqual(
            cfg_dict['testsection']['testkey'], ('testvalue', 'env var'))
