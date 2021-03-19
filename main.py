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

import docx
import os
import sys
import re


def search_folder():
    docs = [doc for doc in os.listdir() if re.search(".docx$", doc)]
    if not len(docs):
        sys.exit("Error: No files found")
    return docs


def get_refs(filepath):
    try:
        doc = docx.Document(filepath)
    except:
        sys.exit("Error: No file found")

    return [p.text for p in doc.paragraphs
            if re.search("^.*, (‘|\"|').*.('|\"|’).*$", p.text)]


def conv_refs(refs_to_conv):
    for ref in refs_to_conv:
        tmp = []
        a, b = ref.split(",")
        a = a.split()
        b = b.replace(" ", ", ")
        for i in range(0, len(a) - 1, 1):
            tmp.append(a[i][0])
        tmp.append(a[-1])
        tmp.append(b)
        refs_to_conv[refs_to_conv.index(ref)] = " ".join(tmp)
    return refs_to_conv


def write_refs(refs_to_write, num):
    f = open("OUTPUT%s.txt" % num, "w")
    for ref in refs_to_write:
        f.write("%s\n" % ref)
    f.close()


def main(f, count):
    it_refs = get_refs(f)
    bib_refs = conv_refs(it_refs)
    write_refs(bib_refs, count)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc > 2:
        sys.exit("Error: too many values")
    elif argc == 1:
        files = search_folder()
        fcount = len(files)
        if fcount > 1:
            count = 1
        else:
            count = ""
        for f in files:
            main(f, count)
            if fcount > 1:
                count += 1
    else:
        main(sys.argv[1], "")
