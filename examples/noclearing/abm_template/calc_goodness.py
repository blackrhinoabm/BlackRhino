#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Robustness check for Agent-Based Models
(conceivably other models as well)
across the whole of the multidimensional
parameter space.

Author: Pawel Fiedor (pawel@fiedor.eu)
        Co-Pierre Georg (cogeorg@gmail.com)

Version: 0.2

Date of last update: 19-11-2015 (Cape Town)

"""
if __name__ == '__main__':
    import sys
    from src.goodness import Goodness

    args = sys.argv

    if len(args) != 2:
        print "Usage: ./calc_goodness config_file_path.xml"
        sys.exit()

    goodness = Goodness()
    goodness.do_run(args[1])
