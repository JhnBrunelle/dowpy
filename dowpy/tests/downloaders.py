import os, requests
import threading
import time
import hashlib
import sys



def _createRange(value, numsplits):
    ranges= []
    for i in range(numsplits):
        if i == 0:
            ranges.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        else:
            ranges.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    return ranges
