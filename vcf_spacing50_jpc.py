#!/usr/bin/env python

"""
    usage:
        vcf_spacing50 [options] input_vcf output_vcf

    where the options are:
        -h,--help : print usage and quit
        -d,--debug: print debug information
"""

from __future__ import with_statement
from sys import argv, stderr, stdin, exit, stdout
from getopt import getopt, GetoptError


# do we want the debug information to be printed?
debug_flag = False


def spacing50(inputfile, outputfile):
    '''
    spacing 50
    '''
    data=[]
    spacing=50 #change if want different distance
    with open(inputfile, "r") as fp_file:
        fp=fp_file.readlines()
        data.append(fp[0])
        cpt_line=fp[0].split()
        for i in range(1, len(fp)):        
            pre_line=fp[i-1].split()
            curr_line=fp[i].split()
            if curr_line[0]==pre_line[0]:
                if int(curr_line[1])-int(cpt_line[1])>=spacing:
                    data.append(fp[i])
                    cpt_line=curr_line
            else:
                cpt_line=curr_line
                data.append(fp[i])
                
    with open(outputfile, "w") as fp1:
        fp1.writelines(data)

    print "Done"

if __name__ == "__main__":
    try:
        opts, args = getopt(argv[1:], "hd",["help", "debug"])
    except GetoptError, err:
        print str(err)
        print >> stderr, __doc__
        exit(2) 

    for o, a in opts:
        if o in ("-h", "--help"):
            print >> stderr, __doc__
            exit()
        elif o in ("-d", "--debug"):
            debug_flag = True
        else:
            assert False, "unhandled option"

    if len(args) != 2:
        print >> stderr, __doc__
        exit(3)

    spacing50(args[0], args[1])
