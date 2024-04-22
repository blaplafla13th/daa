#!/bin/bash
pandoc --pdf-engine=xelatex -H "baitap.tex" --metadata-file=meta.yaml --number-sections --listings "baitap.ipynb" -s -o "LT7_20001976_Phambathang.pdf"