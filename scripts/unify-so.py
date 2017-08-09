#!/usr/bin/python3

import re
import subprocess

files = subprocess.check_output(["find", "-name", "*.cpython-*.so"]).decode("utf-8").split()
re_ = re.compile("(.*)\.cpython-.*\.so")
print(files)

for file_ in files:
    print(file_)
    print(re_.sub(r"\1.so", file_))
    subprocess.check_call(["ln", "-s", file_, re_.sub(r"\1.so", file_)])
