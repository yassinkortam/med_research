############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.signal import argrelextrema
from grapher import build_graph

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

    #Build a graph representation of the report
    root, nodes = build_graph(report)
    
    #Find the sections with headings that are the same or similar to the given headings
    # - Find the cosine similarity between the heading and the node name
    # - Add the node with the maximum similarity to the relevant sections
    # - choose a model that is fast and good for short phrases
    model = SentenceTransformer('all-mpnet-base-v2')
    relevant_nodes = {}
    for heading in headings:

        #Encode the given heading
        heading_embedding = model.encode(heading.strip().lower())

        #Encode the headings in the report
        report_node_hashes = sorted(nodes.keys())
        report_headings = [nodes[node_hash].name for node_hash in report_node_hashes]
        report_headings_embeddings = model.encode(report_headings)

        #Find the most similar heading
        similarities = cosine_similarity([heading_embedding], report_headings_embeddings)[0]
        closest_node_hash = report_node_hashes[np.argmax(similarities)]

        #Find the node with the maximum similarity
        relevant_node = nodes[closest_node_hash]

        #Do a BFS to find all the text in nodes that are connected to the relevant node
        relevant_text = ""
        queue = [relevant_node]
        while queue:
            node = queue.pop(0)
            relevant_text += node.name + ":\n"
            relevant_text += node.text
            for child in node.children:
                queue.append(child)
        relevant_nodes[heading] = relevant_text

    #Return a Dict with the sections
    return relevant_nodes