# Audit du pack ASI (27 octobre 2026)

## Références effectivement consultées

- **ASI_C1** : acteurs, cas d'utilisation, include/extend, description textuelle du retrait d'argent (p. 36), N1.
- **ASI_C2** : classes métier, relations, multiplicités, paquetages, cycle de vie et transitions `événement [garde] / action`.
- **ASI_C3** : DCP, MVC, séquences N3 et communications.
- **ASI_C4** : processus unifié, vision, risques, Scrum, agilité et SAFe.
- **ASI_C5** : 6 diagrammes prioritaires pour l'écrit, traçabilité des modèles, erreurs notées, 3 heures/20 points/5 questions.
- **Organisation de courses de fond**, TD final, 6 pages : **9 travaux** ; l'exemple d'examen est centré sur les mêmes compétences, non sur les mêmes questions garanties.
- **Location voitures** et autres TD : cas de contraste seulement, sans transporter leurs règles dans les courses.

## Vérifications du fond

| Point à vérifier | Décision retenue |
|---|---|
| Description textuelle | Identification, déclencheur, préconditions, scénario nominal, variantes, exceptions, postconditions et règles + un exemple long entièrement rédigé. |
| Inscription internet | Préinscription ≤ J-15 et quota non atteint ; paiement accepté puis certificat médical de moins d'un an, envoyé par courrier. |
| Paiement | Un paiement refusé entraîne l'annulation dans le flux internet. Ne pas confondre avec une préautorisation de la **location de voitures**. |
| Sur place | Tout doit être validé au moins 1 heure avant le départ ; aucune inscription de triathlon/vélo sur place. |
| Courrier | Finalisation au plus tard J-5 ; document manquant => conservation de l'étape et demande de pièce, pas annulation immédiate. |
| Club | Pour triathlon/vélo, inscription par club et licence au lieu de certificat. |
| Classement | Cinq meilleurs temps du club ; si ≤4 arrivés : club disqualifié. Recherche par dossard, nom, prénom, sexe, catégorie. |
| Chronométrage | Puce affectée au dossard, tronçons/antennes/passage, retour du transpondeur obligatoire. |
| DCP et N3 | Aucune liaison directe Dialogue–Entité ; entités aux mêmes noms que dans le domaine. |
| Examen blanc | Sujet inédit : 5 questions, 20 points. Question 1 contient explicitement la description textuelle. Son corrigé est distinct du sujet. |

## Hypothèses pédagogiques et limites

Les classes, leur affectation des règles, certains noms d'écran, les multiplicités non écrites par l'énoncé et les messages précis sont des choix de modélisation. Ils sont signalés H1... dans les documents. **Ces PDF ne sont pas des corrigés officiels.** Un diagramme montre les échanges utiles au niveau demandé : certains schémas compacts sont accompagnés de tables de messages pour le parcours complet.

## Génération

- Modifier `sources/revision.tex`, `sources/td_courses_complet.tex` ou `sources/examen_blanc.tex`.
- `make pdf` : XeLaTeX crée les deux PDF dans `dist/`.
- `make verify` : contrôle PDF, sections obligatoires et contenu du sujet.
- Chaque push sur `asi-revision-courses-de-fond` déclenche GitHub Actions et régénère les PDF téléchargeables depuis le dépôt. Garder les sources versionnées.


## Corrigé intégral autonome (nouveau)

- `sources/corrige_integral.tex` contient les neuf questions et les planches de clarification.
- La copie de 29 pages envoyée à M. Lahmer le 21 octobre 2026 a été retrouvée dans les courriels et comparée comme document personnel, sans la considérer comme un corrigé officiel.
- Les échanges physiques courrier et remise des pièces restent distincts des messages envoyés au SI.
- Après un refus en ligne, le scénario cesse ; une inscription par courrier peut rester ouverte pour régularisation avant J-5.
- Certaines planches séparent les phases pour lisibilité ; leurs branches de refus sont exclusives et ne déclenchent pas les phases suivantes.
- Le dossier garde les hypothèses affichées lorsque le cas ne fixe pas les cardinalités, écrans ou opérations internes.