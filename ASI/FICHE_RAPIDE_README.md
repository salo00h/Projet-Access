# Fiche rapide UML — Analyse des SI d'entreprise

Résumé de 10 pages A4, en français simple, basé sur les cours ASI_C1, ASI_C2, ASI_C3, ASI_C5 et le TD *Organisation de courses de fond*.

## Contenu

- Cas d'utilisation
- Description textuelle détaillée (préconditions, postconditions, nominal, alternatives)
- Séquence système N1
- Classes du domaine et multiplicités
- Paquetages et états
- DCP (inscription sur internet et recherche de classement)
- Séquence N3 MVC
- Diagramme de communication
- Activité
- Checklist avant de rendre

## Construction locale

Prérequis : XeLaTeX, Graphviz (`dot`, `neato`), police Carlito.

```bash
# depuis le répertoire contenant fiche_rapide.tex et diagrams/
for f in diagrams/*.dot; do
  name="$(basename "$f" .dot)"
  case "$name" in
    usecases|classes|communication|activity) neato -n2 -Tpdf "$f" -o "diagrams/$name.pdf" ;;
    *) dot -Tpdf "$f" -o "diagrams/$name.pdf" ;;
  esac
done
xelatex -interaction=nonstopmode -halt-on-error fiche_rapide.tex
xelatex -interaction=nonstopmode -halt-on-error fiche_rapide.tex
```

Les diagrammes et les intitulés métier sont des exemples pédagogiques, pas un corrigé officiel ; les contraintes propres au sujet et les hypothèses figurent dans le texte.