# Analyse des SI d'entreprise — M2 SIA

Projet de préparation à l'examen, centré sur **Organisation de courses de fond** (TD final).

## Livrables

- [`dist/PACK_IMPRESSION_ASI.pdf`](dist/PACK_IMPRESSION_ASI.pdf) : **fichier unique prêt à imprimer**, regroupant corrigé intégral, révision, examen blanc avec solution, dans cet ordre ; généré automatiquement.

- [`dist/Corrige_Integral_Courses_de_Fond_9_Questions.pdf`](dist/Corrige_Integral_Courses_de_Fond_9_Questions.pdf) : **corrigé complet, indépendant et imprimable des neuf questions du TD final**, avec planches N1 (internet, guichet, courrier, club), classes, états, DCP, communication et N3. Modèle pédagogique **non officiel**.

- [`dist/Revision_ASI_Courses_de_fond.pdf`](dist/Revision_ASI_Courses_de_fond.pdf) : fiche complète en français simple **avec les neuf questions du TD, une **description textuelle détaillée** et les diagrammes**.
- [`dist/Examen_Blanc_ASI_Corrige.pdf`](dist/Examen_Blanc_ASI_Corrige.pdf) : examen blanc difficile, un seul sujet, cinq questions, une description textuelle détaillée corrigée et schémas UML.

## Modifier et reconstruire

Les sources éditables sont :

- [`sources/corrige_integral.tex`](sources/corrige_integral.tex) : source autonome du corrigé intégral (inclut `td_courses_complet.tex`).
- [`sources/revision.tex`](sources/revision.tex)
- [`sources/td_courses_complet.tex`](sources/td_courses_complet.tex) : **corrigé des neuf travaux, à modifier en priorité**.
- [`sources/examen_blanc.tex`](sources/examen_blanc.tex)

Pour produire **les trois PDF** localement : `make pdf` (XeLaTeX, latexmk et police Carlito).

Sur GitHub, chaque push sur la branche de ce projet déclenche la compilation et place les nouveaux PDF dans `dist/` ; un artefact téléchargeable est également généré. Évitez de modifier directement les PDF : modifiez les fichiers `.tex`.

## Source et limites

Références : cours ASI_C1 à ASI_C5, TD *Organisation de courses de fond*, TD *Location de véhicules*. Les sujets et corrigés sont **pédagogiques et non officiels** ; les hypothèses ajoutées sont signalées. Le TD original du professeur n'est pas recopié dans ce dépôt.

Priorités annoncées à l'examen : cas d'utilisation, N1, classes et paquetages, états, DCP, N3 (MVC). Communication et autres sujets sont complémentaires pour les TD.

## Contrôle de qualité

Lire [QA_SOURCE.md](QA_SOURCE.md) pour les règles vérifiées face aux cours, la distinction faits / hypothèses et les limites du corrigé. `make verify` contrôle les PDF, la présence des sections, les 9 tâches du TD et le barème 20 points.