#!/usr/bin/env bash

/usr/local/bin/docker build -t rieh/latex .
/usr/local/bin/docker run --rm -i -v "$PWD":/data rieh/latex pdflatex seungmoon_rieh_resume.tex
