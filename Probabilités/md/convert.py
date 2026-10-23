"""Regénère chapitres/ProbaX.tex et chapitres/ProbaX_corrections.tex à partir des sources markdown.

Usage (depuis le dossier md/, avec pandoc 2.9 et pandoc-citeproc dans le PATH,
par exemple celui de l'environnement conda du projet) :

    python convert.py            # les cinq cours
    python convert.py III V      # certains cours seulement

Attention : les chapitres ne doivent être regénérés que tant qu'ils n'ont pas
été retouchés à la main (la conversion écrase les fichiers).
"""
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "chapitres"
COURSES = ["I", "II", "III", "IV", "V"]


def convert(course):
    cmd = [
        "pandoc", "-f", "markdown", "-t", "latex", "--no-highlight",
        "--lua-filter", "poly.lua",
        "--filter", "pandoc-citeproc",
        "--bibliography", f"bibliography{course}.json",
        "-M", "link-citations=true",
        f"Proba{course}.md",
    ]
    env = dict(os.environ, PROBA_COURSE=course)
    res = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, encoding="utf8", env=env)
    if res.returncode != 0:
        sys.exit(f"pandoc a échoué pour Probabilités {course}:\n{res.stderr}")
    tex = res.stdout.replace("\r\n", "\n")
    for line in res.stderr.splitlines():
        if not line.startswith("MACRO"):
            print(f"[{course}] {line}")

    # références bibliographiques : une cible par cours (les cinq bibliographies se recoupent)
    tex = tex.replace("{ref-", "{ref" + course + "-")

    # bloc de macros du markdown de Probabilités II, resté sous forme de texte entre deux "$" : déplacé dans le préambule
    tex = re.sub(r"\\\$\\newcommand.*?\\\$\n", "", tex, count=1, flags=re.S)

    # corrigés : mis à part (ils vont en fin de poly)
    m = re.search(r"%%SOLUTIONS-BEGIN%%\n(.*?)%%SOLUTIONS-END%%\n?", tex, re.S)
    if m:
        sol = m.group(1)
        tex = tex[:m.start()] + tex[m.end():]
    else:
        sol = ""
    return tidy(tex), tidy(sol)


def tidy(tex):
    """Recolle les marqueurs d'environnement au texte qui les suit (pas de ligne vide parasite)."""
    parts = re.split(r"(\n\n+)", tex)
    out = [parts[0]]
    for sep, unit in zip(parts[1::2], parts[2::2]):
        prev = out[-1]
        glue = False
        last_unit = prev.split("\n\n")[-1]
        if re.match(r"\\hypertarget\{[^}]*\}\{\}\Z", last_unit) and re.match(r"\\(addcontentsline|begin\{)", unit):
            glue = True
        elif re.match(r"\\addcontentsline\{toc\}\{subsection\}", last_unit) and unit.startswith("\\begin{"):
            glue = True
        elif re.match(r"\\begin\{(definition|theoreme|proposition|corollaire|lemme|remarque|exemple|preuve)\}", last_unit):
            glue = True
        elif last_unit.startswith("\\runinhead{") and not re.match(r"\\(begin|end|section|subsection|chapter|runinhead|\[|part)", unit):
            glue = True  # titre en ligne : même paragraphe que le texte qui suit
        elif unit.startswith("\\end{") and re.match(r"\\end\{(definition|theoreme|proposition|corollaire|lemme|remarque|exemple|preuve)\}", unit):
            glue = True
        out.append(("\n" if glue else sep) + unit)
    return "".join(out).strip() + "\n"


def main():
    courses = sys.argv[1:] or COURSES
    OUT.mkdir(exist_ok=True)
    for c in courses:
        body, sol = convert(c)
        for name, text in ((f"Proba{c}.tex", body), (f"Proba{c}_corrections.tex", sol)):
            with open(OUT / name, "w", encoding="utf8", newline="\n") as f:
                f.write(text)
        print(f"Probabilités {c}: {len(body.splitlines())} lignes, corrigés {len(sol.splitlines())} lignes")


if __name__ == "__main__":
    main()
