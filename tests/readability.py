"""Rough Flesch-Kincaid grade for the S14 notice-decoder output in results.md.
Strips URLs, emails, phone numbers and the Source/disclaimer lines, since those
are fixed text rather than plain-language explanation."""
import re, pathlib

text = pathlib.Path(__file__).with_name("results.md").read_text()
block = text.split("## Full output: S14 (notice-decoder)")[1].split("### Reading level")[0]
lines = [l.lstrip("> ").strip() for l in block.splitlines()]
lines = [l for l in lines if l and not l.startswith(("**Source", "**This is general", "**What", "**Deadline", "**Where"))]
prose = " ".join(lines)
prose = re.sub(r"https?://\S+|\S+@\S+|\b[\d-]{7,}\b|\(TTY[^)]*\)|866-LEGLAID", "", prose)
prose = re.sub(r"[*_`]", "", prose)

sentences = max(1, len(re.findall(r"[.!?](\s|$)", prose)))
words = re.findall(r"[A-Za-z']+", prose)

def syllables(w):
    w = w.lower()
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 else 0)
    return max(1, n)

syl = sum(syllables(w) for w in words)
grade = 0.39 * len(words) / sentences + 11.8 * syl / len(words) - 15.59
print(f"words={len(words)} sentences={sentences} syllables={syl} FK grade={grade:.1f}")
