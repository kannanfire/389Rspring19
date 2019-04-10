#!/usr/bin/env python2

import sys
import struct
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, sectionSize = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d" % int(sectionSize))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
start = 24
end = start+8
for i in range(0, sectionSize):
    stype, slen = struct.unpack("<LL", data[start:end])
    print("SECTION TYPE: %s" % hex(stype))
    print("SECTION LENGTH: %s" % int(slen))
    start = end
    end = start + int(slen)

    if slen > 0:
        if stype == 0x1 or stype == 0x2:
            value = struct.unpack("<{}s".format(slen), data[start:end])
            print("SECTION VALUE: %s" % str(value))
        elif stype == 0x3:
            value = struct.unpack("<{}L".format(slen/4), data[start:end])
            print("SECTION VALUE: %s" % str(value))
        elif stype == 0x4:
            value = struct.unpack("<{}LL".format(slen/8), data[start:end])
            print("SECTION VALUE: %s" % str(value))
        elif stype == 0x5:
            value = struct.unpack("<{}Q".format(slen/8), data[start:end])
            print("SECTION VALUE: %s" % str(value))
        elif stype == 0x6:
            if slen == 16:
                value = struct.unpack("<dd", data[start:end])
                print("SECTION VALUE: %s" % str(value))
            else:
                bork("Bad size! Got %s, expected 16" % slen)
        elif stype == 0x7:
            if slen == 4:
                value = struct.unpack("<{}s".format(slen), data[start:end])
                print("SECTION VALUE: %s" % str(value))
            else:
                bork("Bad size! Got %s, expected 4" % slen)
        elif stype == 0x8:
            value = "\\x89\\50\\4E\\47\\0D\\0A\\1A\\0A"
            temp = struct.unpack("<{}s".format(slen), data[start:end])
            value = value + str(temp)
            print("SECTION VALUE: %s" % value)
            file = open("section{}d.png".format(i), "w")
            file.write(value)
            file.close()
        elif stype == 0x9:
            value = "\\G\\I\\F\\8\\7\\a" + str(struct.unpack("<{}s".format(slen), data[start:end]))
            print("SECTION VALUE: %s" % value)
            file = open("section{}d.gif".format(i), "w")
            file.write(value)
            file.close()
        elif stype == 0xA:
            value = "\\G\\I\\F\\8\\9\\a" + str(struct.unpack("<{}s".format(slen), data[start:end]))
            print("SECTION VALUE: %s" % value)
            file = open("section{}d.gif".format(i), "w")
            file.write(value)
            file.close()
        else:
            bork("Bad type! Got %s" % hex(stype))

        start = end
        end = start + 8
