#!/bin/bash
pandoc --pdf-engine=xelatex -H "baitap.tex" --metadata-file=meta.yaml --number-sections --listings "baitap.ipynb" -s -o "baitap.pdf"