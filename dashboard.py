# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_AutoDs_Intelligent(object):
    def setupUi(self, AutoDs_Intelligent):
        if not AutoDs_Intelligent.objectName():
            AutoDs_Intelligent.setObjectName(u"AutoDs_Intelligent")
        AutoDs_Intelligent.resize(1081, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoDs_Intelligent.sizePolicy().hasHeightForWidth())
        AutoDs_Intelligent.setSizePolicy(sizePolicy)
        AutoDs_Intelligent.setMinimumSize(QSize(851, 608))
        AutoDs_Intelligent.setMaximumSize(QSize(1081, 608))
        self.centralwidget = QWidget(AutoDs_Intelligent)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(851, 608))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.upload_page = QWidget()
        self.upload_page.setObjectName(u"upload_page")
        self.upload_page.setMinimumSize(QSize(851, 608))
        self.frame_2 = QFrame(self.upload_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 301, 1081, 311))
        self.frame_2.setStyleSheet(u"background-color: rgb(193, 223, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 170, 131, 121))
        self.frame_4.setStyleSheet(u"QLabel {\n"
"    font: italic 12px 'Segoe UI', sans-serif;\n"
"    color: #777777;\n"
"    padding: 5px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(260, 0, 621, 301))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)

        self.goto_dashboard = QPushButton(self.frame_5)
        self.goto_dashboard.setObjectName(u"goto_dashboard")
        self.goto_dashboard.setMinimumSize(QSize(115, 35))
        self.goto_dashboard.setMaximumSize(QSize(115, 35))
        self.goto_dashboard.setStyleSheet(u"QPushButton {\n"
"    background-color: green;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    border-radius: 6px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004c99;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #666666;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.goto_dashboard, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.upload_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1081, 301))
        self.frame.setStyleSheet(u"background-color: rgb(190, 216, 255);\n"
"background-color: rgb(193, 223, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 20, 281, 51))
        self.label.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.upload_data = QFrame(self.frame)
        self.upload_data.setObjectName(u"upload_data")
        self.upload_data.setGeometry(QRect(470, 100, 201, 81))
        self.upload_data.setAcceptDrops(True)
        self.upload_data.setStyleSheet(u"	            QFrame {\n"
"                border: 2px dashed #aaa;\n"
"                border-radius: 10px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QFrame:hover {\n"
"                background-color: #f0f0f0;\n"
"                border-color: #0078d7;\n"
"            }")
        self.upload_data.setFrameShape(QFrame.StyledPanel)
        self.upload_data.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.upload_data)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 161, 41))
        self.label_2.setStyleSheet(u"color: #666; font: 14px 'Segoe UI';\n"
"border:none;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.load_data = QPushButton(self.frame)
        self.load_data.setObjectName(u"load_data")
        self.load_data.setGeometry(QRect(510, 250, 111, 31))
        self.load_data.setStyleSheet(u"QPushButton {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    border-radius: 6px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #005fb8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004c99;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #666666;\n"
"}\n"
"")
        self.promt_input = QLineEdit(self.frame)
        self.promt_input.setObjectName(u"promt_input")
        self.promt_input.setGeometry(QRect(360, 200, 431, 41))
        self.promt_input.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    background-color: #fdfdfd;\n"
"    color: #333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"    background-color: #ffffff;\n"
"    outline: none;\n"
"}\n"
"")
        self.promt_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 200, 71, 31))
        self.label_23.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.upload_page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"background-color: rgb(159, 173, 200);")
        self.frame_6 = QFrame(self.main_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 161, 591))
        self.frame_6.setStyleSheet(u"background-color:#ffffff;\n"
"border-radius:20px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 30, 121, 20))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    font: bold 17px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.load_data_button = QPushButton(self.frame_6)
        self.buttonGroup = QButtonGroup(AutoDs_Intelligent)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.load_data_button)
        self.load_data_button.setObjectName(u"load_data_button")
        self.load_data_button.setGeometry(QRect(20, 340, 131, 41))
        self.load_data_button.setMinimumSize(QSize(131, 41))
        self.load_data_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.load_data_button.setCheckable(True)
        self.load_data_button.setChecked(False)
        self.load_data_button.setAutoExclusive(True)
        self.data_info_button = QPushButton(self.frame_6)
        self.buttonGroup.addButton(self.data_info_button)
        self.data_info_button.setObjectName(u"data_info_button")
        self.data_info_button.setGeometry(QRect(20, 180, 131, 41))
        self.data_info_button.setMinimumSize(QSize(131, 41))
        self.data_info_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.data_info_button.setCheckable(True)
        self.data_info_button.setChecked(True)
        self.data_info_button.setAutoExclusive(True)
        self.visualisation_button = QPushButton(self.frame_6)
        self.buttonGroup.addButton(self.visualisation_button)
        self.visualisation_button.setObjectName(u"visualisation_button")
        self.visualisation_button.setGeometry(QRect(20, 240, 131, 41))
        self.visualisation_button.setMinimumSize(QSize(131, 41))
        self.visualisation_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.visualisation_button.setCheckable(True)
        self.visualisation_button.setAutoExclusive(True)
        self.model_training_button = QPushButton(self.frame_6)
        self.buttonGroup.addButton(self.model_training_button)
        self.model_training_button.setObjectName(u"model_training_button")
        self.model_training_button.setGeometry(QRect(20, 290, 131, 41))
        self.model_training_button.setMinimumSize(QSize(131, 41))
        self.model_training_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 1px 0px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.model_training_button.setCheckable(True)
        self.model_training_button.setAutoExclusive(True)
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 490, 151, 71))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.stackedWidget_2 = QStackedWidget(self.main_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(179, 9, 891, 591))
        self.stackedWidget_2.setStyleSheet(u"background-color:#ffffff;\n"
"border-radius:20px;")
        self.data_info = QWidget()
        self.data_info.setObjectName(u"data_info")
        self.label_12 = QLabel(self.data_info)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(370, 10, 201, 41))
        self.label_12.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.frame_7 = QFrame(self.data_info)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(210, 80, 521, 58))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.data_info_button_2 = QPushButton(self.frame_7)
        self.buttonGroup_2 = QButtonGroup(AutoDs_Intelligent)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.data_info_button_2)
        self.data_info_button_2.setObjectName(u"data_info_button_2")
        self.data_info_button_2.setMinimumSize(QSize(200, 40))
        self.data_info_button_2.setMaximumSize(QSize(200, 40))
        self.data_info_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.data_info_button_2.setCheckable(True)
        self.data_info_button_2.setChecked(True)
        self.data_info_button_2.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.data_info_button_2)

        self.feature_info_button = QPushButton(self.frame_7)
        self.buttonGroup_2.addButton(self.feature_info_button)
        self.feature_info_button.setObjectName(u"feature_info_button")
        self.feature_info_button.setMinimumSize(QSize(200, 40))
        self.feature_info_button.setMaximumSize(QSize(200, 40))
        self.feature_info_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.feature_info_button.setCheckable(True)
        self.feature_info_button.setChecked(False)
        self.feature_info_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.feature_info_button)

        self.stackedWidget_3 = QStackedWidget(self.data_info)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(19, 159, 851, 421))
        self.stackedWidget_3.setStyleSheet(u"")
        self.dataset_information_page = QWidget()
        self.dataset_information_page.setObjectName(u"dataset_information_page")
        self.label_18 = QLabel(self.dataset_information_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(300, 0, 291, 41))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.tableWidget = QTableWidget(self.dataset_information_page)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 831, 371))
        self.tableWidget.setStyleSheet(u"QTableWidget, QTableView {\n"
"    background-color: white;\n"
"    border: 1px solid #ddd;\n"
"    gridline-color: #e0e0e0;\n"
"    font: 13px 'Segoe UI', sans-serif;\n"
"    alternate-background-color: #f9f9f9;\n"
"    selection-background-color: #0078d7;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f2f2f2;\n"
"    color: #333;\n"
"    padding: 6px;\n"
"    border: 1px solid #ddd;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #f5f5f5;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #999999;\n"
"}\n"
"")
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.stackedWidget_3.addWidget(self.dataset_information_page)
        self.custom_information = QWidget()
        self.custom_information.setObjectName(u"custom_information")
        self.label_19 = QLabel(self.custom_information)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(300, 0, 291, 31))
        self.label_19.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.custom_information)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(180, 40, 661, 381))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"}\n"
