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
Created on Novemeber 1, 2018

author: Lucas Olivari
'''

import h5py
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp

####################################################################
#### COMBINE THE HORN-FREQUENCY MAPS INTO A SINGLE SET OF FREQUENCY 
#### MAPS. 
####################################################################

# ==================================================================
# BINGO PARAMETERS
# ==================================================================
number_horns = 1
number_channels = 30
nside = 128

# ==================================================================
# COMBINE MAPS: FILL THE PIXELS WITH THE MEAN OF ALL MEASUREMENTS IN 
# THAT PIXEL.
# ==================================================================
bingo_maps = np.zeros((number_channels, hp.nside2npix(nside)))
counts_total = np.zeros(hp.nside2npix(nside))
mask = np.zeros(hp.nside2npix(nside))

for i in range(number_horns):
    with h5py.File('./bingo_maps_horn_' + str(i) + '.hdf', 'r') as fp:
        bingo_map = fp['MAPS'].value
        counts = fp['COUNTS'].value
    bingo_maps += bingo_map[:, 0, :]
    counts_total += counts[0, 0, :]

mask = np.where(counts_total == 0, 1, counts_total)
bingo_maps = bingo_maps / mask

# ==================================================================
# OUTPUT: HDF5 FILE
# ==================================================================
h5f = h5py.File('bingo_maps.hdf', 'w')
h5f.create_dataset('MAPS', data=bingo_maps)
h5f.close()   
    
