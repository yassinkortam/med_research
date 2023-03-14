############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import argparse
import re 

def argparser():
    '''
    Parse arguements for the ec.py program from the command line.

    Returns:
        - ArgumentParser
    '''
    def xlsx(arg_value, pat=re.compile(r"^[\w\-. ]+\.xlsx$")):
        '''
        Make sure that a given filename is valid and an xlsx

        Args:
            - str
            - Pattern[str]
        
        Returns:
            - str
        
        Raises:
            - ArgumentTypeError exception 
        '''
        if not pat.match(arg_value):
            raise argparse.ArgumentTypeError("file must be a xlsx with a valid filename")
        return arg_value
    
    def heading(arg_value, pat=re.compile(r"^[\w\-. ]")):
        '''
        Make sure that a given heading is valid

        Args:
            - str
            - Pattern[str]
        
        Returns:
            - str
        
        Raises:
            - ArgumentTypeError exception 
        '''
        if not pat.match(arg_value):
            raise argparse.ArgumentTypeError("file must be an xlsx with a valid filename")
        return arg_value
    
    parser = argparse.ArgumentParser(description='Automatically generate columated data from a column of plain text reports')
    parser.add_argument('-c', type=str, default='reports',
                        help='column name of the column containing plain text reports')
    parser.add_argument('-d', type=xlsx, default=None,
                        help='destination xlsx file to save columated data')
    parser.add_argument('source', metavar='src', type=xlsx, 
                        help='source xlsx file with plain text reports')
    parser.add_argument('headings', metavar='hdngs', type=heading, nargs='+',
                        help='headings for the columated data')
    return parser
