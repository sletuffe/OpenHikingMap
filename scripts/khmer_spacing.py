#!/usr/bin/env python3
"""Duplicate the Mapnik style rules that have a non-zero character-spacing on [name] text.

Khmer is a cluster-based script: the character-spacing applied by Mapnik between
each glyph splits subscript consonants from vowels (unreadable text).
For each affected rule we generate:
  - the original rule, restricted to names WITHOUT any Khmer character (Latin rendering unchanged)
  - a copy, restricted to names containing Khmer, with character-spacing="0"
Rules with horizontal-alignment="adjust" (lake and river names) are handled the
same way: the Khmer copy drops the alignment (the name is no longer stretched) and
adds spacing="300", which repeats the name along the axis of the lake. With
horizontal-alignment="middle" the name would only be shown once, in the middle of the lake.
<ElseFilter/> rules are converted to an explicit filter (negation of the previous
filters of the same scale range) because Mapnik cannot combine Else and Filter.

Idempotent: a file that was already processed (KHMER-SPACING marker) is skipped.
Usage: scripts/khmer_spacing.py styles/*.xml
"""
import re, sys

KH = "[name].match(\x27.*[\\x{1780}-\\x{17FF}].*\x27)"
REPEAT = 300  # distance (px) between two repetitions of a Khmer lake name
ADJUST = "horizontal-alignment=\"adjust\""  # stretches the text along the line: scatters Khmer clusters
MARK = "<!-- KHMER-SPACING: rules duplicated by scripts/khmer_spacing.py -->"
SPACING = re.compile(r"character-spacing=\"([^\"]*)\"")

def nonzero_spacing(rule):
    return any(v not in ("0", "0.0", "") for v in SPACING.findall(rule))

def scale_key(rule):
    return tuple(re.findall(r"&(?:max|min)scale_zoom\d+;", rule))

def get_filter(rule):
    m = re.search(r"<Filter>(.*?)</Filter>", rule, flags=re.S)
    return m.group(1).strip() if m else None

def with_filter(rule, expr):
    """Replace or insert the rule's filter with expr."""
    if "<ElseFilter/>" in rule:
        return rule.replace("<ElseFilter/>", "<Filter>%s</Filter>" % expr)
    if "<Filter>" in rule:
        return re.sub(r"<Filter>.*?</Filter>", lambda m: "<Filter>%s</Filter>" % expr, rule, count=1, flags=re.S)
    return rule.replace("<TextSymbolizer", "<Filter>%s</Filter>\n\t\t<TextSymbolizer" % expr, 1)

def process_style(style):
    rules = re.findall(r"<Rule>.*?</Rule>", style, flags=re.S)
    previous = {}  # scale range -> filters of the previous rules
    out = style
    for rule in rules:
        key = scale_key(rule)
        flt = get_filter(rule)
        is_else = "<ElseFilter/>" in rule
        concerned = (nonzero_spacing(rule) or ADJUST in rule) and "[name]" in rule
        if concerned:
            if is_else:
                prev = previous.get(key, [])
                base = " and ".join("not (%s)" % p for p in prev) or "true"
            else:
                base = flt
            if base is None:
                normal = with_filter(rule, "not %s" % KH)
                khmer = with_filter(rule, KH)
            else:
                normal = with_filter(rule, "(%s) and not %s" % (base, KH))
                khmer = with_filter(rule, "(%s) and %s" % (base, KH))
            khmer = SPACING.sub("character-spacing=\"0\"", khmer)
            if ADJUST in khmer:
                # without "adjust" Mapnik repeats the name along the axis (spacing, in pixels)
                khmer = khmer.replace(ADJUST + " ", "").replace(ADJUST, "")
                khmer = khmer.replace("placement=\"line\"", "placement=\"line\" spacing=\"%d\"" % REPEAT, 1)
            out = out.replace(rule, normal + "\n" + khmer, 1)
        if flt is not None and not is_else:
            previous.setdefault(key, []).append(flt)
    return out

def main(files):
    for fn in files:
        s = open(fn, encoding="utf-8").read()
        if MARK in s:
            print("%s : already processed" % fn); continue
        before = s.count("<Rule>")
        out = re.sub(r"<Style .*?</Style>", lambda m: process_style(m.group(0)), s, flags=re.S)
        if out != s:
            out = (MARK + "\n" + out) if not out.startswith("<?xml") else re.sub(r"(<\?xml[^>]*\?>\n?)", lambda m: m.group(1) + MARK + "\n", out, count=1)
            open(fn, "w", encoding="utf-8").write(out)
        print("%s : %d -> %d rules" % (fn, before, out.count("<Rule>")))

if __name__ == "__main__":
    main(sys.argv[1:])
