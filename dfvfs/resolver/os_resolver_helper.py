# -*- coding: utf-8 -*-
"""The operating system path specification resolver helper implementation."""

from __future__ import unicode_literals

# This is necessary to prevent a circular import.
import dfvfs.file_io.os_file_io
import dfvfs.vfs.os_file_system

from dfvfs.lib import definitions
from dfvfs.resolver import resolver
from dfvfs.resolver import resolver_helper


class OSResolverHelper(resolver_helper.ResolverHelper):
  """Operating system resolver helper."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_OS

  def NewFileObject(self, resolver_context):
    """Creates a new file-like object.

    Args:
      resolver_context (Context): resolver context.

    Returns:
      FileIO: file-like object.
    """
    return dfvfs.file_io.os_file_io.OSFile(resolver_context)

  def NewFileSystem(self, resolver_context):
    """Creates a new file system object.

    Args:
      resolver_context (Context): resolver context.

    Returns:
      FileSystem: file system.
    """
    return dfvfs.vfs.os_file_system.OSFileSystem(resolver_context)


resolver.Resolver.RegisterHelper(OSResolverHelper())