"")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textEdit.setLineWrapColumnOrWidth(6)
        self.textEdit.setReadOnly(True)
        self.listWidget = QListWidget(self.custom_information)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 40, 171, 381))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    padding: 5px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"    color: #333;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget.setAutoScrollMargin(14)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty(u"showDropIndicator", False)
        self.listWidget.setTextElideMode(Qt.ElideMiddle)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setProperty(u"isWrapping", False)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setWordWrap(True)
        self.stackedWidget_3.addWidget(self.custom_information)
        self.stackedWidget_2.addWidget(self.data_info)
        self.visualisation = QWidget()
        self.visualisation.setObjectName(u"visualisation")
        self.label_15 = QLabel(self.visualisation)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(350, 10, 241, 41))
        self.label_15.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.frame_8 = QFrame(self.visualisation)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(210, 80, 521, 58))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.preset_button = QPushButton(self.frame_8)
        self.preset_button.setObjectName(u"preset_button")
        self.preset_button.setMinimumSize(QSize(200, 40))
        self.preset_button.setMaximumSize(QSize(200, 40))
        self.preset_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.preset_button.setCheckable(True)
        self.preset_button.setChecked(True)
        self.preset_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.preset_button)

        self.custom_dashboard_button = QPushButton(self.frame_8)
        self.custom_dashboard_button.setObjectName(u"custom_dashboard_button")
        self.custom_dashboard_button.setMinimumSize(QSize(200, 40))
        self.custom_dashboard_button.setMaximumSize(QSize(200, 40))
        self.custom_dashboard_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.custom_dashboard_button.setCheckable(True)
        self.custom_dashboard_button.setChecked(False)
        self.custom_dashboard_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.custom_dashboard_button)

        self.stackedWidget_4 = QStackedWidget(self.visualisation)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(20, 140, 851, 421))
        self.stackedWidget_4.setStyleSheet(u"")
        self.preset_chart_page = QWidget()
        self.preset_chart_page.setObjectName(u"preset_chart_page")
        self.label_20 = QLabel(self.preset_chart_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 10, 291, 41))
        self.label_20.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.listWidget_3 = QListWidget(self.preset_chart_page)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(10, 50, 141, 371))
        self.listWidget_3.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    padding: 5px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"    color: #333;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.listWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_3.setProperty(u"isWrapping", True)
        self.label_17 = QLabel(self.preset_chart_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(176, 59, 671, 361))
        self.label_17.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.stackedWidget_4.addWidget(self.preset_chart_page)
        self.custom_chart_page = QWidget()
        self.custom_chart_page.setObjectName(u"custom_chart_page")
        self.label_21 = QLabel(self.custom_chart_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(300, 0, 291, 31))
        self.label_21.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.listWidget_2 = QListWidget(self.custom_chart_page)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(0, 40, 141, 381))
        self.listWidget_2.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    padding: 5px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"    color: #333;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setProperty(u"isWrapping", True)
        self.label_22 = QLabel(self.custom_chart_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(160, 120, 671, 291))
        self.label_22.setAlignment(Qt.AlignCenter)
        self.generate_button = QPushButton(self.custom_chart_page)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(320, 50, 151, 41))
        self.generate_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"\n"
