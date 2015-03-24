import urllib.request
import re

MARKDOWN_URL = 'https://raw.githubusercontent.com/Mikescher/absGDX/master/QuickGuide.md'
TEX_FOLDER = 'E:/Eigene Dateien/Dropbox/Programming/Latex/DHBW-Studienarbeit-absGDX';

mdown = urllib.request.urlopen(MARKDOWN_URL).read().decode('utf-8')

mdown = mdown.replace("_", "\\_")

mdown = re.sub(
    r'(~~~+|```+)(java|groovy|xml)([\s\S]*?)(~~~+|```+)', 
    "\n" + r'\doinline' + "\n" + r'\\begin{lstlisting}[caption=Markdown Tutorial: fenced code block, title=\\hspace{0 pt}, language=\2]'  + "\n" + r'\3' + "\n" + r'\\end{lstlisting}' + "\n", 
    mdown)

while (re.search(r'((^ - .*$)\r?\n){2,}', mdown, flags=re.M) != None):
    list = re.search(r'((^ - .*$)\r?\n)+', mdown, flags=re.M).group()
    repl = "\n" + "\\begin{itemize}" + "\n"
    for item in re.findall(r'^ - (.*)$', list, flags=re.M):
        repl += "\n" + "\\item " + item
    repl += "\n" + "\\end{itemize}" + "\n" + "\n"
    mdown = mdown.replace(list, repl)

mdown = re.sub(r'\*\*([^\r\n*]+)\*\*', r'\\textbf{\1}', mdown)
mdown = re.sub(r'\*([^\r\n*]+)\*', r'\\textit{\1}', mdown)

mdown = re.sub(r'^([^\r\n]*)\r?\n===+', "\n" + r'\\subsection{\1}' + "\n", mdown, flags=re.M)
mdown = re.sub(r'^###[ ]*(.*)', "\n" + r'\\subparagraph{\1}' + "\n", mdown, flags=re.M)
mdown = re.sub(r'^##[ ]*(.*)', "\n" + r'\\paragraph{\1}' + "\n", mdown, flags=re.M)
mdown = re.sub(r'^#[ ]*(.*)', "\n" + r'\\subsubsection{\1}' + "\n", mdown, flags=re.M)

mdown = re.sub(r'`([^`\r\n]+)`', r'\\fcolorbox{mdlightergray}{mdlightergray}{\1}', mdown)
mdown = re.sub(r'\[([^\[\]\r\n]+)\]\(([^\(\)\r\n]+)\)', r'\hyperlink{\2}{\1}', mdown)

mdown = re.sub(r'(\r?\n)(\r?\n)', r'\1', mdown)

mdown = "Der folgende Paragraph wurde automatisiert generiert. Für eine passendere Darstellung sehen Sie sich bitte das gerenderte Markdown direkt (z.B: auf GitHub) an." + "\n\n" + mdown

with open(TEX_FOLDER + "/content/tutorial.tex", "w") as texfile:
    texfile.write(mdown)
    
print("SUCESS.")