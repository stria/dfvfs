#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the VFS path specification factory object."""

import unittest

from dfvfs.lib import definitions
from dfvfs.path import factory
from tests.path import test_lib


class FactoryTest(unittest.TestCase):
  """Class to test the VFS path specification factory object."""

  def testPathSpecRegistration(self):
    """Tests the DeregisterPathSpec and DeregisterPathSpec functions."""
    # pylint: disable=protected-access
    number_of_path_spec_types = len(factory.Factory._path_spec_types)

    factory.Factory.RegisterPathSpec(test_lib.TestPathSpec)
    self.assertEqual(
        len(factory.Factory._path_spec_types),
        number_of_path_spec_types + 1)

    with self.assertRaises(KeyError):
      factory.Factory.RegisterPathSpec(test_lib.TestPathSpec)

    factory.Factory.DeregisterPathSpec(test_lib.TestPathSpec)
    self.assertEqual(
        len(factory.Factory._path_spec_types), number_of_path_spec_types)

  def testNewPathSpec(self):
    """Tests the NewPathSpec function."""
    test_path_spec = factory.Factory.NewPathSpec(
        definitions.TYPE_INDICATOR_OS, location=u'/test')

    self.assertNotEqual(test_path_spec, None)

  def testIsSystemLevelTypeIndicator(self):
    """Tests the IsSystemLevelTypeIndicator function."""
    result = factory.Factory.IsSystemLevelTypeIndicator(
        definitions.TYPE_INDICATOR_OS)
    self.assertTrue(result)

    result = factory.Factory.IsSystemLevelTypeIndicator(
        definitions.TYPE_INDICATOR_TSK)
    self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()
