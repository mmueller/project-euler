#!/usr/bin/env python

import sys

def p29(limit):
    result = set()
    for a in range(2, limit+1):
        for b in range(2, limit+1):
            result.add(a**b)
    return result

def main(argv):
    try:
        limit = int(argv[1])
    except:
        print "Usage: %s <limit>" % argv[0]
        return 1
    result = p29(limit)
    print "Terms:", len(result)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
