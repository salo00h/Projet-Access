#!/usr/bin/env python3
"""Contrôle de présence et de cohérence avant impression (pas validation pédagogique)."""
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = {
    'revision': root/'dist'/'Revision_ASI_Courses_de_fond.pdf',
    'examen': root/'dist'/'Examen_Blanc_ASI_Corrige.pdf',
    'corrige': root/'dist'/'Corrige_Integral_Courses_de_Fond_9_Questions.pdf',
}
checks = {
    'revision': [
        'Description textuelle détaillée', 'Préconditions', 'Postconditions',
        'Enchaînement nominal', 'Alternatives', 'Exceptions',
        'Organisation de courses de fond', 'DCP', 'Séquence N3',
        'Communication', 'Paquetages',
    ],
    'corrige': ['Organisation de courses de fond', 'Description textuelle', 'séquence N3', 'Communication', 'classes du domaine', 'Préconditions', 'Postconditions', 'Paquetages'],
    'examen': [
        'Description textuelle', 'Préconditions', 'Postcondition',
        'séquence système N1', 'Corrigé', 'N3',
    ],
}
for name, p in files.items():
    if not p.exists():
        raise SystemExit(f'ABSENT: {p}')
    info = subprocess.check_output(['pdfinfo', str(p)], text=True)
    n = int(re.search(r'^Pages:\s*(\d+)', info, re.M).group(1))
    if n < (20 if name == 'revision' else (17 if name == 'corrige' else 12)):
        raise SystemExit(f'PDF suspect ({n} pages): {p}')
    raw = subprocess.check_output(['pdftotext', '-layout', str(p), '-'], text=True)
    norm = ' '.join(raw.split()).lower()
    for word in checks[name]:
        if ' '.join(word.split()).lower() not in norm:
            raise SystemExit(f'MOT/SECTION MANQUANT ({name}): {word}')
    print(f'{name}: OK - {n} pages, sections et mots vérifiés : {p.name}')
tex = (root/'sources'/'examen_blanc.tex').read_text()
points = re.findall(r'\\subsection\*\{Question \d+ -- (\d+) points', tex)
if sum(map(int, points)) != 20 or len(points) != 5:
    raise SystemExit(f'BARÈME ERREUR: {points}')
td = (root/'sources'/'td_courses_complet.tex').read_text()
for i in range(1, 10):
    if not re.search(r'\\subsection\{' + str(i) + r'\.', td):
        raise SystemExit(f'TD QUESTION ABSENTE: {i}')
print('Barème: 5 questions, 20 points. TD: 9 travaux présents.')