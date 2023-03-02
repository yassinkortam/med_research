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
import textwrap


args = parser.parser().parse_args()
reports = scraper.scraper(args.source, args.headings, args.c)

#format the output in a pretty way
print("_"*100)
print()
for count, report in enumerate(reports):
    print("REPORT #", count+1)
    print()
    for heading in report.keys():
        output = ""
        for line in report[heading]:
            output += '\n'
            output += line
        prefix = heading.upper() + ": "
        preferredWidth = 100
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,subsequent_indent=' '*len(prefix))
        print(wrapper.fill(output))
        print()
    print("_"*100)
    print()
#writer.writer(data, args.destination)