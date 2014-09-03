import vim
import re

#class Line(object):
#
#    def __init__(self, line):
#        self.line = line
#    
#    @cached
#    @property
#    def indentLevel():
#        if not has

def switchTo3():
    mapRun('write', '!{} %'.format(var('s:py2exepath')))

def switchTo2():
    mapRun('write', '!{} %'.format(var('s:py3exepath')))

def isInClass():
    indentationLevel(line)

def defineFunction():
    if isInClass():
        pass
    else:
        pass

def defineClass():
    line = curline()
    xs = line.split()
    if len(xs) == 2:
        className, parentName = xs
    else:
        className, parentName = xs[0], 'object'
    indent = re.match('^(\s*).*', line).group(1)
    line = '{}class {}({}):'.format(indent, className, parentName)
    curline(line)
    emulate('A\<cr>\<cr>')