# coding=utf-8


def cvt(n):
    c = ord(n)
    return '&#' + str(c) + ';'


print("Markdown 转义字符处理\n")
inPath = input("文件路径：")
outPath = inPath[0:-3] + 'md'
with open(r"" + inPath, 'r') as inLine, open(r"" + outPath, 'w', encoding='utf-8') as outLine:
    for s in inLine.readlines():
        s = s.replace('<', cvt('<')).replace('>', cvt('>')).replace('(', cvt('(')) \
            .replace(')', cvt(')')).replace('[', cvt('[')).replace(']', cvt(']')) \
            .replace('{', cvt('{')).replace('}', cvt('}')).replace('.', cvt('.')) \
            .replace('*', cvt('*')).replace('~', cvt('~')).replace('=', cvt('=')) \
            .replace('^', cvt('^')).replace('+', cvt('+')).replace('$', cvt('$'))
        outLine.write(s)
print("输出路径：" + outPath)
