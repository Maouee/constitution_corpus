## Constitution de corpus
Dépôt pour le projet du cours d'Outils de Traitement de Corpus de M1 PluriTal (2023_2024)

## Tâche
Réalisation d'une tâche de synthèse d'un dialogue qui permet ensuite d'avoir le sujet principal du dialogue. (tâche de synthèse et tâche de génération de texte)

## Corpus 
DialogSum: A Real-Life Scenario Dialogue Summarization Dataset `knkarthick/dialogsum`. Corpus en langue anglaise de 13,460 dialogues avec leur résumé et le sujet principal manuellement annotées. 
- **Dialogues** -> récoltés à partir de trois corpus de dialogue public : Dailydialog, DREAM et MuTual, ainsi qu’un site Web de pratique de l'anglais. Les données sont donc des données réelles récupérées. Les dialogues ont pour sujets la vie quotidienne (la scolarité, le travail, les médicaments, les achats, les loisirs,les voyages etc.). La plupart des conversations ont lieu entre amis, collègues et entre les fournisseurs de services et les clients. Ils sont de longueur raisonnable.
- **Instances** -> dialogue : texte du dialogue / summary : résumé du dialogue écrit par un humain / topic : sujet du dialogue écrit par un humain / id : id unique d'un exemple.
- Lignes directives pour les annotateurs : transmettre l’information la plus importante; Être bref; Préserver les entités nommées importantes dans la conversation; Être écrit du point de vue d’un observateur; Être écrit dans un langage formel.
- **Licence** -> le coprus peut être exploité pour une utilisation non commerciale. Ils demandent néanmoins d'être cités.

## Modèles qui ont utilisé le corpus
Plusieurs modèles ont utilisé ce corpus. Ces modèles ont été entrainé sur ce corpus pour différentes tâches, certains pour de la synthèse, d'autres pour de la génération de texte (plus particulièrement de dialogues).
