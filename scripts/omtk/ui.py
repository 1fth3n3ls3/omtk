# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rlessard/packages/omtk/9.9.9/scripts/omtk/ui.ui'
#
# Created: Tue Aug 23 12:22:30 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 683)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_modules = QtGui.QLabel(self.widget)
        self.label_modules.setObjectName("label_modules")
        self.verticalLayout.addWidget(self.label_modules)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_search_modules = QtGui.QLineEdit(self.widget)
        self.lineEdit_search_modules.setObjectName("lineEdit_search_modules")
        self.horizontalLayout.addWidget(self.lineEdit_search_modules)
        self.btn_update_modules = QtGui.QPushButton(self.widget)
        self.btn_update_modules.setObjectName("btn_update_modules")
        self.horizontalLayout.addWidget(self.btn_update_modules)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtGui.QTreeWidget(self.widget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_jnts = QtGui.QLabel(self.widget1)
        self.label_jnts.setObjectName("label_jnts")
        self.verticalLayout_2.addWidget(self.label_jnts)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search_jnt = QtGui.QLineEdit(self.widget1)
        self.lineEdit_search_jnt.setObjectName("lineEdit_search_jnt")
        self.horizontalLayout_2.addWidget(self.lineEdit_search_jnt)
        self.btn_update_influences = QtGui.QPushButton(self.widget1)
        self.btn_update_influences.setObjectName("btn_update_influences")
        self.horizontalLayout_2.addWidget(self.btn_update_influences)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.checkBox_hideAssigned = QtGui.QCheckBox(self.widget1)
        self.checkBox_hideAssigned.setObjectName("checkBox_hideAssigned")
        self.verticalLayout_2.addWidget(self.checkBox_hideAssigned)
        self.treeWidget_jnts = QtGui.QTreeWidget(self.widget1)
        self.treeWidget_jnts.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.treeWidget_jnts.setRootIsDecorated(True)
        self.treeWidget_jnts.setObjectName("treeWidget_jnts")
        self.treeWidget_jnts.headerItem().setText(0, "Joint Hierarchy")
        self.treeWidget_jnts.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treeWidget_jnts)
        self.widget2 = QtGui.QWidget(self.splitter)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.widget2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_search_meshes = QtGui.QLineEdit(self.widget2)
        self.lineEdit_search_meshes.setObjectName("lineEdit_search_meshes")
        self.horizontalLayout_3.addWidget(self.lineEdit_search_meshes)
        self.btn_update_meshes = QtGui.QPushButton(self.widget2)
        self.btn_update_meshes.setObjectName("btn_update_meshes")
        self.horizontalLayout_3.addWidget(self.btn_update_meshes)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.treeWidget_meshes = QtGui.QTreeWidget(self.widget2)
        self.treeWidget_meshes.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.treeWidget_meshes.setObjectName("treeWidget_meshes")
        self.verticalLayout_3.addWidget(self.treeWidget_meshes)
        self.pushButton_selectGrpMeshes = QtGui.QPushButton(self.widget2)
        self.pushButton_selectGrpMeshes.setObjectName("pushButton_selectGrpMeshes")
        self.verticalLayout_3.addWidget(self.pushButton_selectGrpMeshes)
        self.verticalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRig = QtGui.QMenu(self.menubar)
        self.menuRig.setObjectName("menuRig")
        self.menuJoint = QtGui.QMenu(self.menubar)
        self.menuJoint.setObjectName("menuJoint")
        self.menuInfluences = QtGui.QMenu(self.menubar)
        self.menuInfluences.setObjectName("menuInfluences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionBuild = QtGui.QAction(MainWindow)
        self.actionBuild.setObjectName("actionBuild")
        self.actionUnbuild = QtGui.QAction(MainWindow)
        self.actionUnbuild.setObjectName("actionUnbuild")
        self.actionRebuild = QtGui.QAction(MainWindow)
        self.actionRebuild.setObjectName("actionRebuild")
        self.actionCreateModule = QtGui.QAction(MainWindow)
        self.actionCreateModule.setObjectName("actionCreateModule")
        self.actionAddNodeToModule = QtGui.QAction(MainWindow)
        self.actionAddNodeToModule.setObjectName("actionAddNodeToModule")
        self.actionRemoveNodeFromModule = QtGui.QAction(MainWindow)
        self.actionRemoveNodeFromModule.setObjectName("actionRemoveNodeFromModule")
        self.actionMirrorJntsLToR = QtGui.QAction(MainWindow)
        self.actionMirrorJntsLToR.setObjectName("actionMirrorJntsLToR")
        self.actionMirrorJntsRToL = QtGui.QAction(MainWindow)
        self.actionMirrorJntsRToL.setObjectName("actionMirrorJntsRToL")
        self.actionMirrorSelection = QtGui.QAction(MainWindow)
        self.actionMirrorSelection.setObjectName("actionMirrorSelection")
        self.actionSelectGrpJnts = QtGui.QAction(MainWindow)
        self.actionSelectGrpJnts.setObjectName("actionSelectGrpJnts")
        self.actionSelectGrpMeshes = QtGui.QAction(MainWindow)
        self.actionSelectGrpMeshes.setObjectName("actionSelectGrpMeshes")
        self.actionUpdateModulesView = QtGui.QAction(MainWindow)
        self.actionUpdateModulesView.setObjectName("actionUpdateModulesView")
        self.actionUpdateInfluencesView = QtGui.QAction(MainWindow)
        self.actionUpdateInfluencesView.setObjectName("actionUpdateInfluencesView")
        self.actionUpdateMeshesView = QtGui.QAction(MainWindow)
        self.actionUpdateMeshesView.setObjectName("actionUpdateMeshesView")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate)
        self.menuRig.addAction(self.actionBuild)
        self.menuRig.addAction(self.actionUnbuild)
        self.menuRig.addAction(self.actionRebuild)
        self.menuJoint.addAction(self.actionCreateModule)
        self.menuJoint.addAction(self.actionAddNodeToModule)
        self.menuJoint.addAction(self.actionRemoveNodeFromModule)
        self.menuInfluences.addAction(self.actionMirrorJntsLToR)
        self.menuInfluences.addAction(self.actionMirrorJntsRToL)
        self.menuInfluences.addAction(self.actionMirrorSelection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRig.menuAction())
        self.menubar.addAction(self.menuJoint.menuAction())
        self.menubar.addAction(self.menuInfluences.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_selectGrpMeshes, QtCore.SIGNAL("pressed()"), self.actionSelectGrpMeshes.trigger)
        QtCore.QObject.connect(self.btn_update_modules, QtCore.SIGNAL("pressed()"), self.actionUpdateModulesView.trigger)
        QtCore.QObject.connect(self.btn_update_meshes, QtCore.SIGNAL("pressed()"), self.actionUpdateMeshesView.trigger)
        QtCore.QObject.connect(self.btn_update_influences, QtCore.SIGNAL("pressed()"), self.actionUpdateInfluencesView.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Open Rigging Toolkit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_modules.setText(QtGui.QApplication.translate("MainWindow", "Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_modules.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_jnts.setText(QtGui.QApplication.translate("MainWindow", "Influences", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_influences.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_hideAssigned.setText(QtGui.QApplication.translate("MainWindow", "Hide Assigned", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Meshes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update_meshes.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_selectGrpMeshes.setText(QtGui.QApplication.translate("MainWindow", "Select Meshes Grp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRig.setTitle(QtGui.QApplication.translate("MainWindow", "Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.menuJoint.setTitle(QtGui.QApplication.translate("MainWindow", "Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfluences.setTitle(QtGui.QApplication.translate("MainWindow", "Influences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setToolTip(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("MainWindow", "Build All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnbuild.setText(QtGui.QApplication.translate("MainWindow", "Unbuild All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRebuild.setText(QtGui.QApplication.translate("MainWindow", "Rebuild All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateModule.setText(QtGui.QApplication.translate("MainWindow", "Create Module", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddNodeToModule.setText(QtGui.QApplication.translate("MainWindow", "Add Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveNodeFromModule.setText(QtGui.QApplication.translate("MainWindow", "Remove Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorJntsLToR.setText(QtGui.QApplication.translate("MainWindow", "Mirror R <- L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorJntsRToL.setText(QtGui.QApplication.translate("MainWindow", "Mirror R -> L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMirrorSelection.setText(QtGui.QApplication.translate("MainWindow", "Mirror using Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectGrpJnts.setText(QtGui.QApplication.translate("MainWindow", "SelectGrpJnts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectGrpMeshes.setText(QtGui.QApplication.translate("MainWindow", "SelectGrpMeshes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateModulesView.setText(QtGui.QApplication.translate("MainWindow", "UpdateModulesView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateInfluencesView.setText(QtGui.QApplication.translate("MainWindow", "UpdateInfluencesView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateMeshesView.setText(QtGui.QApplication.translate("MainWindow", "UpdateMeshesView", None, QtGui.QApplication.UnicodeUTF8))

