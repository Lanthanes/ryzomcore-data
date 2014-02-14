#!/usr/bin/python
# 
# \file directories.py
# \brief Directories configuration
# \date 2014-02-13 20:32GMT
# \author Jan Boon (Kaetemi)
# Python port of game data build pipeline.
# Directories configuration.
# 
# NeL - MMORPG Framework <http://dev.ryzom.com/projects/nel/>
# Copyright (C) 2014  by authors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

from buildsite import *
import os

# *** COMMON NAMES AND PATHS ***
CommonName = "data_game_share"
CommonPath = "shard/" + CommonName


# *** DIRECT SOURCE DIRECTORIES ***

# Copy dir directories
CopyDirectSourceDirectories = [ ]
CopyDirectSourceFiles = [ ]
fileList = os.listdir(DataShardDirectory + "/mirror_sheets")
for fileName in fileList:
	if fileName != ".svn" and fileName != ".." and fileName != "." and fileName != "*.*":
		if fileName.endswith(".dataset"):
			CopyDirectSourceFiles += [ DataShardDirectory + "/mirror_sheets/" + fileName ]


# *** SOURCE DIRECTORIES IN LEVELDESIGN ***
CopyLeveldesignSourceDirectories = [ ]
CopyLeveldesignSourceFiles = [ ]
CopyLeveldesignWorldSourceDirectories = [ ]
CopyLeveldesignWorldSourceFiles = [ ]
CopyLeveldesignDfnSourceDirectories = [ ]
CopyLeveldesignDfnSourceFiles = [ ]


# *** SOURCE DIRECTORIES IN THE DATABASE ***

# Copy dir directories
CopyDatabaseSourceDirectories = [ ]
CopyDatabaseSourceFiles = [ ]


# *** INSTALL DIRECTORIES IN THE CLIENT DATA ***

# Common data install directory
CopyInstallDirectory = CommonName