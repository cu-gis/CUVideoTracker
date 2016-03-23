# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableManagerUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(627, 453)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/icons/tableManagerIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.fieldsTable = QtGui.QTableWidget(self.tab_2)
        self.fieldsTable.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsTable.sizePolicy().hasHeightForWidth())
        self.fieldsTable.setSizePolicy(sizePolicy)
        self.fieldsTable.setMinimumSize(QtCore.QSize(0, 280))
        self.fieldsTable.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fieldsTable.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.fieldsTable.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.fieldsTable.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.fieldsTable.setGridStyle(QtCore.Qt.DotLine)
        self.fieldsTable.setWordWrap(False)
        self.fieldsTable.setCornerButtonEnabled(False)
        self.fieldsTable.setRowCount(0)
        self.fieldsTable.setColumnCount(2)
        self.fieldsTable.setObjectName(_fromUtf8("fieldsTable"))
        item = QtGui.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(1, item)
        self.gridlayout1.addWidget(self.fieldsTable, 0, 0, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.butUp = QtGui.QToolButton(self.tab_2)
        self.butUp.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butUp.sizePolicy().hasHeightForWidth())
        self.butUp.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/crystalsvg_1uparrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butUp.setIcon(icon1)
        self.butUp.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butUp.setObjectName(_fromUtf8("butUp"))
        self.vboxlayout.addWidget(self.butUp)
        self.butDown = QtGui.QToolButton(self.tab_2)
        self.butDown.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDown.sizePolicy().hasHeightForWidth())
        self.butDown.setSizePolicy(sizePolicy)
        self.butDown.setMinimumSize(QtCore.QSize(120, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/crystalsvg_1downarrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDown.setIcon(icon2)
        self.butDown.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDown.setObjectName(_fromUtf8("butDown"))
        self.vboxlayout.addWidget(self.butDown)
        self.butRename = QtGui.QToolButton(self.tab_2)
        self.butRename.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRename.sizePolicy().hasHeightForWidth())
        self.butRename.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/tableManagerIcon3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRename.setIcon(icon3)
        self.butRename.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butRename.setObjectName(_fromUtf8("butRename"))
        self.vboxlayout.addWidget(self.butRename)
        self.butIns = QtGui.QToolButton(self.tab_2)
        self.butIns.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butIns.sizePolicy().hasHeightForWidth())
        self.butIns.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionNewAttribute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butIns.setIcon(icon4)
        self.butIns.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butIns.setObjectName(_fromUtf8("butIns"))
        self.vboxlayout.addWidget(self.butIns)
        self.butClone = QtGui.QToolButton(self.tab_2)
        self.butClone.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClone.sizePolicy().hasHeightForWidth())
        self.butClone.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionCopySelected.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClone.setIcon(icon5)
        self.butClone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butClone.setObjectName(_fromUtf8("butClone"))
        self.vboxlayout.addWidget(self.butClone)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout.addItem(spacerItem)
        self.butDel = QtGui.QToolButton(self.tab_2)
        self.butDel.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDel.sizePolicy().hasHeightForWidth())
        self.butDel.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 147, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.butDel.setPalette(palette)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionDeleteAttribute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDel.setIcon(icon6)
        self.butDel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDel.setObjectName(_fromUtf8("butDel"))
        self.vboxlayout.addWidget(self.butDel)
        spacerItem1 = QtGui.QSpacerItem(120, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridlayout1.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridlayout2 = QtGui.QGridLayout(self.tab_4)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.dataTable = QtGui.QTableWidget(self.tab_4)
        self.dataTable.setEnabled(True)
        self.dataTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.dataTable.setGridStyle(QtCore.Qt.DotLine)
        self.dataTable.setWordWrap(False)
        self.dataTable.setCornerButtonEnabled(False)
        self.dataTable.setObjectName(_fromUtf8("dataTable"))
        self.dataTable.setColumnCount(0)
        self.dataTable.setRowCount(0)
        self.gridlayout2.addWidget(self.dataTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.butSaveAs = QtGui.QPushButton(Dialog)
        self.butSaveAs.setEnabled(False)
        self.butSaveAs.setMinimumSize(QtCore.QSize(0, 32))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionFileSaveAs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSaveAs.setIcon(icon7)
        self.butSaveAs.setObjectName(_fromUtf8("butSaveAs"))
        self.hboxlayout.addWidget(self.butSaveAs)
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem5)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.fieldsTable)
        Dialog.setTabOrder(self.fieldsTable, self.butUp)
        Dialog.setTabOrder(self.butUp, self.butDown)
        Dialog.setTabOrder(self.butDown, self.butRename)
        Dialog.setTabOrder(self.butRename, self.butIns)
        Dialog.setTabOrder(self.butIns, self.butClone)
        Dialog.setTabOrder(self.butClone, self.dataTable)
        Dialog.setTabOrder(self.dataTable, self.butSaveAs)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Table Manager", None))
        item = self.fieldsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name", None))
        item = self.fieldsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Type", None))
        self.butUp.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field up</p></body></html>", None))
        self.butUp.setText(_translate("Dialog", "Move Up", None))
        self.butDown.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field down</p></body></html>", None))
        self.butDown.setText(_translate("Dialog", "Move Down", None))
        self.butRename.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rename selected field</p></body></html>", None))
        self.butRename.setText(_translate("Dialog", "Rename", None))
        self.butIns.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Insert new field</p></body></html>", None))
        self.butIns.setText(_translate("Dialog", "Insert", None))
        self.butClone.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone selected field</p></body></html>", None))
        self.butClone.setText(_translate("Dialog", "Clone", None))
        self.butDel.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remove selected field</p></body></html>", None))
        self.butDel.setText(_translate("Dialog", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Table preview", None))
        self.butSaveAs.setToolTip(_translate("Dialog", "Save changes to a new layer", None))
        self.butSaveAs.setText(_translate("Dialog", "Create Point Layer", None))

import resources
