"""
LEGION (https://govanguard.io)
Copyright (c) 2018 GoVanguard

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
import subprocess

from app.logging.legionLog import log
from app.shell.Shell import Shell
from app.timing import timing
from app.tools.nmap.NmapExporter import NmapExporter


class DefaultNmapExporter(NmapExporter):
    def __init__(self, shell: Shell):
        self.shell = shell

    @timing
    def exportOutputToHtml(self, fileName: str, outputFolder: str) -> None:
        try:
            command = f"xsltproc -o {fileName}.html {fileName}.xml"
            p = subprocess.Popen(command, shell=True)
            p.wait()
            self.shell.move(f"{fileName}.html", outputFolder)
        except:
            log.error("nmap output export to html attempted, but failed.")
            log.error('Could not convert nmap XML to HTML. Try: apt-get install xsltproc')
