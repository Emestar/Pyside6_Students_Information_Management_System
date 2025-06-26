# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 605)
        Form.setStyleSheet(u"/* Styles for the info_frame element */\n"
"#info_frame {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
" \n"
"/* Styles for labels, input fields, and combo boxes inside \"info_frame\" */\n"
"#info_frame QLabel,\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section {\n"
"  font-family: Segoe UI Semibold;\n"
"  font-size: 12px;\n"
"}\n"
" \n"
"/* Styles for input fields and combo boxes inside info_frame */\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"  padding: 4px 5px;\n"
"  border: 1px solid #838383;\n"
"  border-radius: 2px;\n"
"}\n"
" \n"
"/* Focus styles for input fields and combo boxes */\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus {\n"
"  border-color: #005fff;\n"
"}\n"
" \n"
"/* Styles for combo boxes drop-down */\n"
"QComboBox::drop-down {\n"
"  background: transparent;\n"
"  border: none;\n"
"  margin-right: 5px;\n"
"}\n"
" \n"
"/* Styles for the down-arrow icon in combo boxes */\n"
"QComboBox::down-a"
                        "rrow {\n"
"  image: url(:/icons/expand_more.svg);\n"
"}\n"
" \n"
"/* Style for the result_frame */\n"
"#result_frame {\n"
"  border-radius: 5px;\n"
"}\n"
" \n"
"/* Style for border of QTableWidget */\n"
"QTableWidget {\n"
"  border-radius: 5px;\n"
"  border: 1px solid #0f0f0f;\n"
"}\n"
" \n"
"/* Style for table header section */\n"
"QHeaderView::section {\n"
"  border: none;\n"
"  border-bottom: 1px solid #0fc6ff;\n"
"  text-align: left;\n"
"  padding: 3px 5px;\n"
"}\n"
" \n"
"/* Styles for table items */\n"
"QTableWidget::item {\n"
"  border-bottom: 1px solid #0fc6ff;\n"
"  color: #000;\n"
"  padding-left: 5px;\n"
"}")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result_frame = QFrame(self.centralwidget)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setGeometry(QRect(20, 280, 761, 271))
        self.result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.result_table = QTableWidget(self.result_frame)
        if (self.result_table.columnCount() < 6):
            self.result_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.result_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setGeometry(QRect(30, 10, 701, 251))
        self.result_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.result_table.setShowGrid(False)
        self.result_table.horizontalHeader().setMinimumSectionSize(50)
        self.result_table.horizontalHeader().setDefaultSectionSize(100)
        self.result_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(20, 59, 761, 151))
        self.info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.info_frame.setLineWidth(0)
        self.info_frame.setMidLineWidth(0)
        self.info_split = QSplitter(self.info_frame)
        self.info_split.setObjectName(u"info_split")
        self.info_split.setGeometry(QRect(30, 10, 701, 131))
        self.info_split.setOrientation(Qt.Orientation.Horizontal)
        self.info_split.setOpaqueResize(True)
        self.info_split.setHandleWidth(50)
        self.gridLayoutWidget_2 = QWidget(self.info_split)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.grid_1 = QGridLayout(self.gridLayoutWidget_2)
        self.grid_1.setObjectName(u"grid_1")
        self.grid_1.setHorizontalSpacing(10)
        self.grid_1.setVerticalSpacing(15)
        self.grid_1.setContentsMargins(10, 0, 0, 0)
        self.firstName_label = QLabel(self.gridLayoutWidget_2)
        self.firstName_label.setObjectName(u"firstName_label")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setBold(True)
        self.firstName_label.setFont(font)

        self.grid_1.addWidget(self.firstName_label, 1, 0, 1, 1)

        self.studentID_label = QLabel(self.gridLayoutWidget_2)
        self.studentID_label.setObjectName(u"studentID_label")
        self.studentID_label.setFont(font)

        self.grid_1.addWidget(self.studentID_label, 0, 0, 1, 1)

        self.lastName_label = QLabel(self.gridLayoutWidget_2)
        self.lastName_label.setObjectName(u"lastName_label")
        self.lastName_label.setFont(font)

        self.grid_1.addWidget(self.lastName_label, 2, 0, 1, 1)

        self.studentID_input = QLineEdit(self.gridLayoutWidget_2)
        self.studentID_input.setObjectName(u"studentID_input")

        self.grid_1.addWidget(self.studentID_input, 0, 1, 1, 1)

        self.firstName_input = QLineEdit(self.gridLayoutWidget_2)
        self.firstName_input.setObjectName(u"firstName_input")

        self.grid_1.addWidget(self.firstName_input, 1, 1, 1, 1)

        self.lastName_input = QLineEdit(self.gridLayoutWidget_2)
        self.lastName_input.setObjectName(u"lastName_input")

        self.grid_1.addWidget(self.lastName_input, 2, 1, 1, 1)

        self.info_split.addWidget(self.gridLayoutWidget_2)
        self.gridLayoutWidget = QWidget(self.info_split)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.grid_2 = QGridLayout(self.gridLayoutWidget)
        self.grid_2.setObjectName(u"grid_2")
        self.grid_2.setHorizontalSpacing(10)
        self.grid_2.setVerticalSpacing(15)
        self.grid_2.setContentsMargins(10, 0, 0, 0)
        self.city_comboBox = QComboBox(self.gridLayoutWidget)
        self.city_comboBox.setObjectName(u"city_comboBox")

        self.grid_2.addWidget(self.city_comboBox, 1, 1, 1, 1)

        self.city_label = QLabel(self.gridLayoutWidget)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setFont(font)

        self.grid_2.addWidget(self.city_label, 1, 0, 1, 1)

        self.email_input = QLineEdit(self.gridLayoutWidget)
        self.email_input.setObjectName(u"email_input")

        self.grid_2.addWidget(self.email_input, 2, 1, 1, 1)

        self.state_comboBox = QComboBox(self.gridLayoutWidget)
        self.state_comboBox.setObjectName(u"state_comboBox")

        self.grid_2.addWidget(self.state_comboBox, 0, 1, 1, 1)

        self.state_label = QLabel(self.gridLayoutWidget)
        self.state_label.setObjectName(u"state_label")
        self.state_label.setFont(font)

        self.grid_2.addWidget(self.state_label, 0, 0, 1, 1)

        self.email_label = QLabel(self.gridLayoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font)

        self.grid_2.addWidget(self.email_label, 2, 0, 1, 1)

        self.info_split.addWidget(self.gridLayoutWidget)
        self.function_frame = QFrame(self.centralwidget)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setGeometry(QRect(20, 220, 760, 51))
        self.function_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_split = QSplitter(self.function_frame)
        self.btn_split.setObjectName(u"btn_split")
        self.btn_split.setGeometry(QRect(30, 10, 701, 28))
        self.btn_split.setOrientation(Qt.Orientation.Horizontal)
        self.btn_split.setHandleWidth(25)
        self.add_btn = QPushButton(self.btn_split)
        self.add_btn.setObjectName(u"add_btn")
        icon = QIcon()
        icon.addFile(u"icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.add_btn)
        self.update_btn = QPushButton(self.btn_split)
        self.update_btn.setObjectName(u"update_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/update.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.update_btn.setIcon(icon1)
        self.update_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.update_btn)
        self.select_btn = QPushButton(self.btn_split)
        self.select_btn.setObjectName(u"select_btn")
        icon2 = QIcon()
        icon2.addFile(u"icons/select.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_btn.setIcon(icon2)
        self.select_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.select_btn)
        self.search_btn = QPushButton(self.btn_split)
        self.search_btn.setObjectName(u"search_btn")
        icon3 = QIcon()
        icon3.addFile(u"icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.search_btn)
        self.clear_btn = QPushButton(self.btn_split)
        self.clear_btn.setObjectName(u"clear_btn")
        icon4 = QIcon()
        icon4.addFile(u"icons/clear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clear_btn.setIcon(icon4)
        self.clear_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.clear_btn)
        self.delete_btn = QPushButton(self.btn_split)
        self.delete_btn.setObjectName(u"delete_btn")
        icon5 = QIcon()
        icon5.addFile(u"icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setIconSize(QSize(20, 20))
        self.btn_split.addWidget(self.delete_btn)
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(20, 10, 761, 41))
        self.title_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 0, 761, 41))
        font1 = QFont()
        font1.setFamilies([u"Quicksand"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.title_label.setFont(font1)
        self.title_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title_label.setTextFormat(Qt.TextFormat.AutoText)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Form.setCentralWidget(self.centralwidget)
        self.function_frame.raise_()
        self.info_frame.raise_()
        self.result_frame.raise_()
        self.title_frame.raise_()
        self.menubar = QMenuBar(Form)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Form.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form)
        self.statusbar.setObjectName(u"statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        ___qtablewidgetitem = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Student ID", None));
        ___qtablewidgetitem1 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"First Name", None));
        ___qtablewidgetitem2 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Last Name", None));
        ___qtablewidgetitem3 = self.result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"City", None));
        ___qtablewidgetitem4 = self.result_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"State", None));
        ___qtablewidgetitem5 = self.result_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Email Address", None));
        self.firstName_label.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.studentID_label.setText(QCoreApplication.translate("Form", u"Student ID:", None))
        self.lastName_label.setText(QCoreApplication.translate("Form", u"Last Name:", None))
        self.city_label.setText(QCoreApplication.translate("Form", u"City:", None))
        self.state_label.setText(QCoreApplication.translate("Form", u"State:", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email Address:", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.select_btn.setText(QCoreApplication.translate("Form", u"Select", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Student Information System", None))
    # retranslateUi

