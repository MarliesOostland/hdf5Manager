# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hdf5_manager.ui'
#
# Created: Tue Apr  7 23:27:51 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(908, 870)
        MainWindow.setMinimumSize(QtCore.QSize(0, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.fileGridFrame = QtGui.QFrame(self.centralwidget)
        self.fileGridFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fileGridFrame.setObjectName(_fromUtf8("fileGridFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.fileGridFrame)
        self.gridLayout_2.setMargin(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalWidget = QtGui.QWidget(self.fileGridFrame)
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(8, 2, 8, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loadDirectoryBtn = QtGui.QPushButton(self.horizontalWidget)
        self.loadDirectoryBtn.setObjectName(_fromUtf8("loadDirectoryBtn"))
        self.horizontalLayout.addWidget(self.loadDirectoryBtn)
        self.reloadDirectoryBtn = QtGui.QPushButton(self.horizontalWidget)
        self.reloadDirectoryBtn.setObjectName(_fromUtf8("reloadDirectoryBtn"))
        self.horizontalLayout.addWidget(self.reloadDirectoryBtn)
        self.gridLayout_2.addWidget(self.horizontalWidget, 1, 0, 1, 1)
        self.experimentTree = QtGui.QTreeWidget(self.fileGridFrame)
        self.experimentTree.setObjectName(_fromUtf8("experimentTree"))
        self.gridLayout_2.addWidget(self.experimentTree, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.fileGridFrame, 0, 0, 2, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.dataTab = QtGui.QWidget()
        self.dataTab.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dataTab.setObjectName(_fromUtf8("dataTab"))
        self.experimentGridFrame = QtGui.QFrame(self.dataTab)
        self.experimentGridFrame.setGeometry(QtCore.QRect(10, 10, 421, 521))
        self.experimentGridFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.experimentGridFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.experimentGridFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.experimentGridFrame.setObjectName(_fromUtf8("experimentGridFrame"))
        self.gridLayout = QtGui.QGridLayout(self.experimentGridFrame)
        self.gridLayout.setMargin(6)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dataSetAttributes = QtGui.QTableWidget(self.experimentGridFrame)
        self.dataSetAttributes.setMaximumSize(QtCore.QSize(16777215, 42))
        self.dataSetAttributes.setRowCount(2)
        self.dataSetAttributes.setColumnCount(2)
        self.dataSetAttributes.setObjectName(_fromUtf8("dataSetAttributes"))
        self.dataSetAttributes.horizontalHeader().setVisible(False)
        self.dataSetAttributes.horizontalHeader().setDefaultSectionSize(160)
        self.dataSetAttributes.horizontalHeader().setHighlightSections(True)
        self.dataSetAttributes.horizontalHeader().setStretchLastSection(True)
        self.dataSetAttributes.verticalHeader().setVisible(False)
        self.dataSetAttributes.verticalHeader().setDefaultSectionSize(20)
        self.dataSetAttributes.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.dataSetAttributes, 8, 0, 1, 1)
        self.expInfoLabel = QtGui.QLabel(self.experimentGridFrame)
        self.expInfoLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.expInfoLabel.setFont(font)
        self.expInfoLabel.setObjectName(_fromUtf8("expInfoLabel"))
        self.gridLayout.addWidget(self.expInfoLabel, 0, 0, 1, 1)
        self.experimentAttributesFixed = QtGui.QTableWidget(self.experimentGridFrame)
        self.experimentAttributesFixed.setMaximumSize(QtCore.QSize(16777215, 62))
        self.experimentAttributesFixed.setStyleSheet(_fromUtf8("background-color: rgb(230, 230, 230);"))
        self.experimentAttributesFixed.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.experimentAttributesFixed.setRowCount(3)
        self.experimentAttributesFixed.setColumnCount(2)
        self.experimentAttributesFixed.setObjectName(_fromUtf8("experimentAttributesFixed"))
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.experimentAttributesFixed.setItem(0, 0, item)
        self.experimentAttributesFixed.horizontalHeader().setVisible(False)
        self.experimentAttributesFixed.horizontalHeader().setDefaultSectionSize(160)
        self.experimentAttributesFixed.horizontalHeader().setStretchLastSection(True)
        self.experimentAttributesFixed.verticalHeader().setVisible(False)
        self.experimentAttributesFixed.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout.addWidget(self.experimentAttributesFixed, 1, 0, 1, 1)
        self.horizontalWidget1 = QtGui.QWidget(self.experimentGridFrame)
        self.horizontalWidget1.setObjectName(_fromUtf8("horizontalWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveAttributeChangeBtn = QtGui.QPushButton(self.horizontalWidget1)
        self.saveAttributeChangeBtn.setObjectName(_fromUtf8("saveAttributeChangeBtn"))
        self.horizontalLayout_2.addWidget(self.saveAttributeChangeBtn)
        self.restoreAttributesBtn = QtGui.QPushButton(self.horizontalWidget1)
        self.restoreAttributesBtn.setObjectName(_fromUtf8("restoreAttributesBtn"))
        self.horizontalLayout_2.addWidget(self.restoreAttributesBtn)
        self.gridLayout.addWidget(self.horizontalWidget1, 9, 0, 1, 1)
        self.groupAttributes = QtGui.QTableWidget(self.experimentGridFrame)
        self.groupAttributes.setMaximumSize(QtCore.QSize(16777215, 82))
        self.groupAttributes.setAutoFillBackground(False)
        self.groupAttributes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.groupAttributes.setFrameShadow(QtGui.QFrame.Sunken)
        self.groupAttributes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.groupAttributes.setTextElideMode(QtCore.Qt.ElideRight)
        self.groupAttributes.setRowCount(4)
        self.groupAttributes.setColumnCount(2)
        self.groupAttributes.setObjectName(_fromUtf8("groupAttributes"))
        self.groupAttributes.horizontalHeader().setVisible(False)
        self.groupAttributes.horizontalHeader().setCascadingSectionResizes(False)
        self.groupAttributes.horizontalHeader().setDefaultSectionSize(160)
        self.groupAttributes.horizontalHeader().setHighlightSections(True)
        self.groupAttributes.horizontalHeader().setMinimumSectionSize(56)
        self.groupAttributes.horizontalHeader().setSortIndicatorShown(False)
        self.groupAttributes.horizontalHeader().setStretchLastSection(True)
        self.groupAttributes.verticalHeader().setVisible(False)
        self.groupAttributes.verticalHeader().setCascadingSectionResizes(False)
        self.groupAttributes.verticalHeader().setDefaultSectionSize(20)
        self.groupAttributes.verticalHeader().setHighlightSections(False)
        self.groupAttributes.verticalHeader().setMinimumSectionSize(20)
        self.groupAttributes.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.groupAttributes, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.experimentGridFrame)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.experimentAttributes = QtGui.QTableWidget(self.experimentGridFrame)
        self.experimentAttributes.setMinimumSize(QtCore.QSize(0, 142))
        self.experimentAttributes.setMaximumSize(QtCore.QSize(16777215, 142))
        self.experimentAttributes.setTextElideMode(QtCore.Qt.ElideLeft)
        self.experimentAttributes.setRowCount(7)
        self.experimentAttributes.setColumnCount(2)
        self.experimentAttributes.setObjectName(_fromUtf8("experimentAttributes"))
        self.experimentAttributes.horizontalHeader().setVisible(False)
        self.experimentAttributes.horizontalHeader().setDefaultSectionSize(160)
        self.experimentAttributes.horizontalHeader().setStretchLastSection(True)
        self.experimentAttributes.verticalHeader().setVisible(False)
        self.experimentAttributes.verticalHeader().setDefaultSectionSize(20)
        self.experimentAttributes.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.experimentAttributes, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.experimentGridFrame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.groupAttributesFixed = QtGui.QTableWidget(self.experimentGridFrame)
        self.groupAttributesFixed.setMinimumSize(QtCore.QSize(0, 22))
        self.groupAttributesFixed.setMaximumSize(QtCore.QSize(16777215, 22))
        self.groupAttributesFixed.setStyleSheet(_fromUtf8("background-color: rgb(230, 230, 230);"))
        self.groupAttributesFixed.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.groupAttributesFixed.setRowCount(1)
        self.groupAttributesFixed.setColumnCount(2)
        self.groupAttributesFixed.setObjectName(_fromUtf8("groupAttributesFixed"))
        self.groupAttributesFixed.horizontalHeader().setVisible(False)
        self.groupAttributesFixed.horizontalHeader().setDefaultSectionSize(160)
        self.groupAttributesFixed.horizontalHeader().setStretchLastSection(True)
        self.groupAttributesFixed.verticalHeader().setVisible(False)
        self.groupAttributesFixed.verticalHeader().setDefaultSectionSize(20)
        self.groupAttributesFixed.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.groupAttributesFixed, 4, 0, 1, 1)
        self.dataSetAttributesFixed = QtGui.QTableWidget(self.experimentGridFrame)
        self.dataSetAttributesFixed.setMaximumSize(QtCore.QSize(16777215, 42))
        self.dataSetAttributesFixed.setStyleSheet(_fromUtf8("background-color: rgb(230, 230, 230);"))
        self.dataSetAttributesFixed.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.dataSetAttributesFixed.setRowCount(2)
        self.dataSetAttributesFixed.setColumnCount(2)
        self.dataSetAttributesFixed.setObjectName(_fromUtf8("dataSetAttributesFixed"))
        self.dataSetAttributesFixed.horizontalHeader().setVisible(False)
        self.dataSetAttributesFixed.horizontalHeader().setDefaultSectionSize(160)
        self.dataSetAttributesFixed.horizontalHeader().setStretchLastSection(True)
        self.dataSetAttributesFixed.verticalHeader().setVisible(False)
        self.dataSetAttributesFixed.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout.addWidget(self.dataSetAttributesFixed, 7, 0, 1, 1)
        self.gridFrame = QtGui.QFrame(self.dataTab)
        self.gridFrame.setGeometry(QtCore.QRect(10, 540, 421, 131))
        self.gridFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gridFrame.setObjectName(_fromUtf8("gridFrame"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout_6.setMargin(6)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_5 = QtGui.QLabel(self.gridFrame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalWidget2 = QtGui.QWidget(self.gridFrame)
        self.horizontalWidget2.setObjectName(_fromUtf8("horizontalWidget2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.genericRadioBtn = QtGui.QRadioButton(self.horizontalWidget2)
        self.genericRadioBtn.setObjectName(_fromUtf8("genericRadioBtn"))
        self.plottingChoice = QtGui.QButtonGroup(MainWindow)
        self.plottingChoice.setObjectName(_fromUtf8("plottingChoice"))
        self.plottingChoice.addButton(self.genericRadioBtn)
        self.horizontalLayout_5.addWidget(self.genericRadioBtn)
        self.timeSeriesRadioBtn = QtGui.QRadioButton(self.horizontalWidget2)
        self.timeSeriesRadioBtn.setObjectName(_fromUtf8("timeSeriesRadioBtn"))
        self.plottingChoice.addButton(self.timeSeriesRadioBtn)
        self.horizontalLayout_5.addWidget(self.timeSeriesRadioBtn)
        self.spikesRadioBtn = QtGui.QRadioButton(self.horizontalWidget2)
        self.spikesRadioBtn.setObjectName(_fromUtf8("spikesRadioBtn"))
        self.plottingChoice.addButton(self.spikesRadioBtn)
        self.horizontalLayout_5.addWidget(self.spikesRadioBtn)
        self.threeDRadioBtn = QtGui.QRadioButton(self.horizontalWidget2)
        self.threeDRadioBtn.setObjectName(_fromUtf8("threeDRadioBtn"))
        self.plottingChoice.addButton(self.threeDRadioBtn)
        self.horizontalLayout_5.addWidget(self.threeDRadioBtn)
        self.gridLayout_6.addWidget(self.horizontalWidget2, 1, 0, 1, 1)
        self.dataSetSelection = QtGui.QLineEdit(self.gridFrame)
        self.dataSetSelection.setObjectName(_fromUtf8("dataSetSelection"))
        self.gridLayout_6.addWidget(self.dataSetSelection, 2, 0, 1, 1)
        self.horizontalFrame = QtGui.QFrame(self.gridFrame)
        self.horizontalFrame.setObjectName(_fromUtf8("horizontalFrame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.plotDataBtn = QtGui.QPushButton(self.horizontalFrame)
        self.plotDataBtn.setObjectName(_fromUtf8("plotDataBtn"))
        self.horizontalLayout_3.addWidget(self.plotDataBtn)
        self.addToPlotBtn = QtGui.QPushButton(self.horizontalFrame)
        self.addToPlotBtn.setObjectName(_fromUtf8("addToPlotBtn"))
        self.horizontalLayout_3.addWidget(self.addToPlotBtn)
        self.gridLayout_6.addWidget(self.horizontalFrame, 3, 0, 1, 1)
        self.gridFrame1 = QtGui.QFrame(self.dataTab)
        self.gridFrame1.setGeometry(QtCore.QRect(9, 679, 421, 61))
        self.gridFrame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gridFrame1.setObjectName(_fromUtf8("gridFrame1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridFrame1)
        self.gridLayout_5.setMargin(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalWidget3 = QtGui.QWidget(self.gridFrame1)
        self.horizontalWidget3.setObjectName(_fromUtf8("horizontalWidget3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.launchiPythonBtn = QtGui.QPushButton(self.horizontalWidget3)
        self.launchiPythonBtn.setObjectName(_fromUtf8("launchiPythonBtn"))
        self.horizontalLayout_6.addWidget(self.launchiPythonBtn)
        self.sendToConsoleBtn = QtGui.QPushButton(self.horizontalWidget3)
        self.sendToConsoleBtn.setObjectName(_fromUtf8("sendToConsoleBtn"))
        self.horizontalLayout_6.addWidget(self.sendToConsoleBtn)
        self.plotNameSpaceBtn = QtGui.QPushButton(self.horizontalWidget3)
        self.plotNameSpaceBtn.setObjectName(_fromUtf8("plotNameSpaceBtn"))
        self.horizontalLayout_6.addWidget(self.plotNameSpaceBtn)
        self.gridLayout_5.addWidget(self.horizontalWidget3, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridFrame1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.dataTab, _fromUtf8(""))
        self.notesTab = QtGui.QWidget()
        self.notesTab.setObjectName(_fromUtf8("notesTab"))
        self.gridFrame2 = QtGui.QFrame(self.notesTab)
        self.gridFrame2.setGeometry(QtCore.QRect(10, 10, 421, 671))
        self.gridFrame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gridFrame2.setObjectName(_fromUtf8("gridFrame2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridFrame2)
        self.gridLayout_4.setMargin(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.experimentNotesValue = QtGui.QTextEdit(self.gridFrame2)
        self.experimentNotesValue.setObjectName(_fromUtf8("experimentNotesValue"))
        self.gridLayout_4.addWidget(self.experimentNotesValue, 1, 0, 1, 1)
        self.groupNotesValue = QtGui.QTextEdit(self.gridFrame2)
        self.groupNotesValue.setObjectName(_fromUtf8("groupNotesValue"))
        self.gridLayout_4.addWidget(self.groupNotesValue, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridFrame2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridFrame2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalWidget4 = QtGui.QWidget(self.gridFrame2)
        self.horizontalWidget4.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget4.setObjectName(_fromUtf8("horizontalWidget4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.saveNotesBtn = QtGui.QPushButton(self.horizontalWidget4)
        self.saveNotesBtn.setObjectName(_fromUtf8("saveNotesBtn"))
        self.horizontalLayout_4.addWidget(self.saveNotesBtn)
        self.restoreNotesBtn = QtGui.QPushButton(self.horizontalWidget4)
        self.restoreNotesBtn.setObjectName(_fromUtf8("restoreNotesBtn"))
        self.horizontalLayout_4.addWidget(self.restoreNotesBtn)
        self.gridLayout_4.addWidget(self.horizontalWidget4, 4, 0, 1, 1)
        self.tabWidget.addTab(self.notesTab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.loadDirectoryBtn.setText(_translate("MainWindow", "Load directory", None))
        self.reloadDirectoryBtn.setText(_translate("MainWindow", "Reload directory", None))
        self.experimentTree.headerItem().setText(0, _translate("MainWindow", "Data", None))
        self.expInfoLabel.setText(_translate("MainWindow", "Experiment information", None))
        __sortingEnabled = self.experimentAttributesFixed.isSortingEnabled()
        self.experimentAttributesFixed.setSortingEnabled(False)
        self.experimentAttributesFixed.setSortingEnabled(__sortingEnabled)
        self.saveAttributeChangeBtn.setText(_translate("MainWindow", "Save Attribute Changes ", None))
        self.restoreAttributesBtn.setText(_translate("MainWindow", "Restore Attributes", None))
        self.label.setText(_translate("MainWindow", "Data-set information", None))
        self.label_2.setText(_translate("MainWindow", "Group information", None))
        self.label_5.setText(_translate("MainWindow", "Plotting", None))
        self.genericRadioBtn.setText(_translate("MainWindow", "Generic", None))
        self.timeSeriesRadioBtn.setText(_translate("MainWindow", "TimeSeries", None))
        self.spikesRadioBtn.setText(_translate("MainWindow", "Spikes", None))
        self.threeDRadioBtn.setText(_translate("MainWindow", "3D", None))
        self.plotDataBtn.setText(_translate("MainWindow", "Plot data", None))
        self.addToPlotBtn.setText(_translate("MainWindow", "Add to plot", None))
        self.launchiPythonBtn.setText(_translate("MainWindow", "Launch iPython", None))
        self.sendToConsoleBtn.setText(_translate("MainWindow", "Send to concole", None))
        self.plotNameSpaceBtn.setText(_translate("MainWindow", "Print NameSpace", None))
        self.label_6.setText(_translate("MainWindow", "Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), _translate("MainWindow", "Data", None))
        self.label_3.setText(_translate("MainWindow", "Experiment notes", None))
        self.label_4.setText(_translate("MainWindow", "Group notes", None))
        self.saveNotesBtn.setText(_translate("MainWindow", "Save Notes", None))
        self.restoreNotesBtn.setText(_translate("MainWindow", "Restore Notes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), _translate("MainWindow", "Notes", None))

