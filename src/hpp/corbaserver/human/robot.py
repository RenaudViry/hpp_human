#
# Copyright (c) 2014 CNRS
# Authors: Renaud Viry
#
#
# This file is part of hpp_romeo
# hpp_romeo is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_romeo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_romeo  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.robot import Robot as Parent

##
#  Control of robot Romeo in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp-corbaserver. It derive from class hpp.corbaserver.robot.Robot.
#
#  This class is also used to initialize a client to rviz in order to
#  display configurations of the Romeo robot.
#
#  At creation of an instance, the urdf and srdf files are loaded using
#  idl interface hpp::corbaserver::Robot::loadRobotModel.
class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    packageName = "human_model"
    ##
    #  Information to retrieve urdf and srdf files.
    urdfName = "Human"
    urdfSuffix = ""
    srdfSuffix = ""

    initPos = {'Pelvis'     :(0, 0, 0, 0, 0, 0)
               'TorsoX'     : 0,
               'TorsoY'     : 0,
               'TorsoZ'     : 0,
               'HeadZ'      : 0,
               'HeadY'      : 0,
               'rShoulderX' : 0,
               'rShoulderZ' : 0,
               'rShoulderY' : 0,
               'rArmTrans'  : 0,
               'rElbowZ'    : 0,
               'rPoint'     : 0,
               'rWristX'    : 0,
               'rWristY'    : 0,
               'rWristZ'    : 0,
               'lShoulderX' : 0,
               'lShoulderZ' : 0,
               'lShoulderY' : 0,
               'lArmTrans'  : 0,
               'lElbowZ'    : 0,
               'lPoint'     : 0,
               'lWristX'    : 0,
               'lWristY'    : 0,
               'lWristZ'    : 0,
               'rHipX'      : 0,
               'rHipY'      : 0,
               'rHipZ'      : 0,
               'rKnee'      : 0,
               'rAnkleX'    : 0,
               'rAnkleY'    : 0,
               'rAnkleZ'    : 0,
               'lHipX'      : 0,
               'lHipY'      : 0,
               'lHipZ'      : 0,
               'lKnee'      : 0,
               'lAnkleX'    : 0,
               'lAnkleY'    : 0,
               'lAnkleZ'    : 0,
               'rPalm'      : 0,
               'lPalm'      : 0 }

    standing = {'Pelvis'     :(0, 0, 1.07, 0, 0, 0)
                'TorsoX'     : 0,
                'TorsoY'     : 0,
                'TorsoZ'     : 0,
                'HeadZ'      : 0,
                'HeadY'      : 0,
                'rShoulderX' : 1.4,
                'rShoulderZ' : 0,
                'rShoulderY' : 0,
                'rArmTrans'  : 0,
                'rElbowZ'    : 1.4,
                'rPoint'     : 0,
                'rWristX'    : 0,
                'rWristY'    : 0,
                'rWristZ'    : 0,
                'lShoulderX' : -1.4,
                'lShoulderZ' : 0,
                'lShoulderY' : 0,
                'lArmTrans'  : 0,
                'lElbowZ'    : -1.4,
                'lPoint'     : 0,
                'lWristX'    : 0,
                'lWristY'    : 0,
                'lWristZ'    : 0,
                'rHipX'      : 0,
                'rHipY'      : 0,
                'rHipZ'      : 0,
                'rKnee'      : 0,
                'rAnkleX'    : 0,
                'rAnkleY'    : 0,
                'rAnkleZ'    : 0,
                'lHipX'      : 0,
                'lHipY'      : 0,
                'lHipZ'      : 0,
                'lKnee'      : 0,
                'lAnkleX'    : 0,
                'lAnkleY'    : 0,
                'lAnkleZ'    : 0,
                'rPalm'      : 0,
                'lPalm'      : 0 }

    sitting = {'Pelvis'     :(0, 0, 0.61, 0, 0, 0)
               'TorsoX'     : 0,
               'TorsoY'     : 0,
               'TorsoZ'     : 0,
               'HeadZ'      : 0,
               'HeadY'      : 0,
               'rShoulderX' : 1.4,
               'rShoulderZ' : 0,
               'rShoulderY' : 0,
               'rArmTrans'  : 0,
               'rElbowZ'    : 1.4,
               'rPoint'     : 0,
               'rWristX'    : 0,
               'rWristY'    : 0,
               'rWristZ'    : 0,
               'lShoulderX' : -1.4,
               'lShoulderZ' : 0,
               'lShoulderY' : 0,
               'lArmTrans'  : 0,
               'lElbowZ'    : -1.4,
               'lPoint'     : 0,
               'lWristX'    : 0,
               'lWristY'    : 0,
               'lWristZ'    : 0,
               'rHipX'      : 0,
               'rHipY'      : -1.57,
               'rHipZ'      : 0,
               'rKnee'      : 1.57,
               'rAnkleX'    : 0,
               'rAnkleY'    : 0,
               'rAnkleZ'    : 0,
               'lHipX'      : 0,
               'lHipY'      : -1.57,
               'lHipZ'      : 0,
               'lKnee'      : 1.57,
               'lAnkleX'    : 0,
               'lAnkleY'    : 0,
               'lAnkleZ'    : 0,
               'rPalm'      : 0,
               'lPalm'      : 0 }

    def __init__ (self, robotName, load = True):
        Parent.__init__ (self, robotName, "freeflyer", load)
        self.tf_root = "base_link"
        self.leftAnkle = "lFoot"
        self.rightAnkle = "rFoot"

    def getInitialConfig (self):
        q = []
        for n in self.jointNames:
            dof = self.initPos [n]
            if type (dof) is tuple:
                q += dof
            else:
                q.append (dof)
        return q

    def getStandingConfig (self):
        q = []
        for n in self.jointNames:
            dof = self.standing [n]
            if type (dof) is tuple:
                q += dof
            else:
                q.append (dof)
        return q

    def getSittingConfig (self):
        q = []
        for n in self.jointNames:
            dof = self.sitting [n]
            if type (dof) is tuple:
                q += dof
            else:
                q.append (dof)
        return q
