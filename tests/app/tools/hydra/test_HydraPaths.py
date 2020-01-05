"""
LEGION (https://govanguard.io)
Copyright (c) 2020 GoVanguard

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
    version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
    details.

    You should have received a copy of the GNU General Public License along with this program.
    If not, see <http://www.gnu.org/licenses/>.

Author(s): Dmitriy Dubson (d.dubson@gmail.com)
"""

import unittest
from unittest.mock import patch

from app.tools.hydra.HydraPaths import getHydraOutputFileName


class HydraPathsTest(unittest.TestCase):
    @patch("app.timing.getTimestamp")
    def test_getHydraPathOutputFileName(self, getTimestamp):
        getTimestamp.return_value = "20200101"
        expected = "runningfolder/hydra/20200101-192.168.1.1-22-someservice.txt"
        self.assertEqual(expected, getHydraOutputFileName("runningfolder", "192.168.1.1", "22", "someservice"))
