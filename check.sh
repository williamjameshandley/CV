#!/bin/zsh

diff <(cat 'publications.tex' | grep -o '{.*}' | cut -c2-  | rev | cut -c2- | rev | sort -u ) <(grep '@' papers_raw.bib | grep -o '{.*' | cut -c2-  | rev | cut -c2- | rev | sort -u)

