#!/bin/bash
iconv -c -f CP1251 -t UTF-8 "$1" >"$2"