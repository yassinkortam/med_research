############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import re
import numpy as np
from difflib import SequenceMatcher

# #NLP
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.signal import argrelextrema

#Currently, sections are found using regex 
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

    #Use sentence transformers to find the most similar headings
    model = SentenceTransformer('all-mpnet-base-v2')

    #Find the sections with headings that are the same or similar to the given headings
    relevant_sections = {}
    for heading in headings:
        #Encode the given heading
        heading_embedding = model.encode([heading.strip().lower()])

        #Encode the headings in the report
        report_headings = list(report_sections.keys())
        report_headings_embeddings = model.encode(report_headings)

        #Find the most similar heading
        similarities = cosine_similarity(heading_embedding, report_headings_embeddings)
        closest_heading = report_headings[np.argmax(similarities)]

        #Save the section with the most similar heading if it is not empty
        if report_sections[closest_heading] != []:
            relevant_sections[heading] = report_sections[closest_heading]
            
    #Return a DataFrame with the sections
    return relevant_sections