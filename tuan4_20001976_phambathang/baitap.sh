#!/bin/bash
pandoc --pdf-engine=xelatex -H "baitap.tex" --number-sections --listings "baitap.md" -s -o "20001981_PhamThiThuong.pdf"