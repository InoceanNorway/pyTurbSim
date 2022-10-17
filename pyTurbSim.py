#!/usr/bin/python
"""
This is the pyTurbSim 'executable script', which utilizes the
:mod:`pyts.runConfig` package.
"""

import sys
from pyts.runInput.main import readInput, run, write
import time


def runTurbsim(fname):


    config = readInput(fname)

    tm0 = time.time()
    tsdat = run(config)
    write(tsdat, config, fname)
    print 'TurbSim exited normally, runtime was %g seconds' % (time.time() - tm0)
fnames=['Turbsim9.inp','Turbsim11.inp' ,'Turbsim13.inp' ,'Turbsim25.inp' ]


if __name__=='__main__':
    import multiprocessing as mp
    pool=mp.Pool(4)
    pool.map(runTurbsim,fnames)
    pool.join()
    pool.close()

    runTurbsim(fnames[0])