"    background-color: green;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"    color: #222;\n"
"}")
        self.comboBox = QComboBox(self.custom_chart_page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 50, 101, 31))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px 12px;\n"
"    border-radius: 6px;\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #0078d7;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 0px;\n"
"    border-left: 1px solid #cccccc;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #0078d7;\n"
"    selection-color: white;\n"
"    background-color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.stackedWidget_4.addWidget(self.custom_chart_page)
        self.stackedWidget_2.addWidget(self.visualisation)
        self.model_training = QWidget()
        self.model_training.setObjectName(u"model_training")
        self.label_16 = QLabel(self.model_training)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(410, 10, 151, 41))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.frame_9 = QFrame(self.model_training)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(210, 80, 521, 58))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.preset_button_2 = QPushButton(self.frame_9)
        self.preset_button_2.setObjectName(u"preset_button_2")
        self.preset_button_2.setMinimumSize(QSize(200, 40))
        self.preset_button_2.setMaximumSize(QSize(200, 40))
        self.preset_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.preset_button_2.setCheckable(True)
        self.preset_button_2.setChecked(True)
        self.preset_button_2.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.preset_button_2)

        self.custom_dashboard_button_2 = QPushButton(self.frame_9)
        self.custom_dashboard_button_2.setObjectName(u"custom_dashboard_button_2")
        self.custom_dashboard_button_2.setMinimumSize(QSize(200, 40))
        self.custom_dashboard_button_2.setMaximumSize(QSize(200, 40))
        self.custom_dashboard_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2f2f2;\n"
