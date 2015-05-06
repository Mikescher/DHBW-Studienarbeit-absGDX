lualatex main.tex -synctex=0
bibtex bu1.aux
bibtex bu2.aux
bibtex bu3.aux
lualatex main.tex -synctex=0
lualatex main.tex -synctex=0

@PAUSE

START main.pdf