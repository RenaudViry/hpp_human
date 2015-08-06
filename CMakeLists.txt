#
# Copyright (c) 2015 CNRS
# Authors: Renaud Viry
#
#
# This file is part of hpp_human
# hpp_human is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_human is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_human  If not, see
# <http://www.gnu.org/licenses/>.

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/python.cmake)


SET(PROJECT_NAME hpp_human)
SET(PROJECT_DESCRIPTION
  "Python and ros launch files for Human in hpp."
  )
SET(PROJECT_URL "")

SETUP_PROJECT()

# Catkin stuff
#FIND_PACKAGE(catkin REQUIRED COMPONENTS
#  hpp_ros)
#CATKIN_PACKAGE()

FINDPYTHON()
ADD_REQUIRED_DEPENDENCY("hpp-corbaserver >= 3")
ADD_REQUIRED_DEPENDENCY("human_model")
#ADD_REQUIRED_DEPENDENCY("hpp_ros")

INSTALL (FILES
  src/hpp/corbaserver/human/robot.py
  src/hpp/corbaserver/human/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/human
  )

#SET(CATKIN_PACKAGE_SHARE_DESTINATION
#  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})

#INSTALL(FILES launch/human.launch
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
#  )

#INSTALL(FILES rviz/config.rviz
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rviz
#  )

SETUP_PROJECT_FINALIZE()
