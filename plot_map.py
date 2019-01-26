# SEEK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SEEK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SEEK.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on October 1, 2018

author: Lucas Olivari
'''

import h5py
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp

####################################################################
#### EXAMPLE OF HOW TO HANDLE HDF5 FILES
####################################################################

with h5py.File("./bingo_maps_horn_0.hdf", 'r') as fp:
    bingo_map = fp['MAPS'].value
    counts = fp['COUNTS'].value

bingo_map[counts==0] = hp.UNSEEN
hp.mollview(bingo_map[0, 0, :])#, cmap="gist_earth")
plt.savefig("map_0.png")
plt.close()

hp.mollview(bingo_map[1, 0, :])#, cmap="gist_earth")
plt.savefig("map_1.png")
plt.close()  
