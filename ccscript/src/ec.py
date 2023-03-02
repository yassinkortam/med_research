############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import parser
import scraper
import writer
import pandas as pd


args = parser.parser().parse_args()
reports = scraper.scraper(args.source, args.headings, args.c)
for report in reports:
    #format the output in a pretty way
    for heading in report.keys():
        output = ""
        for line in report[heading]:
            output += line
        print(heading, output, sep=":")
        print()
    print("*"*50)
#writer.writer(data, args.destination)