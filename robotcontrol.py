#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robotcontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class Ui_RobotControlWindow(object):
    def setupUi(self, RobotControlWindow):
        RobotControlWindow.setObjectName("RobotControlWindow")
        RobotControlWindow.resize(562, 304)
        self.centralwidget = QtWidgets.QWidget(RobotControlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.line_linear = QtWidgets.QLineEdit(self.centralwidget)
        self.line_linear.setReadOnly(True)
        self.line_linear.setObjectName("line_linear")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_linear)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.line_angular = QtWidgets.QLineEdit(self.centralwidget)
        self.line_angular.setReadOnly(True)
        self.line_angular.setObjectName("line_angular")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_angular)
        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.line_posx = QtWidgets.QLineEdit(self.centralwidget)
        self.line_posx.setReadOnly(True)
        self.line_posx.setObjectName("line_posx")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_posx)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line_posy = QtWidgets.QLineEdit(self.centralwidget)
        self.line_posy.setReadOnly(True)
        self.line_posy.setObjectName("line_posy")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_posy)
        self.gridLayout_2.addLayout(self.formLayout_2, 4, 1, 1, 1)
        self.label_robotcont = QtWidgets.QLabel(self.centralwidget)
        self.label_robotcont.setObjectName("label_robotcont")
        self.gridLayout_2.addWidget(self.label_robotcont, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_left = QtWidgets.QPushButton(self.centralwidget)
        self.button_left.setObjectName("button_left")
        self.gridLayout.addWidget(self.button_left, 1, 0, 1, 1)
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setObjectName("button_stop")
        self.gridLayout.addWidget(self.button_stop, 1, 1, 1, 1)
        self.button_right = QtWidgets.QPushButton(self.centralwidget)
        self.button_right.setObjectName("button_right")
        self.gridLayout.addWidget(self.button_right, 1, 2, 1, 1)
        self.button_forward = QtWidgets.QPushButton(self.centralwidget)
        self.button_forward.setObjectName("button_forward")
        self.gridLayout.addWidget(self.button_forward, 0, 1, 1, 1)
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setObjectName("button_back")
        self.gridLayout.addWidget(self.button_back, 2, 1, 1, 1)
        self.button_RightForward = QtWidgets.QPushButton(self.centralwidget)
        self.button_RightForward.setObjectName("button_RightForward")
        self.gridLayout.addWidget(self.button_RightForward, 0, 2, 1, 1)
        self.button_LeftForward = QtWidgets.QPushButton(self.centralwidget)
        self.button_LeftForward.setObjectName("button_LeftForward")
        self.gridLayout.addWidget(self.button_LeftForward, 0, 0, 1, 1)
        self.button_LeftBack = QtWidgets.QPushButton(self.centralwidget)
        self.button_LeftBack.setObjectName("button_LeftBack")
        self.gridLayout.addWidget(self.button_LeftBack, 2, 0, 1, 1)
        self.button_RightBack = QtWidgets.QPushButton(self.centralwidget)
        self.button_RightBack.setObjectName("button_RightBack")
        self.gridLayout.addWidget(self.button_RightBack, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 4, 1)
        RobotControlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RobotControlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 22))
        self.menubar.setObjectName("menubar")
        self.menugithub_com_ercandumanmdbf = QtWidgets.QMenu(self.menubar)
        self.menugithub_com_ercandumanmdbf.setObjectName("menugithub_com_ercandumanmdbf")
        RobotControlWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RobotControlWindow)
        self.statusbar.setObjectName("statusbar")
        RobotControlWindow.setStatusBar(self.statusbar)
        self.menugithub_com_ercandumanmdbf.addSeparator()
        self.menubar.addAction(self.menugithub_com_ercandumanmdbf.menuAction())

        self.retranslateUi(RobotControlWindow)
        QtCore.QMetaObject.connectSlotsByName(RobotControlWindow)

    def retranslateUi(self, RobotControlWindow):
        _translate = QtCore.QCoreApplication.translate
        RobotControlWindow.setWindowTitle(_translate("RobotControlWindow", "Robot Control Main Window"))
        self.label_3.setText(_translate("RobotControlWindow", "Velocity"))
        self.label.setText(_translate("RobotControlWindow", "Linear Vel (m/s):"))
        self.label_2.setText(_translate("RobotControlWindow", "Angular Vel (rad/s):"))
        self.label_5.setText(_translate("RobotControlWindow", "Position"))
        self.label_4.setText(_translate("RobotControlWindow", "Pos X:"))
        self.label_6.setText(_translate("RobotControlWindow", "Pos Y:"))
        self.label_robotcont.setText(_translate("RobotControlWindow", "Robot Control"))
        self.button_left.setText(_translate("RobotControlWindow", "Left"))
        self.button_stop.setText(_translate("RobotControlWindow", "Stop"))
        self.button_right.setText(_translate("RobotControlWindow", "Right"))
        self.button_forward.setText(_translate("RobotControlWindow", "Forward"))
        self.button_back.setText(_translate("RobotControlWindow", "Back"))
        self.button_RightForward.setText(_translate("RobotControlWindow", "RightForward"))
        self.button_LeftForward.setText(_translate("RobotControlWindow", "LeftForward"))
        self.button_LeftBack.setText(_translate("RobotControlWindow", "LeftBack"))
        self.button_RightBack.setText(_translate("RobotControlWindow", "Rightback"))
        self.menugithub_com_ercandumanmdbf.setTitle(_translate("RobotControlWindow", "github.com/ercandumanmdbf"))

        rospy.init_node("RobotControlWindow")
        self.pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.velocity=Twist()
        rospy.Subscriber("odom",Odometry,self.odomCallback)

        self.button_stop.clicked.connect(self.robot_stop)
        self.button_forward.clicked.connect(self.robot_forward)
        self.button_back.clicked.connect(self.robot_back)
        self.button_left.clicked.connect(self.robot_left)
        self.button_right.clicked.connect(self.robot_right)
        self.button_LeftForward.clicked.connect(self.robot_left_forward)
        self.button_RightForward.clicked.connect(self.robot_right_forward)
        self.button_LeftBack.clicked.connect(self.robot_left_back)
        self.button_RightBack.clicked.connect(self.robot_right_back)

        self.line_angular.setText(str(0.0))
        self.line_linear.setText(str(0.0))
        self.line_posx.setText(str(0.0))
        self.line_posy.setText(str(0.0))

    def odomCallback(self,msg):
        self.line_posx.setText(str(round(msg.pose.pose.position.x,3)))
        self.line_posy.setText(str(round(msg.pose.pose.position.y,3)))

    def robot_stop(self):
        self.velocity.linear.x = 0
        self.velocity.angular.z = 0
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_forward(self):
        self.velocity.linear.x = 0.5
        self.velocity.angular.z = 0
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_back(self):
        self.velocity.linear.x = -0.5
        self.velocity.angular.z = 0
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_left(self):
        self.velocity.linear.x = 0
        self.velocity.angular.z = 0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))
    
    def robot_right(self):
        self.velocity.linear.x = 0
        self.velocity.angular.z = -0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_left_forward(self):
        self.velocity.linear.x = 0.5
        self.velocity.angular.z = 0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))
    
    def robot_right_forward(self):
        self.velocity.linear.x = 0.5
        self.velocity.angular.z = -0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_left_back(self):
        self.velocity.linear.x = -0.5
        self.velocity.angular.z = 0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))

    def robot_right_back(self):
        self.velocity.linear.x = -0.5
        self.velocity.angular.z = -0.5
        self.pub.publish(self.velocity)
        self.line_angular.setText(str(self.velocity.angular.z))
        self.line_linear.setText(str(self.velocity.linear.x))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotControlWindow = QtWidgets.QMainWindow()
    ui = Ui_RobotControlWindow()
    ui.setupUi(RobotControlWindow)
    RobotControlWindow.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RobotControlWindow = QtWidgets.QMainWindow()
    ui = Ui_RobotControlWindow()
    ui.setupUi(RobotControlWindow)
    RobotControlWindow.show()
    sys.exit(app.exec_())
