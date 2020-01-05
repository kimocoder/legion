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
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QRadioButton, QVBoxLayout, QPlainTextEdit, \
    QHBoxLayout, QFileDialog, QCheckBox, QComboBox, QButtonGroup

from app.timing import getTimestamp
from app.tools.hydra.HydraCommandBuilder import HydraCommandArguments, buildHydraCommand
from app.tools.hydra.HydraPaths import getHydraOutputFileName


class BruteWidget(QWidget):
    def __init__(self, ip, port, service, settings, parent=None):
        QWidget.__init__(self, parent)
        self.ip = ip
        self.port = port
        self.service = service

        ##
        # self.hydraServices = hydraServices
        # self.hydraNoUsernameServices = hydraNoUsernameServices
        # self.hydraNoPasswordServices = hydraNoPasswordServices
        # self.bruteSettings = bruteSettings
        # self.generalSettings = generalSettings
        ##

        self.settings = settings
        self.pid = -1  # will store hydra's pid so we can kill it
        self.setupLayout()

        self.browseUsersButton.clicked.connect(lambda: self.wordlistDialog())
        self.browsePasswordsButton.clicked.connect(lambda: self.wordlistDialog('Choose password list'))
        self.usersTextinput.textEdited.connect(self.singleUserRadio.toggle)
        self.passwordsTextinput.textEdited.connect(self.singlePassRadio.toggle)
        self.userlistTextinput.textEdited.connect(self.userListRadio.toggle)
        self.passlistTextinput.textEdited.connect(self.passListRadio.toggle)
        self.checkAddMoreOptions.stateChanged.connect(self.showMoreOptions)

    def setupLayoutHlayout(self):
        hydraServiceConversion = {'login': 'rlogin', 'ms-sql-s': 'mssql', 'ms-wbt-server': 'rdp',
                                  'netbios-ssn': 'smb', 'netbios-ns': 'smb', 'microsoft-ds': 'smb',
                                  'postgresql': 'postgres', 'vmware-auth': 'vmauthd"'}
        # sometimes nmap service name is different from hydra service name
        if self.service is None:
            self.service = ''
        elif str(self.service) in hydraServiceConversion:
            self.service = hydraServiceConversion.get(str(self.service))

        self.label1 = QLabel()
        self.label1.setText('IP')
        self.label1.setAlignment(Qt.AlignLeft)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.ipTextinput = QLineEdit()
        self.ipTextinput.setText(str(self.ip))
        self.ipTextinput.setFixedWidth(125)

        self.label2 = QLabel()
        self.label2.setText('Port')
        self.label2.setAlignment(Qt.AlignLeft)
        self.label2.setAlignment(Qt.AlignVCenter)
        self.portTextinput = QLineEdit()
        self.portTextinput.setText(str(self.port))
        self.portTextinput.setFixedWidth(60)

        self.label3 = QLabel()
        self.label3.setText('Service')
        self.label3.setAlignment(Qt.AlignLeft)
        self.label3.setAlignment(Qt.AlignVCenter)
        self.serviceComboBox = QComboBox()
        self.serviceComboBox.insertItems(0, self.settings.brute_services.split(","))
        self.serviceComboBox.setStyleSheet("QComboBox { combobox-popup: 0; }");
        self.serviceComboBox.currentIndexChanged.connect(self.checkSelectedService)

        # autoselect service from combo box
        for i in range(len(self.settings.brute_services.split(","))):
            if str(self.service) in self.settings.brute_services.split(",")[i]:
                self.serviceComboBox.setCurrentIndex(i)
                break

        #       self.labelPath = QLineEdit()  # this is the extra input field to insert the path to brute force
        #       self.labelPath.setFixedWidth(800)
        #       self.labelPath.setText('/')

        self.runButton = QPushButton('Run')
        self.runButton.setMaximumSize(110, 30)
        self.runButton.setDefault(True)  # new

        ###
        self.validationLabel = QLabel(self)
        self.validationLabel.setText('Invalid input. Please try again!')
        self.validationLabel.setStyleSheet('QLabel { color: red }')
        ###

        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.label1)
        self.hlayout.addWidget(self.ipTextinput)
        self.hlayout.addWidget(self.label2)
        self.hlayout.addWidget(self.portTextinput)
        self.hlayout.addWidget(self.label3)
        self.hlayout.addWidget(self.serviceComboBox)
        self.hlayout.addWidget(self.runButton)
        ###
        self.hlayout.addWidget(self.validationLabel)
        self.validationLabel.hide()
        ###
        self.hlayout.addStretch()

        return self.hlayout

    def setupLayoutHlayout2(self):
        self.singleUserRadio = QRadioButton()
        self.label4 = QLabel()
        self.label4.setText('Username')
        self.label4.setFixedWidth(70)
        self.usersTextinput = QLineEdit()
        self.usersTextinput.setFixedWidth(125)
        self.usersTextinput.setText(self.settings.brute_default_username)
        self.userListRadio = QRadioButton()
        self.label5 = QLabel()
        self.label5.setText('Username list')
        self.label5.setFixedWidth(90)
        self.userlistTextinput = QLineEdit()
        self.userlistTextinput.setFixedWidth(125)
        self.browseUsersButton = QPushButton('Browse')
        self.browseUsersButton.setMaximumSize(80, 30)

        self.foundUsersRadio = QRadioButton()
        self.label9 = QLabel()
        self.label9.setText('Found usernames')
        self.label9.setFixedWidth(117)

        self.userGroup = QButtonGroup()
        self.userGroup.addButton(self.singleUserRadio)
        self.userGroup.addButton(self.userListRadio)
        self.userGroup.addButton(self.foundUsersRadio)
        self.foundUsersRadio.toggle()

        self.warningLabel = QLabel()
        self.warningLabel.setText('*Note: when using form-based services from the Service menu, ' +
                                  'select the "Additional Options" checkbox and add the proper arguments' +
                                  ' for the webpage form. See Hydra documentation for extra help when' +
                                  ' targeting HTTP/HTTPS forms.')
        self.warningLabel.setWordWrap(True)
        self.warningLabel.setAlignment(Qt.AlignRight)
        self.warningLabel.setStyleSheet('QLabel { color: red }')

        self.hlayout2 = QHBoxLayout()
        self.hlayout2.addWidget(self.singleUserRadio)
        self.hlayout2.addWidget(self.label4)
        self.hlayout2.addWidget(self.usersTextinput)
        self.hlayout2.addWidget(self.userListRadio)
        self.hlayout2.addWidget(self.label5)
        self.hlayout2.addWidget(self.userlistTextinput)
        self.hlayout2.addWidget(self.browseUsersButton)
        self.hlayout2.addWidget(self.foundUsersRadio)
        self.hlayout2.addWidget(self.label9)
        self.hlayout2.addWidget(self.warningLabel)
        self.warningLabel.hide()
        self.hlayout2.addStretch()

        return self.hlayout2

    def checkSelectedService(self):
        self.service = str(self.serviceComboBox.currentText())
        if 'form' in str(self.service):
            self.warningLabel.show()
        # else: This clause would produce an interesting logic error and crash
        # self.warningLabel.hide()

    def setupLayoutHlayout3(self):
        # add usernames wordlist
        self.singlePassRadio = QRadioButton()
        self.label6 = QLabel()
        self.label6.setText('Password')
        self.label6.setFixedWidth(70)
        self.passwordsTextinput = QLineEdit()
        self.passwordsTextinput.setFixedWidth(125)
        self.passwordsTextinput.setText(self.settings.brute_default_password)
        self.passListRadio = QRadioButton()
        self.label7 = QLabel()
        self.label7.setText('Password list')
        self.label7.setFixedWidth(90)
        self.passlistTextinput = QLineEdit()
        self.passlistTextinput.setFixedWidth(125)
        self.browsePasswordsButton = QPushButton('Browse')
        self.browsePasswordsButton.setMaximumSize(80, 30)

        self.foundPasswordsRadio = QRadioButton()
        self.label10 = QLabel()
        self.label10.setText('Found passwords')
        self.label10.setFixedWidth(115)

        self.passGroup = QButtonGroup()
        self.passGroup.addButton(self.singlePassRadio)
        self.passGroup.addButton(self.passListRadio)
        self.passGroup.addButton(self.foundPasswordsRadio)
        self.foundPasswordsRadio.toggle()

        self.label8 = QLabel()
        self.label8.setText('Threads')
        self.label8.setFixedWidth(60)
        self.threadOptions = []
        for i in range(1, 129):
            self.threadOptions.append(str(i))
        self.threadsComboBox = QComboBox()
        self.threadsComboBox.insertItems(0, self.threadOptions)
        self.threadsComboBox.setMinimumContentsLength(3)
        self.threadsComboBox.setMaxVisibleItems(3)
        self.threadsComboBox.setStyleSheet("QComboBox { combobox-popup: 0; }");
        self.threadsComboBox.setCurrentIndex(15)

        self.hlayout3 = QHBoxLayout()
        self.hlayout3.addWidget(self.singlePassRadio)
        self.hlayout3.addWidget(self.label6)
        self.hlayout3.addWidget(self.passwordsTextinput)
        self.hlayout3.addWidget(self.passListRadio)
        self.hlayout3.addWidget(self.label7)
        self.hlayout3.addWidget(self.passlistTextinput)
        self.hlayout3.addWidget(self.browsePasswordsButton)
        self.hlayout3.addWidget(self.foundPasswordsRadio)
        self.hlayout3.addWidget(self.label10)
        self.hlayout3.addStretch()
        self.hlayout3.addWidget(self.label8)
        self.hlayout3.addWidget(self.threadsComboBox)
        # self.hlayout3.addStretch()

        return self.hlayout3

    def setupLayoutHlayout4(self):
        # label6.setText('Try blank password')
        self.checkBlankPass = QCheckBox()
        self.checkBlankPass.setText('Try blank password')
        self.checkBlankPass.toggle()
        # add 'try blank password'
        # label7.setText('Try login as password')
        self.checkLoginAsPass = QCheckBox()
        self.checkLoginAsPass.setText('Try login as password')
        self.checkLoginAsPass.toggle()
        # add 'try login as password'
        # label8.setText('Loop around users')
        self.checkLoopUsers = QCheckBox()
        self.checkLoopUsers.setText('Loop around users')
        self.checkLoopUsers.toggle()
        # add 'loop around users'
        # label9.setText('Exit on first valid')
        self.checkExitOnValid = QCheckBox()
        self.checkExitOnValid.setText('Exit on first valid')
        self.checkExitOnValid.toggle()
        # add 'exit after first valid combination is found'
        self.checkVerbose = QCheckBox()
        self.checkVerbose.setText('Verbose')

        self.checkAddMoreOptions = QCheckBox()
        self.checkAddMoreOptions.setText('Additional Options')

        self.hlayout4 = QHBoxLayout()
        self.hlayout4.addWidget(self.checkBlankPass)
        self.hlayout4.addWidget(self.checkLoginAsPass)
        self.hlayout4.addWidget(self.checkLoopUsers)
        self.hlayout4.addWidget(self.checkExitOnValid)
        self.hlayout4.addWidget(self.checkVerbose)
        self.hlayout4.addWidget(self.checkAddMoreOptions)
        self.hlayout4.addStretch()

        return self.hlayout4

    def setupLayout(self):
        ###
        self.labelPath = QLineEdit()  # this is the extra input field to insert the path to brute force
        self.labelPath.setFixedWidth(800)
        self.labelPath.setText('-m "/login/login.html:username=^USER^&password=^PASS^&Login=Login:failed"')
        ###

        self.layoutAddOptions = QHBoxLayout()
        self.layoutAddOptions.addWidget(self.labelPath)
        self.labelPath.hide()
        self.layoutAddOptions.addStretch()

        self.display = QPlainTextEdit()
        self.display.setReadOnly(True)
        if self.settings.general_tool_output_black_background == 'True':
            self.__drawPalette()

        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(self.setupLayoutHlayout())
        self.vlayout.addLayout(self.setupLayoutHlayout4())
        self.vlayout.addLayout(self.layoutAddOptions)
        self.vlayout.addLayout(self.setupLayoutHlayout2())
        self.vlayout.addLayout(self.setupLayoutHlayout3())
        self.vlayout.addWidget(self.display)
        self.setLayout(self.vlayout)

    def __drawPalette(self):
        p = self.display.palette()
        p.setColor(QPalette.Base, Qt.black)  # black background
        p.setColor(QPalette.Text, Qt.white)  # white font
        self.display.setPalette(p)
        self.display.setStyleSheet("QMenu { color:black;}")

    # TODO: need to check all the methods that need an additional input field and add them here
    #   def showMoreOptions(self, text):
    #       if str(text) == "http-head":
    #           self.labelPath.show()
    #       else:
    #           self.labelPath.hide()

    def showMoreOptions(self):
        if self.checkAddMoreOptions.isChecked():
            self.labelPath.show()
        else:
            self.labelPath.hide()

    def wordlistDialog(self, title='Choose username list'):

        if title == 'Choose username list':
            filename = QFileDialog.getOpenFileName(self, title, self.settings.brute_username_wordlist_path)
            self.userlistTextinput.setText(str(filename[0]))
            self.userListRadio.toggle()
        else:
            filename = QFileDialog.getOpenFileName(self, title, self.settings.brute_password_wordlist_path)
            self.passlistTextinput.setText(str(filename[0]))
            self.passListRadio.toggle()

    def buildHydraCommand(self, runningfolder, userlistPath, passlistPath):
        self.ip = self.ipTextinput.text()
        self.port = self.portTextinput.text()
        self.service = str(self.serviceComboBox.currentText())
        outputFile = getHydraOutputFileName(runningfolder, self.ip, self.port, self.service)
        threadsToUse = str(self.threadsComboBox.currentText())
        labelText = str(self.labelPath.text()) if self.checkAddMoreOptions.isChecked() else None

        if 'form' not in str(self.service):
            self.warningLabel.hide()

        tryLoginName = None
        tryLoginNameFile = None
        if not self.service in self.settings.brute_no_username_services.split(","):
            if self.singleUserRadio.isChecked():
                tryLoginName = self.usersTextinput.text()
            elif self.foundUsersRadio.isChecked():
                tryLoginNameFile = userlistPath
            else:
                tryLoginNameFile = self.userlistTextinput.text()

        tryPassword = None
        tryPasswordFile = None
        if not self.service in self.settings.brute_no_password_services.split(","):
            if self.singlePassRadio.isChecked():
                tryPassword = self.passwordsTextinput.text().replace('"', '\"\"\"')
            elif self.foundPasswordsRadio.isChecked():
                tryPasswordFile = passlistPath
            else:
                tryPasswordFile = self.passlistTextinput.text()

        hydraArgs = HydraCommandArguments(ipAddress=str(self.ip), port=self.port, outputFile=outputFile,
                                          threadsToUse=threadsToUse, service=self.service,
                                          verbose=self.checkVerbose.isChecked(), label=labelText,
                                          exitAfterFirstUserPassPairFound=self.checkExitOnValid.isChecked(),
                                          loopUsers=self.checkLoopUsers.isChecked(),
                                          tryLoginAsPass=self.checkLoginAsPass.isChecked(),
                                          tryNullPassword=self.checkBlankPass.isChecked(),
                                          tryPassword=tryPassword, tryPasswordFile=tryPasswordFile,
                                          tryLoginName=tryLoginName, tryLoginNameFile=tryLoginNameFile)
        return buildHydraCommand(hydraArgs)

    def getPort(self):
        return self.port

    def toggleRunButton(self):
        if self.runButton.text() == 'Run':
            self.runButton.setText('Stop')
        else:
            self.runButton.setText('Run')

    # used to be able to display the tool output in both the Brute tab and the tool display panel
    def resetDisplay(self):
        self.display.setParent(None)
        self.display = QPlainTextEdit()
        self.display.setReadOnly(True)
        if self.settings.general_tool_output_black_background == 'True':
            self.__drawPalette()
        self.vlayout.addWidget(self.display)
