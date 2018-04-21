# Temp code writing file, keeping it separate from __init__.py to avoid users calling unusable code
# Will be moved to __init__ to keep things pythonic

import os, requests
import threading
import time
import hashlib
import sys

# Main Downloading class
# Private
class _Dow:


    # Default
    def __init__(self, url):
        self.url = ""
        self.chunks = 0
        self.data = {}

    # Creates a range based on the number of splits
    def createRange(self, value, numsplits):
        ranges = []
        for i in range(numsplits):
            if i == 0:
                ranges.append(
                    '%s-%s' % (i, int(round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
            else:
                ranges.append('%s-%s' % (int(round(1 + i * value / (numsplits * 1.0), 0)), int(
                    round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
        return ranges

    # Downloads a chunk
    def downloadChunk(self, url, byteIndex, byteRange, retry=False):

        # Only send Range header if supported
        if (len(self.data) != 1):
            headers = {"Range": 'bytes=%s' % byteRange}

        # Download chunk, with a retry if something goes wrong
        start = time.time()
        try:
            data[byteIndex] = requests.get(url, headers=headers)
        except Exception:
            if (retry == True):
                print("Error retrying chunk %d, terminating program" % byteIndex)
            else:
                print("[!] Error downloading chunk %d, retrying download.." % byteIndex)
                downloadChunk(url, byteIndex, byteRange, True)

        end = time.time()
        print("\b\b - Complete: chunk %d took %s seconds to download" % (byteIndex, end - start))


# Single download, 1 chunk
# Public
class SingleDow(_Dow):

    def __init__(self, url=""):
        self.url = url
        self.chunks = 1



# Multi chunk download, 2+ chunks
# Public
class MutliDow(_Dow):

    def __init__(self, url="", chunks=2):
        self.url = url
        self.chunks = chunks

