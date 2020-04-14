rm report.bbl report.blg report.log report.aux
pdflatex report.tex
bibtex report
pdflatex report.tex
pdflatex report.tex
