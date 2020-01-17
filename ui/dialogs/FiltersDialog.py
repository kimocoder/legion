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

"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QCheckBox, QVBoxLayout, QLineEdit, QPushButton
from six import u as unicode


# dialog displayed when the user clicks on the advanced filters button
class FiltersDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupLayout()
        self.applyButton.clicked.connect(self.close)
        self.cancelButton.clicked.connect(self.close)

    def setupLayout(self):
        self.setModal(True)
        self.setWindowTitle('Filters')
        self.setFixedSize(640, 200)

        hostsBox = QGroupBox("Host Filters")
        self.hostsUp = QCheckBox("Show up hosts")
        self.hostsUp.toggle()
        self.hostsDown = QCheckBox("Show down hosts")
        self.hostsChecked = QCheckBox("Show checked hosts")
        self.hostsChecked.toggle()
        hostLayout = QVBoxLayout()
        hostLayout.addWidget(self.hostsUp)
        hostLayout.addWidget(self.hostsDown)
        hostLayout.addWidget(self.hostsChecked)
        hostsBox.setLayout(hostLayout)

        portsBox = QGroupBox("Port Filters")
        self.portsOpen = QCheckBox("Show open ports")
        self.portsOpen.toggle()
        self.portsFiltered = QCheckBox("Show filtered ports")
        self.portsClosed = QCheckBox("Show closed ports")
        self.portsTcp = QCheckBox("Show tcp")
        self.portsTcp.toggle()
        self.portsUdp = QCheckBox("Show udp")
        self.portsUdp.toggle()
        servicesLayout = QVBoxLayout()
        servicesLayout.addWidget(self.portsOpen)
        servicesLayout.addWidget(self.portsFiltered)
        servicesLayout.addWidget(self.portsClosed)
        servicesLayout.addWidget(self.portsTcp)
        servicesLayout.addWidget(self.portsUdp)
        portsBox.setLayout(servicesLayout)

        keywordSearchBox = QGroupBox("Keyword Filters")
        self.hostKeywordText = QLineEdit()
        keywordLayout = QVBoxLayout()
        keywordLayout.addWidget(self.hostKeywordText)
        keywordSearchBox.setLayout(keywordLayout)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(hostsBox)
        hlayout.addWidget(portsBox)
        hlayout.addWidget(keywordSearchBox)

        buttonLayout = QtWidgets.QHBoxLayout()
        self.applyButton = QPushButton('Apply', self)
        self.applyButton.setMaximumSize(110, 30)
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.setMaximumSize(110, 30)
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.applyButton)

        layout = QVBoxLayout()
        layout.addLayout(hlayout)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def getFilters(self):
        # return [self.hostsUp.isChecked(), self.hostsDown.isChecked(), self.hostsChecked.isChecked(),
        # self.portsOpen.isChecked(), self.portsFiltered.isChecked(), self.portsClosed.isChecked(),
        # self.portsTcp.isChecked(), self.portsUdp.isChecked(), str(self.hostKeywordText.text()).split()]
        return [self.hostsUp.isChecked(), self.hostsDown.isChecked(), self.hostsChecked.isChecked(),
                self.portsOpen.isChecked(), self.portsFiltered.isChecked(), self.portsClosed.isChecked(),
                self.portsTcp.isChecked(), self.portsUdp.isChecked(), unicode(self.hostKeywordText.text()).split()]

    def setCurrentFilters(self, filters):
        if not self.hostsUp.isChecked() == filters[0]:
            self.hostsUp.toggle()

        if not self.hostsDown.isChecked() == filters[1]:
            self.hostsDown.toggle()

        if not self.hostsChecked.isChecked() == filters[2]:
            self.hostsChecked.toggle()

        if not self.portsOpen.isChecked() == filters[3]:
            self.portsOpen.toggle()

        if not self.portsFiltered.isChecked() == filters[4]:
            self.portsFiltered.toggle()

        if not self.portsClosed.isChecked() == filters[5]:
            self.portsClosed.toggle()

        if not self.portsTcp.isChecked() == filters[6]:
            self.portsTcp.toggle()

        if not self.portsUdp.isChecked() == filters[7]:
            self.portsUdp.toggle()

        self.hostKeywordText.setText(" ".join(filters[8]))

    def setKeywords(self, keywords):
        self.hostKeywordText.setText(keywords)