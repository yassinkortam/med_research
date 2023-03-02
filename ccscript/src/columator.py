############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import re
from difflib import SequenceMatcher

# #NLP
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# from scipy.signal import argrelextrema

#Currently, sections are found using regex and sequence matcher for simplicity
#Ideally, sections would be found using NLP

#Readings
#https://medium.com/@npolovinkin/how-to-chunk-text-into-paragraphs-using-python-8ae66be38ea6
#https://www.sbert.net/examples/applications/semantic-search/README.html

def columator(report, headings):
    '''
    Columate information in a given report.

    Args:
        - str
        - list
    Returns:
        - dict
    '''

    #A report is divided into sections by headings
    #All the text between a heading and the next heading is a section
    #A heading can be found in the report if it satisfies the following:
    # - It is at the beginning of a line
    # - It is followed by a colon
    def sections(lines):
        '''
        Break up a report into sections.

        Args:
            - list

        Returns:
            - dict
        '''
        sections = {"":[]}
        prevheading = ""
        for line in lines:

            #Check if there is a heading
            raw_heading = re.findall("^.*:", line)
            if raw_heading:
                heading = raw_heading[0].strip().lower().replace(':', '')
                sections[heading] = []
                if line.replace(raw_heading[0], '').split() != []:
                    sections[heading].append(line.replace(raw_heading[0], ''))
                prevheading = heading

            #Save contents of each line under the previous heading
            else:
                if line.split() != []:
                    sections[prevheading].append(line)
        return sections
    
    #The sections with headings that are the same or similar to the given headings are saved
    #Split the report into lines
    lines = report.splitlines()

    #Break up the report into sections
    report_sections = sections(lines)

    #Find the sections with headings that are the same or similar to the given headings
    relevant_sections = {}
    for heading in headings:
        #Find the section with the most similar heading using SequenceMatcher
        closest_heading = max(report_sections.keys(), key=lambda x: SequenceMatcher(None, x, heading.strip().lower()).ratio())

        #Check if the closest heading is the same or similar to the given heading
        if SequenceMatcher(None, closest_heading, heading.strip().lower()).ratio() > 0.6:

            #Save the section with the most similar heading if it is not empty
            if len(report_sections[closest_heading]) > 0:
                relevant_sections[closest_heading] = report_sections[closest_heading]
    
    #Return a DataFrame with the sections
    return relevant_sections