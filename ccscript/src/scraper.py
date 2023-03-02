############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import pandas as pd
import columator

def scraper(source, headings, reports_column):
    '''
    Scrape columated data from a given column of reports in a source csv file.

    Args:
        - str
        - str
        
    Returns:
        - Series
    '''
    try:
        source_data = pd.read_csv(source)
    except FileNotFoundError:
        raise FileNotFoundError("The given source csv file does not exist")

    try:
        reports = pd.DataFrame(source_data)[reports_column].dropna()
    except KeyError:
        raise KeyError("The given column name does not exist in the source csv file")
    
    reports = reports.apply(lambda x: columator.columator(x, headings))
    return reports