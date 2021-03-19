#!/usr/bin/env python3

'''
Copyright 2021 Anthony Beckett

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import sys
import docx
import re


def get_refs(filepath):
    try:
        doc = docx.Document(filepath)
    except:
        return 1

    return [p.text for p in doc.paragraphs
            if re.search("^.*, (‘|\"|').*.('|\"|’).*$", p.text)]


def conv_refs(refs_to_conv):
    for ref in refs_to_conv:
        spl = ref.split(",")
        spl2 = spl[0].split()
        for name in spl2:
            for i in range(0, len(name), 1):
                name[i] = name[i][0]
                i += 1
    print(refs_to_conv)


def write_refs(refs_to_write):
    f = open("OUTPUT.txt", "w")
    for ref in refs_to_write:
        f.write("%s\n" % ref)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Error: not enough values")

    it_refs = get_refs(sys.argv[1])

    if it_refs == 1:
        sys.exit("Error: No file found")

    conv_refs(it_refs)
    write_refs(it_refs)