"    color: #222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.custom_dashboard_button_2.setCheckable(True)
        self.custom_dashboard_button_2.setChecked(False)
        self.custom_dashboard_button_2.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.custom_dashboard_button_2)

        self.stackedWidget_5 = QStackedWidget(self.model_training)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setGeometry(QRect(20, 140, 851, 421))
        self.stackedWidget_5.setStyleSheet(u"")
        self.preset_chart_page_2 = QWidget()
        self.preset_chart_page_2.setObjectName(u"preset_chart_page_2")
        self.label_24 = QLabel(self.preset_chart_page_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(380, 10, 181, 41))
        self.label_24.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.listWidget_4 = QListWidget(self.preset_chart_page_2)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setGeometry(QRect(10, 50, 141, 371))
        self.listWidget_4.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    padding: 5px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"    color: #333;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.listWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setProperty(u"isWrapping", True)
        self.label_25 = QLabel(self.preset_chart_page_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(176, 119, 671, 301))
        self.label_25.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.generate_button_3 = QPushButton(self.preset_chart_page_2)
        self.generate_button_3.setObjectName(u"generate_button_3")
        self.generate_button_3.setGeometry(QRect(170, 60, 151, 41))
        self.generate_button_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"\n"
"    background-color: green;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"    color: #222;\n"
"}")
        self.stackedWidget_5.addWidget(self.preset_chart_page_2)
        self.custom_chart_page_2 = QWidget()
        self.custom_chart_page_2.setObjectName(u"custom_chart_page_2")
        self.label_26 = QLabel(self.custom_chart_page_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(300, 0, 291, 31))
        self.label_26.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.generate_button_2 = QPushButton(self.custom_chart_page_2)
        self.generate_button_2.setObjectName(u"generate_button_2")
        self.generate_button_2.setGeometry(QRect(10, 290, 151, 41))
        self.generate_button_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"\n"
"    background-color: green;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"    color: #222;\n"
"}")
        self.comboBox_2 = QComboBox(self.custom_chart_page_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 130, 151, 31))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px 12px;\n"
