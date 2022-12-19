import sys
import re

if len(sys.argv) < 2:
    print("Usage: python glyphsplitter <svg-file>")
    sys.exit()
with open(sys.argv[1], 'r') as r:
    content = r.read().replace("\n", "")
    isDuotone = content.find(
        "-primary") > 0 and content.find("-secondary") > 0 and content.find("Duotone") > 0
    glyphs = re.findall(
        r'<glyph.*?\s*?.*?/>', content)

    if isDuotone:
        size = int(len(glyphs)/2)
    else:
        size = len(glyphs)
    print("%d items found" % (size))
    input("press enter to continue...")
    for i in range(0, size):
        filename = re.search(r'glyph-name="([^"]+)"', glyphs[i])
        filename = filename.group(1) if filename else str(i + 1).rjust(3, '0')
        if isDuotone:
            filename = filename[:-8]
        print("glyph %d is %s" % (i, filename))
        with open(filename + ".svg", 'w') as w:
            w.write('<?xml version="1.0" standalone="no"?>\n')
            w.write(
                '<svg version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
            w.write(glyphs[i].replace(
                '<glyph', '<path style="fill: #8E44AD" transform="scale(1, -1) translate(0, -512)"') + '\n')
            if (isDuotone):
                w.write(glyphs[i+size].replace(
                    '<glyph', '<path style="fill: #3498DB" transform="scale(1, -1) translate(0, -512)"') + '\n')
            w.write('</svg>')
