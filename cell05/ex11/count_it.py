#!/usr/bin/env python3

import sys

J=1

if len(sys.argv) > 1:   
    x =sys.argv[1:]
    print(f"parameters: {len(x)}")
    for i in x: 
        cti = len(i)
        print(f"{sys.argv[J]}: {cti}")
        J+=1
else:
    print("none")