"    border-radius: 6px;\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #0078d7;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 0px;\n"
"    border-left: 1px solid #cccccc;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #0078d7;\n"
"    selection-color: white;\n"
"    background-color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.label_11 = QLabel(self.custom_chart_page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 190, 101, 21))
        self.label_11.setStyleSheet(u"QLabel {\n"
"    font: bold 15px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_27 = QLabel(self.custom_chart_page_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 240, 101, 21))
        self.label_27.setStyleSheet(u"QLabel {\n"
"    font: bold 15px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.lineEdit = QLineEdit(self.custom_chart_page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 190, 113, 31))
        self.lineEdit.setStyleSheet(u"    QLineEdit {\n"
"        background-color: #ffffff;\n"
"        border: 1.5px solid #cccccc;\n"
"        border-radius: 8px;\n"
"        padding: 6px 10px;\n"
"        font-size: 14px;\n"
"        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;\n"
"        color: #333333;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 1.5px solid #0078d7;\n"
"        outline: none;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: #f2f2f2;\n"
"        color: #a0a0a0;\n"
"    }")
        self.lineEdit_2 = QLineEdit(self.custom_chart_page_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 230, 113, 31))
        self.lineEdit_2.setStyleSheet(u"    QLineEdit {\n"
"        background-color: #ffffff;\n"
"        border: 1.5px solid #cccccc;\n"
"        border-radius: 8px;\n"
"        padding: 6px 10px;\n"
"        font-size: 14px;\n"
"        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;\n"
"        color: #333333;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border: 1.5px solid #0078d7;\n"
"        outline: none;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: #f2f2f2;\n"
"        color: #a0a0a0;\n"
"    }")
        self.label_28 = QLabel(self.custom_chart_page_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(266, 59, 471, 111))
        self.label_28.setStyleSheet(u"QLabel {\n"
"    font: bold 15px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_29 = QLabel(self.custom_chart_page_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 20, 151, 16))
        self.label_29.setStyleSheet(u"QLabel {\n"
"    font: bold 15px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.comboBox_3 = QComboBox(self.custom_chart_page_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(10, 50, 151, 31))
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #cccccc;\n"
"    padding: 6px 12px;\n"
"    border-radius: 6px;\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #0078d7;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 0px;\n"
"    border-left: 1px solid #cccccc;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #cccccc;\n"
"    selection-background-color: #0078d7;\n"
"    selection-color: white;\n"
"    background-color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.label_30 = QLabel(self.custom_chart_page_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 100, 101, 16))
        self.label_30.setStyleSheet(u"QLabel {\n"
"    font: bold 15px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.stackedWidget_5.addWidget(self.custom_chart_page_2)
        self.stackedWidget_2.addWidget(self.model_training)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_31 = QLabel(self.page)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(410, 10, 151, 41))
        self.label_31.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.listWidget_5 = QListWidget(self.page)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setGeometry(QRect(10, 180, 141, 371))
        self.listWidget_5.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    padding: 5px;\n"
"    font: 14px 'Segoe UI', sans-serif;\n"
"    color: #333;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.listWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_5.setProperty(u"isWrapping", True)
        self.label_32 = QLabel(self.page)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(380, 140, 181, 41))
        self.label_32.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_33 = QLabel(self.page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(176, 249, 671, 301))
        self.label_33.setStyleSheet(u"QLabel {\n"
"    font: bold 20px 'Segoe UI', sans-serif;\n"
"    color: #333333;\n"
"\n"
"}")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.generate_button_4 = QPushButton(self.page)
        self.generate_button_4.setObjectName(u"generate_button_4")
        self.generate_button_4.setGeometry(QRect(170, 190, 151, 41))
        self.generate_button_4.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #444;\n"
"    padding: 10px 20px;\n"
"    text-align: centre;\n"
"    border: none;\n"
"    font: 15px 'Segoe UI', sans-serif;\n"
"    border-radius: 6px;\n"
"\n"
"    background-color: green;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: gray;\n"
"    color: #222;\n"
"}")
        self.stackedWidget_2.addWidget(self.page)
        self.stackedWidget.addWidget(self.main_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        AutoDs_Intelligent.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutoDs_Intelligent)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AutoDs_Intelligent)
    # setupUi

    def retranslateUi(self, AutoDs_Intelligent):
        AutoDs_Intelligent.setWindowTitle(QCoreApplication.translate("AutoDs_Intelligent", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Presented By", None))
        self.label_4.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Pranit Kalebere", None))
        self.label_5.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Mehul Kamble", None))
        self.label_6.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Rajashri Kongare", None))
        self.label_7.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Data Importing", None))
        self.label_8.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Problem Statement analysis", None))
        self.label_9.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Identifying features", None))
        self.label_10.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Preprocess Data", None))
        self.goto_dashboard.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Submit", None))
        self.label.setText(QCoreApplication.translate("AutoDs_Intelligent", u"AutoDs Intelligent Workflow", None))
        self.label_2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"\"Drag & drop files here\n"
"or click to choose\"", None))
        self.load_data.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Submit", None))
        self.label_23.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Promt :", None))
        self.label_13.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Control Panel", None))
        self.load_data_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Load Data", None))
        self.data_info_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Data Info", None))
        self.visualisation_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Visualisation", None))
        self.model_training_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Model Training", None))
        self.label_14.setText(QCoreApplication.translate("AutoDs_Intelligent", u"AutoDs Intelligent", None))
        self.label_12.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Feature Information", None))
        self.data_info_button_2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Dataset Information", None))
        self.feature_info_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Feature Information", None))
        self.label_18.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Complete Dataset Information", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Feature", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Nulls", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Unique", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Min", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Max", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Mean", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Mode", None));
        self.label_19.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Custom Feature Information", None))
        self.label_15.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Visualisation  Dashboard", None))
        self.preset_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Presets", None))
        self.custom_dashboard_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Custom Dashboard", None))
        self.label_20.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Preset Visualisation Charts", None))
        self.label_17.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Plot will appear here", None))
        self.label_21.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Custom Visualisation Creation", None))
        self.label_22.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Plot will appear here", None))
        self.generate_button.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Generate Chart", None))
        self.label_16.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Model Training", None))
        self.preset_button_2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Pretrained", None))
        self.custom_dashboard_button_2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Custom Training", None))
        self.label_24.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Pretrained Models", None))
        self.label_25.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Plot will appear here", None))
        self.generate_button_3.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Save Model", None))
        self.label_26.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Custom Model Training", None))
        self.generate_button_2.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Generate Chart", None))
        self.label_11.setText(QCoreApplication.translate("AutoDs_Intelligent", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("AutoDs_Intelligent", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("AutoDs_Intelligent", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Select Problem Type", None))
        self.label_30.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Select Model", None))
        self.label_31.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Model Training", None))
        self.label_32.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Pretrained Models", None))
        self.label_33.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Plot will appear here", None))
        self.generate_button_4.setText(QCoreApplication.translate("AutoDs_Intelligent", u"Save Model", None))
    # retranslateUi

