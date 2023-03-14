############################################################################
#            COPYRIGHT (C) YASSIN KORTAM - ALL RIGHTS RESERVED             #
# UNAUTHORIZED COPYING OF THIS FILE, VIA ANY MEDIUM IS STRICTLY PROHIBITED #
#                       PROPRIETARY AND CONFIDENTIAL                       #
#    WRITTEN BY YASSIN KORTAM <YASSINKORTAM@G.UCLA.EDU>, MARCH 2023        #
############################################################################

import argparser
import scraper
import writer
import pandas as pd
import textwrap


args = argparser.argparser().parse_args()
data = scraper.scraper(args.source, args.headings, args.c)
if args.d == None:
    args.d = "columated_" + args.source
writer.writer(data, args.d)

# #format the output in a pretty way
# print("_"*100)
# print()
# for count, report in enumerate(reports):
#     print("REPORT #", count+1)
#     print()
#     for heading in report.keys():
#         output = ""
#         for line in report[heading]:
#             output += line
#         prefix = heading.upper() + ": "
#         preferredWidth = 100
#         wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,subsequent_indent=' '*len(prefix))
#         print(wrapper.fill(output))
#         print()
#     print("_"*100)
#     print()
# #writer.writer(data, args.destination)