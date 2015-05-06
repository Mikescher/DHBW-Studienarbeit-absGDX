lualatex main.tex -synctex=0
bibtex bu1.aux
bibtex bu2.aux
lualatex main.tex -synctex=0
lualatex main.tex -synctex=0

@PAUSE