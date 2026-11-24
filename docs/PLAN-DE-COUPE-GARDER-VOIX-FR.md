# Ajouter un plan de coupe à une interview sans couper la voix

Vous avez tourné un plan de détail et vous voulez le montrer à un moment précis d’une interview. Superposez l’image du plan de coupe à celle de l’interview. Coupez le son du plan ajouté, gardez la voix sur sa piste et vérifiez les deux raccords dans le MP4 téléchargé. Si vous comparez plusieurs monteurs IA, fournissez le même plan de coupe et la même consigne à chacun.

## Vérifier les raccords sur un vrai export

[Téléchargez le lecteur de comparaison](examples/plan-de-coupe-audio.html?raw=1) et ouvrez-le dans votre navigateur. Il lit les trois MP4 publics de l’exemple. Le fichier principal contient une phrase synthétique en anglais. L’image de départ montre ses mots et sa forme d’onde. Le plan de coupe montre trois échantillons de vert. Passez de la source à l’aperçu puis au MP4 exporté au même instant.

| Image à 25 i/s | Temps de montage | Image visible dans l’aperçu et le MP4 |
| --- | --- | --- |
| 63 | 2,52 s | Forme d’onde de la source |
| 64 | 2,56 s | Première image du plan de coupe |
| 92 | 3,68 s | Dernière image du plan de coupe |
| 93 | 3,72 s | Retour à la forme d’onde |

Les images sont numérotées à partir de zéro. À cette cadence, l’image qui commence à 3,68 s reste visible jusqu’au début de la suivante, à 3,72 s. Indiquez cette convention si votre cahier des charges fixe une fin précise.

Sur le MP4 public, le décodage de la voix en mono à 16 kHz entre 2,625 s et 3,55 s donne une corrélation de **0,9994** avec la source et un écart de niveau RMS inférieur à **0,003 dB**. Cette mesure porte sur le passage sous le plan de coupe. L’aperçu dure quatre secondes. Le MP4 de cet exemple historique contient également un carton de fin de cinq secondes. [Source](https://valmera.io/examples/filler-word-cut/original.mp4) · [Plan fourni](https://valmera.io/examples/b-roll-cutaway/print-swatches.mp4) · [Aperçu](https://valmera.io/examples/b-roll-cutaway/preview.mp4) · [MP4 final](https://valmera.io/examples/b-roll-cutaway/final.mp4) · [Mesures de relecture et empreintes des fichiers](examples/plan-de-coupe-mesures.json) · [Mesures lors du montage](https://valmera.io/examples/b-roll-cutaway/measurements.json)

## Choisir comment placer un plan fourni

| Outil | Ce que vous pouvez vérifier avec vos rushs |
| --- | --- |
| Valmera | Fournissez le fichier et indiquez l’intervalle ou la phrase. Demandez une incrustation d’image avec le son du plan ajouté coupé. Vérifiez l’aperçu et le fichier téléchargé. Le montage IA demande un abonnement adapté. [Fonctionnement et exemple](https://valmera.io/tools/add-b-roll) |
| Descript | Sa documentation montre comment remplacer un média dans une composition. Son connecteur MCP présente aussi une demande d’ajout de B-roll en préservant l’audio. Demandez un fichier précis, puis vérifiez ses deux raccords dans le projet et le MP4. [Remplacer un média](https://help.descript.com/visuals/replace-media) · [Connecteur Descript](https://www.descript.com/mcp) |
| CapCut | Son guide décrit l’importation des rushs et la pose du plan sur une piste vidéo au-dessus de l’interview. CapCut présente également des retouches de timeline dans ChatGPT. Vérifiez si votre fichier et vos deux timecodes sont respectés dans le flux choisi. [Plan de coupe et narration](https://www.capcut.com/features/how-to-add-b-roll-to-a-video-capcut-workflow) · [CapCut dans ChatGPT](https://www.capcut.com/features/chatgpt-video-editing-guide) |
| Adobe Premiere | Placez le plan sur une piste vidéo distincte. Utilisez le ciblage de piste et verrouillez la piste de voix pendant la retouche. Vérifiez le cadre, les raccords et la voix dans le MP4. [Cibler les pistes](https://helpx.adobe.com/fr/premiere/desktop/edit-projects/intro-to-editing/work-with-clips-on-the-timeline-using-track-targeting.html) · [Verrouiller une piste](https://helpx.adobe.com/fr/premiere/desktop/edit-projects/change-clip-sequence/track-lock-to-prevent-changes.html) |

Valmera publie ce guide. La comparaison s’appuie sur la documentation publique des éditeurs. Les mesures ci-dessus concernent l’exemple Valmera.

## Essayer avec votre propre interview

> Superpose **produit-plan-02.mp4** à l’interview de **00:18 inclus à 00:22 exclu**. Garde la voix de l’interview à son niveau actuel, coupe le son du plan ajouté et conserve la durée de la vidéo. Montre-moi l’aperçu, puis donne-moi le MP4 à vérifier.

1. Ouvrez le MP4 et regardez juste avant et juste après les deux raccords. Identifiez le plan utilisé et confirmez que le retour à l’interview se fait au bon mot.
2. Écoutez la phrase entière au casque. Une voix manquante, un son de plateau ajouté ou un changement brusque de niveau se repèrent plus facilement lors d’une écoute continue.
3. Demandez de déplacer le plan sur la phrase suivante. Comparez la nouvelle version à l’ancienne et comptez les retouches manuelles nécessaires avant approbation.

[Préparer un plan de coupe dans Valmera](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=plan_de_coupe_fr). Pour déléguer des montages récurrents, indiquez le nombre de vidéos mensuelles, la durée des rushs et le délai de validation dans votre [demande Enterprise](https://valmera.io/subscribe?inquiry=video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=plan_de_coupe_fr#enterprise).
