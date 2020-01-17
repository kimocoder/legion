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
from typing import NamedTuple


class HydraCommandArguments(NamedTuple):
    ipAddress: str
    port: str
    outputFile: str
    threadsToUse: str
    service: str
    verbose: bool = False
    label: str = None
    exitAfterFirstUserPassPairFound: bool = False
    loopUsers: bool = False
    tryLoginAsPass: bool = False
    tryNullPassword: bool = False
    tryPassword: str = None
    tryPasswordFile: str = None
    tryLoginName: str = None
    tryLoginNameFile: str = None


def buildHydraCommand(arguments: HydraCommandArguments) -> str:
    label = f" {arguments.label}" if arguments.label is not None else ""
    verbose = f" -V" if arguments.verbose else ""
    outputFile = f" -o \"{arguments.outputFile}\""
    exitAfterFirstUserPassPairFound = f" -f" if arguments.exitAfterFirstUserPassPairFound else ""
    loopUsers = f" -u" if arguments.loopUsers else ""
    additionalChecks = __buildAdditionalChecks(arguments)
    tryPassword = f" -p {arguments.tryPassword}" if arguments.tryPassword is not None else ""
    tryPasswordFile = f" -P \"{arguments.tryPasswordFile}\"" if arguments.tryPasswordFile is not None else ""
    tryLoginName = f" -l {arguments.tryLoginName}" if arguments.tryLoginName is not None else ""
    tryLoginNameFile = f" -L \"{arguments.tryLoginNameFile}\"" if arguments.tryLoginNameFile is not None else ""

    return f"hydra {arguments.ipAddress}" \
           f" -s {arguments.port}" \
           f"{outputFile}" \
           f"{tryLoginName}" \
           f"{tryLoginNameFile}" \
           f"{tryPassword}" \
           f"{tryPasswordFile}" \
           f"{additionalChecks}" \
           f"{loopUsers}" \
           f"{exitAfterFirstUserPassPairFound}" \
           f"{verbose}" \
           f" -t {arguments.threadsToUse}" \
           f" {arguments.service}" \
           f"{label}"


def __buildAdditionalChecks(arguments: HydraCommandArguments) -> str:
    def noAdditionalChecksArgumentsPassed():
        return not arguments.tryLoginAsPass and not arguments.tryNullPassword

    if noAdditionalChecksArgumentsPassed():
        return ""

    tryLoginAsPass = "s" if arguments.tryLoginAsPass else ""
    tryNullPassword = "n" if arguments.tryNullPassword else ""
    return f" -e {tryNullPassword}{tryLoginAsPass}"
