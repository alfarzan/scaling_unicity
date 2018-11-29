"""
This file extracts the time for each user in the data and puts the values
in a histogram
"""
import dataformat_utils as dut
import numpy as np
from tqdm import tqdm as tq
from functools import partial

u2p = dut.get_u2p()

lhrs = len(dut.get_date_array())
lants = len(dut.get_ant_array())

time_arr = np.zeros(lhrs)

get_track = partial(dut.get_user_track,  lants=lants)


for user in tq(u2p):

    tx = get_track(u2p[user])
    ti = tx[:, 0]
    time_arr[ti] += 1


np.save('../inputs/circadian.npy', time_arr)