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
    doc = docx.Document(filepath)
    return [p.text for p in doc.paragraphs
            if re.search("^.*, (‘|\"|').*.('|\"|’).*$", p.text)]


def conv_refs(refs_to_conv):
    for ref in refs_to_conv:
        ref.split()
    return 0


def write_refs(refs_to_write):
    f = open("OUTPUT.txt", "a+")
    for ref in refs_to_write:
        if not re.search('^{0}$'.format(re.escape(ref)), f.read(), flags=re.M):
            f.write("%s\n" % ref)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Error: not enough values")

    it_refs = get_refs(sys.argv[1])
    bib_refs = conv_refs(it_refs)
    # write_refs(bib_refs)
