# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------
import logging

from taurus_engine import __version__
from nta.utils.extended_logger import ExtendedLogger



def getLogger(name=None):
  logging.setLoggerClass(logging.Logger)
  return logging.getLogger(name)



def getExtendedLogger(name=None):
  logging.setLoggerClass(ExtendedLogger)
  log = logging.getLogger(name)
  log.setLogPrefix(getStandardLogPrefix())
  return log



def getStandardLogPrefix():
  """Returns a base prefix for logging containing the version
  """
  return 'VER=%s' % (__version__)
