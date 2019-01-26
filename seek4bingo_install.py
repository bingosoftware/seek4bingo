'''
Created on November 1, 2018

author: Lucas Olivari
'''

import os

######################################################################
#### THIS IS THE SCRIPT WILL MODIFY SEEK SO IT CAN BE USED FOR BINGO
######################################################################

# ==================================================================
# CHOOSE DESTINATION AND WORKING PATHS
# ==================================================================

destination_path = '~/anaconda2/lib/python2.7/site-packages/seek-0.1.0-py2.7.egg/' # change to your destination (the place where your seek package is located within your python repository)

working_path = '/home/lucas/Documentos/work/seektest/seek/' # change to your working path (the place where your seek stuff are located)

# ==================================================================
# COPYNG STUFF AROUND
# ==================================================================

dfile = 'files/run_seek.py'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/plot_map.py'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/combine_horn_maps.py'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/bingo.py'
os.system('cp ' + dfile + ' ' + working_path + 'seek/config/')

dfile = 'files/make_fake_bingo_model_1.py'
os.system('cp ' + dfile + ' ' + working_path + 'seek/data/')

dfile = 'files/make_fake_bingo_model_2.py'
os.system('cp ' + dfile + ' ' + working_path + 'seek/data/')

dfile = 'files/load_data.py'
os.system('cp ' + dfile + ' ' + destination_path + 'seek/plugins/')
os.system('cp ' + dfile + ' ' + working_path + 'seek/plugins/')

