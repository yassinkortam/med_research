############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import pandas as pd
import columator
from tqdm import tqdm

def scraper(source, headings, reports_column):
    '''
    Scrape columated data from a given column of reports in a source csv file.

    Args:
        - str
        - str
        - str
        
    Returns:
        - Series
    '''
    try:
        source_data = pd.read_excel(source)
    except FileNotFoundError:
        raise FileNotFoundError("The given source csv file does not exist")

    try:
        reports = pd.DataFrame(source_data)[reports_column]
    except KeyError:
        raise KeyError("The given column name does not exist in the source csv file")
    
    #insert a column for each heading into the source_data DataFrame
    reports_column_index = source_data.columns.get_loc(reports_column)
    for count, heading in enumerate(headings):
        source_data.insert(reports_column_index+count+1, heading, None)
    
    #columate the reports and insert the data into the source_data DataFrame
    print("Columating reports...")
    for count, report in tqdm(enumerate(reports)):
        if type(report) != str:
            continue
        data = columator.columator(report, headings)
        for heading in headings:
            source_data[heading][count] = data[heading]
    return source_data