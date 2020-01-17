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

from app.tools.hydra.HydraCommandBuilder import HydraCommandArguments, buildHydraCommand


class HydraCommandBuilderTest(unittest.TestCase):
    def test_buildCommand_providedRequiredParameters_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -t 16 some-service"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     threadsToUse="16", service="some-service")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndOptionalLabel_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     threadsToUse="16", service="some-service", label="some-label")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndVerboseFlag_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndExitOnFirstPairFoundFlag_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True)
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndLoopUsersFlag_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -u -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True)
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTryLoginAsPassFlag_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -e s -u -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True)
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTryNullPassFlag_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -e ns -u -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True,
                                     tryNullPassword=True)
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTrySpecificPass_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -p somepass -e ns -u -f -V -t 16 " \
                   "some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True,
                                     tryNullPassword=True, tryPassword="somepass")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTrySpecificPassFile_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -P \"passwords.txt\" -e ns -u -f -V -t 16 " \
                   "some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True,
                                     tryNullPassword=True, tryPasswordFile="passwords.txt")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTrySpecificLogin_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -l someusername -P \"passwords.txt\" -e ns " \
                   "-u -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True,
                                     tryNullPassword=True, tryPasswordFile="passwords.txt", tryLoginName="someusername")
        self.assertEqual(expected, buildHydraCommand(args))

    def test_buildCommand_providedRequiredParametersAndTrySpecificLoginFile_buildsAValidHydraCommand(self):
        expected = "hydra 127.0.0.1 -s 22 -o \"some-path/some-file.txt\" -L \"someuser.txt\" -P \"passwords.txt\" " \
                   "-e ns -u -f -V -t 16 some-service some-label"

        args = HydraCommandArguments(ipAddress="127.0.0.1", port="22", outputFile="some-path/some-file.txt",
                                     verbose=True, threadsToUse="16", service="some-service", label="some-label",
                                     exitAfterFirstUserPassPairFound=True, loopUsers=True, tryLoginAsPass=True,
                                     tryNullPassword=True, tryPasswordFile="passwords.txt",
                                     tryLoginNameFile="someuser.txt")
        self.assertEqual(expected, buildHydraCommand(args))
