#!/usr/bin/python3
print(*["{:02d}".format(x) for x in range(100)], sep=", ")