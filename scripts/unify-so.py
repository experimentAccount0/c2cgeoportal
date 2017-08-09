#!/usr/bin/python3

import re
import subprocess

files = subprocess.check_output(["find", "-name", "*.cpython-*.so"]).decode("utf-8").split()
re1 = re.compile("(.*)\.cpython-.*\.so")
re2 = re.compile(".*/([^/]*)\.so")
print(files)

for file_ in files:
    print(file_)
    print(re1.sub(r"\1.so", file_))
    print(re2.sub(r"\1.so", file_))
    print(["ln", "-s", re2.sub(r"\1.so", file_), re1.sub(r"\1.so", file_)])
    subprocess.check_call(["ln", "-s", re2.sub(r"\1.so", file_), re1.sub(r"\1.so", file_)])
