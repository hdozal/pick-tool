# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Directory.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DirectoryConfig(object):
    def setupUi(self, DirectoryConfig):
        DirectoryConfig.setObjectName("DirectoryConfig")
        DirectoryConfig.resize(491, 229)
        self.verticalLayout = QtWidgets.QVBoxLayout(DirectoryConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DirectoryTitle = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.DirectoryTitle.setFont(font)
        self.DirectoryTitle.setObjectName("DirectoryTitle")
        self.verticalLayout.addWidget(self.DirectoryTitle)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.RootDirectTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RootDirectTextbox.sizePolicy().hasHeightForWidth())
        self.RootDirectTextbox.setSizePolicy(sizePolicy)
        self.RootDirectTextbox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.RootDirectTextbox.setObjectName("RootDirectTextbox")
        self.gridLayout.addWidget(self.RootDirectTextbox, 1, 1, 1, 1)
        self.whiteTeamTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whiteTeamTextbox.sizePolicy().hasHeightForWidth())
        self.whiteTeamTextbox.setSizePolicy(sizePolicy)
        self.whiteTeamTextbox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.whiteTeamTextbox.setObjectName("whiteTeamTextbox")
        self.gridLayout.addWidget(self.whiteTeamTextbox, 3, 4, 1, 1)
        self.BluedirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.BluedirectBut.setMaximumSize(QtCore.QSize(20, 16777215))
        self.BluedirectBut.setObjectName("BluedirectBut")
        self.gridLayout.addWidget(self.BluedirectBut, 1, 5, 1, 1)
        self.WhitedirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.WhitedirectBut.setMaximumSize(QtCore.QSize(20, 16777215))
        self.WhitedirectBut.setObjectName("WhitedirectBut")
        self.gridLayout.addWidget(self.WhitedirectBut, 3, 5, 1, 1)
        self.RootdirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.RootdirectBut.setMaximumSize(QtCore.QSize(20, 16777215))
        self.RootdirectBut.setObjectName("RootdirectBut")
        self.gridLayout.addWidget(self.RootdirectBut, 1, 2, 1, 1)
        self.ReddirectBut = QtWidgets.QPushButton(DirectoryConfig)
        self.ReddirectBut.setMaximumSize(QtCore.QSize(20, 16777215))
        self.ReddirectBut.setObjectName("ReddirectBut")
        self.gridLayout.addWidget(self.ReddirectBut, 3, 2, 1, 1)
        self.RedTeamlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RedTeamlabel.setFont(font)
        self.RedTeamlabel.setObjectName("RedTeamlabel")
        self.gridLayout.addWidget(self.RedTeamlabel, 2, 1, 1, 1)
        self.RootDirectlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RootDirectlabel.setFont(font)
        self.RootDirectlabel.setObjectName("RootDirectlabel")
        self.gridLayout.addWidget(self.RootDirectlabel, 0, 1, 1, 1)
        self.BlueTeamlabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BlueTeamlabel.setFont(font)
        self.BlueTeamlabel.setObjectName("BlueTeamlabel")
        self.gridLayout.addWidget(self.BlueTeamlabel, 0, 4, 1, 1)
        self.RedTeamtextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RedTeamtextbox.sizePolicy().hasHeightForWidth())
        self.RedTeamtextbox.setSizePolicy(sizePolicy)
        self.RedTeamtextbox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.RedTeamtextbox.setObjectName("RedTeamtextbox")
        self.gridLayout.addWidget(self.RedTeamtextbox, 3, 1, 1, 1)
        self.BlueTeamTextbox = QtWidgets.QTextBrowser(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BlueTeamTextbox.sizePolicy().hasHeightForWidth())
        self.BlueTeamTextbox.setSizePolicy(sizePolicy)
        self.BlueTeamTextbox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.BlueTeamTextbox.setObjectName("BlueTeamTextbox")
        self.gridLayout.addWidget(self.BlueTeamTextbox, 1, 4, 1, 1)
        self.WhiteTeamLabel = QtWidgets.QLabel(DirectoryConfig)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WhiteTeamLabel.setFont(font)
        self.WhiteTeamLabel.setObjectName("WhiteTeamLabel")
        self.gridLayout.addWidget(self.WhiteTeamLabel, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.goBackToEvent = QtWidgets.QPushButton(DirectoryConfig)
        self.goBackToEvent.setObjectName("goBackToEvent")
        self.verticalLayout.addWidget(self.goBackToEvent)
        self.SaveEventBut = QtWidgets.QPushButton(DirectoryConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveEventBut.sizePolicy().hasHeightForWidth())
        self.SaveEventBut.setSizePolicy(sizePolicy)
        self.SaveEventBut.setObjectName("SaveEventBut")
        self.verticalLayout.addWidget(self.SaveEventBut)

        self.retranslateUi(DirectoryConfig)
        QtCore.QMetaObject.connectSlotsByName(DirectoryConfig)

    def retranslateUi(self, DirectoryConfig):
        _translate = QtCore.QCoreApplication.translate
        DirectoryConfig.setWindowTitle(_translate("DirectoryConfig", "Directory Config"))
        self.DirectoryTitle.setText(_translate("DirectoryConfig", "Directory Configuration"))
        self.BluedirectBut.setText(_translate("DirectoryConfig", "...."))
        self.WhitedirectBut.setText(_translate("DirectoryConfig", "...."))
        self.RootdirectBut.setText(_translate("DirectoryConfig", "...."))
        self.ReddirectBut.setText(_translate("DirectoryConfig", "...."))
        self.RedTeamlabel.setText(_translate("DirectoryConfig", "Red Team Folder"))
        self.RootDirectlabel.setText(_translate("DirectoryConfig", "Root Directory"))
        self.BlueTeamlabel.setText(_translate("DirectoryConfig", "Blue Team Folder"))
        self.WhiteTeamLabel.setText(_translate("DirectoryConfig", "White Team Folder"))
        self.goBackToEvent.setText(_translate("DirectoryConfig", "Event Config"))
        self.SaveEventBut.setText(_translate("DirectoryConfig", "Start Data Ingestion"))