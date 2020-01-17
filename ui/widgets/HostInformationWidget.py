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
from PyQt5 import QtWidgets, QtGui


# widget in which the host information is shown
class HostInformationWidget(QtWidgets.QWidget):

    def __init__(self, informationTab, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.informationTab = informationTab
        self.setupLayout()
        self.updateFields()  # set default values

    def setupLayout(self):
        self.HostStatusLabel = QtWidgets.QLabel()

        self.HostStateLabel = QtWidgets.QLabel()
        self.HostStateText = QtWidgets.QLabel()
        self.HostStateLayout = QtWidgets.QHBoxLayout()
        self.HostStateLayout.addSpacing(20)
        self.HostStateLayout.addWidget(self.HostStateLabel)
        self.HostStateLayout.addWidget(self.HostStateText)
        self.HostStateLayout.addStretch()

        self.OpenPortsLabel = QtWidgets.QLabel()
        self.OpenPortsText = QtWidgets.QLabel()
        self.OpenPortsLayout = QtWidgets.QHBoxLayout()
        self.OpenPortsLayout.addSpacing(20)
        self.OpenPortsLayout.addWidget(self.OpenPortsLabel)
        self.OpenPortsLayout.addWidget(self.OpenPortsText)
        self.OpenPortsLayout.addStretch()

        self.ClosedPortsLabel = QtWidgets.QLabel()
        self.ClosedPortsText = QtWidgets.QLabel()
        self.ClosedPortsLayout = QtWidgets.QHBoxLayout()
        self.ClosedPortsLayout.addSpacing(20)
        self.ClosedPortsLayout.addWidget(self.ClosedPortsLabel)
        self.ClosedPortsLayout.addWidget(self.ClosedPortsText)
        self.ClosedPortsLayout.addStretch()

        self.FilteredPortsLabel = QtWidgets.QLabel()
        self.FilteredPortsText = QtWidgets.QLabel()
        self.FilteredPortsLayout = QtWidgets.QHBoxLayout()
        self.FilteredPortsLayout.addSpacing(20)
        self.FilteredPortsLayout.addWidget(self.FilteredPortsLabel)
        self.FilteredPortsLayout.addWidget(self.FilteredPortsText)
        self.FilteredPortsLayout.addStretch()
        ###################
        self.AddressLabel = QtWidgets.QLabel()

        self.IP4Label = QtWidgets.QLabel()
        self.IP4Text = QtWidgets.QLabel()
        self.IP4Layout = QtWidgets.QHBoxLayout()
        self.IP4Layout.addSpacing(20)
        self.IP4Layout.addWidget(self.IP4Label)
        self.IP4Layout.addWidget(self.IP4Text)
        self.IP4Layout.addStretch()

        self.IP6Label = QtWidgets.QLabel()
        self.IP6Text = QtWidgets.QLabel()
        self.IP6Layout = QtWidgets.QHBoxLayout()
        self.IP6Layout.addSpacing(20)
        self.IP6Layout.addWidget(self.IP6Label)
        self.IP6Layout.addWidget(self.IP6Text)
        self.IP6Layout.addStretch()

        self.MacLabel = QtWidgets.QLabel()
        self.MacText = QtWidgets.QLabel()
        self.MacLayout = QtWidgets.QHBoxLayout()
        self.MacLayout.addSpacing(20)
        self.MacLayout.addWidget(self.MacLabel)
        self.MacLayout.addWidget(self.MacText)
        self.MacLayout.addStretch()

        self.AsnLabel = QtWidgets.QLabel()
        self.AsnText = QtWidgets.QLabel()
        self.AsnLayout = QtWidgets.QHBoxLayout()
        self.AsnLayout.addSpacing(20)
        self.AsnLayout.addWidget(self.AsnLabel)
        self.AsnLayout.addWidget(self.AsnText)
        self.AsnLayout.addStretch()

        self.IspLabel = QtWidgets.QLabel()
        self.IspText = QtWidgets.QLabel()
        self.IspLayout = QtWidgets.QHBoxLayout()
        self.IspLayout.addSpacing(20)
        self.IspLayout.addWidget(self.IspLabel)
        self.IspLayout.addWidget(self.IspText)
        self.IspLayout.addStretch()

        self.dummyLabel = QtWidgets.QLabel()
        self.dummyText = QtWidgets.QLabel()
        self.dummyLayout = QtWidgets.QHBoxLayout()
        self.dummyLayout.addSpacing(20)
        self.dummyLayout.addWidget(self.dummyLabel)
        self.dummyLayout.addWidget(self.dummyText)
        self.dummyLayout.addStretch()
        #########
        self.OSLabel = QtWidgets.QLabel()

        self.OSNameLabel = QtWidgets.QLabel()
        self.OSNameText = QtWidgets.QLabel()
        self.OSNameLayout = QtWidgets.QHBoxLayout()
        self.OSNameLayout.addSpacing(20)
        self.OSNameLayout.addWidget(self.OSNameLabel)
        self.OSNameLayout.addWidget(self.OSNameText)
        self.OSNameLayout.addStretch()

        self.OSAccuracyLabel = QtWidgets.QLabel()
        self.OSAccuracyText = QtWidgets.QLabel()
        self.OSAccuracyLayout = QtWidgets.QHBoxLayout()
        self.OSAccuracyLayout.addSpacing(20)
        self.OSAccuracyLayout.addWidget(self.OSAccuracyLabel)
        self.OSAccuracyLayout.addWidget(self.OSAccuracyText)
        self.OSAccuracyLayout.addStretch()

        font = QtGui.QFont('Calibri', 12)  # in each different section
        font.setBold(True)
        self.HostStatusLabel.setText('Host Status')
        self.HostStatusLabel.setFont(font)
        self.HostStateLabel.setText("State:")
        self.OpenPortsLabel.setText('Open Ports:')
        self.ClosedPortsLabel.setText('Closed Ports:')
        self.FilteredPortsLabel.setText('Filtered Ports:')
        self.AddressLabel.setText('Addresses')
        self.AddressLabel.setFont(font)
        self.IP4Label.setText('IPv4:')
        self.IP6Label.setText('IPv6:')
        self.MacLabel.setText('MAC:')
        self.AsnLabel.setText('ASN:')
        self.IspLabel.setText('ISP:')
        self.OSLabel.setText('Operating System')
        self.OSLabel.setFont(font)
        self.OSNameLabel.setText('Name:')
        self.OSAccuracyLabel.setText('Accuracy:')
        #########
        self.vlayout_1 = QtWidgets.QVBoxLayout()
        self.vlayout_2 = QtWidgets.QVBoxLayout()
        self.vlayout_3 = QtWidgets.QVBoxLayout()
        self.hlayout_1 = QtWidgets.QHBoxLayout()

        self.vlayout_1.addWidget(self.HostStatusLabel)
        self.vlayout_1.addLayout(self.HostStateLayout)
        self.vlayout_1.addLayout(self.OpenPortsLayout)
        self.vlayout_1.addLayout(self.ClosedPortsLayout)
        self.vlayout_1.addLayout(self.FilteredPortsLayout)

        self.vlayout_2.addWidget(self.AddressLabel)
        self.vlayout_2.addLayout(self.IP4Layout)
        self.vlayout_2.addLayout(self.IP6Layout)
        self.vlayout_2.addLayout(self.MacLayout)
        self.vlayout_2.addLayout(self.AsnLayout)
        self.vlayout_2.addLayout(self.IspLayout)
        self.vlayout_2.addLayout(self.dummyLayout)

        self.hlayout_1.addLayout(self.vlayout_1)
        self.hlayout_1.addSpacing(20)
        self.hlayout_1.addLayout(self.vlayout_2)

        self.vlayout_3.addWidget(self.OSLabel)
        self.vlayout_3.addLayout(self.OSNameLayout)
        self.vlayout_3.addLayout(self.OSAccuracyLayout)
        self.vlayout_3.addStretch()

        self.vlayout_4 = QtWidgets.QVBoxLayout()
        self.vlayout_4.addLayout(self.hlayout_1)
        self.vlayout_4.addSpacing(10)
        self.vlayout_4.addLayout(self.vlayout_3)

        self.hlayout_4 = QtWidgets.QHBoxLayout(self.informationTab)
        self.hlayout_4.addLayout(self.vlayout_4)
        self.hlayout_4.insertStretch(-1, 1)
        self.hlayout_4.addStretch()

    def updateFields(self, **kwargs):
        self.HostStateText.setText(kwargs.get('status') or 'unknown')
        self.OpenPortsText.setText(str(kwargs.get('openPorts') or 0))
        self.ClosedPortsText.setText(str(kwargs.get('closedPorts') or 0))
        self.FilteredPortsText.setText(str(kwargs.get('filteredPorts') or 0))
        self.IP4Text.setText(kwargs.get('ipv4') or 'unknown')
        self.IP6Text.setText(kwargs.get('ipv6') or 'unknown')
        self.MacText.setText(kwargs.get('macaddr') or 'unknown')
        self.AsnText.setText(kwargs.get('asn') or 'unknown')
        self.IspText.setText(kwargs.get('isp') or 'unknown')
        self.OSNameText.setText(kwargs.get('osMatch') or 'unknown')
        self.OSAccuracyText.setText(kwargs.get('osAccuracy') or 'unknown')