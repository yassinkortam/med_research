############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import pandas as pd

def writer(data, destination):
    '''
    Write the given Series of DataFrames to a given source file.
    :type data: DataFrame
    :type destination: str
    '''
    try:
        data.to_excel(destination)
        data
    except FileNotFoundError:
        raise FileNotFoundError("The given destination file does not exist")
