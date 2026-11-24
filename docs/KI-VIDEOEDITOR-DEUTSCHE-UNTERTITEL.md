# Vorhandene Videos mit KI schneiden und deutsche Untertitel prüfen

Lade eine vorhandene Aufnahme hoch und beschreibe, was geschnitten werden soll. Gib bei Produktdemos und Schulungen auch die genaue Schreibweise von Schaltflächen, Namen und Fachbegriffen an. Prüfe anschließend das exportierte Video mit Ton und kontrolliere die Untertitel an derselben Stelle. Sobald du vor einem Satz Material entfernst, müssen dessen Untertitel auf der neuen Zeitachse erscheinen.

Wenn du eine separate SRT-Datei brauchst, prüfe diese Anforderung vor dem Abo. Eingebrannte Untertitel sind Teil des Bildes. Eine SRT-Datei lässt sich getrennt korrigieren und in einem kompatiblen Videoplayer ein- und ausblenden. [W3C-Leitfaden zu Untertiteln](https://www.w3.org/WAI/media/av/captions/)

## Zwei Sekunden kürzen und „Größe ändern“ richtig schreiben

Das Beispiel zeigt eine fiktive Produktoberfläche mit synthetischer deutscher Stimme. In der Quelle ist im zweiten Untertitel absichtlich **„Große ändern“** geschrieben. Im Schnitt wurden zwei Sekunden Pause entfernt, die Schreibweise wurde korrigiert und der zweite Untertitel um zwei Sekunden vorgezogen. Das Beispiel wurde lokal erstellt und dient als Testvorlage.

| Datei | Laufzeit | Beginn des zweiten Untertitels | Wortlaut |
| --- | ---: | ---: | --- |
| [Quelle als MP4](examples/deutscher-untertitel-schnitt/quelle.mp4) · [Quell-SRT](examples/deutscher-untertitel-schnitt/quelle.srt) | 10 s | 00:06,400 | „Große ändern“ |
| [Gekürztes MP4](examples/deutscher-untertitel-schnitt/gekuerzt.mp4) · [Korrigierte SRT](examples/deutscher-untertitel-schnitt/korrigiert.srt) | 8 s | 00:04,400 | „Größe ändern“ |

Im Player kannst du bei diesen MP4-Dateien die deutsche Untertitelspur auswählen. Die erste Zeile beginnt in beiden Dateien bei 00:00,400. Alle 240 dekodierten Bilder des kürzeren Videos stimmen mit den beibehaltenen Quellbildern überein. Die extrahierten Untertitelspuren stimmen jeweils mit der zugehörigen SRT-Datei überein. [Messwerte und Prüfsummen](examples/deutscher-untertitel-schnitt/messwerte.json)

## Welcher Editor passt zum gewünschten Export?

| Werkzeug | Was die Dokumentation beschreibt | Was du vor dem Abo prüfst |
| --- | --- | --- |
| **Valmera** | Vorhandene Videos nach Textanweisung schneiden, Vorschau prüfen, Untertitelschreibweise korrigieren und als MP4 exportieren. Studio brennt Untertitel ins Bild ein. Für eine separate SRT-Datei brauchst du einen eigenen Untertitel-Workflow. [Valmera-Dokumentation zu Untertiteln](https://valmera.io/docs/captions) | Prüfe an einem kurzen Clip den Schnitt, die korrekte Schreibweise und den sichtbaren Untertitel im MP4. KI-Bearbeitung in Studio erfordert ein Abo. |
| **Descript** | Video und Ton über das Transkript bearbeiten und Untertitel separat als SRT oder VTT ausgeben. [Descript-Dokumentation zum Untertitelexport](https://help.descript.com/hc/en-us/articles/10255811669773-Exporting-subtitles) | Exportiere das Video und die Untertitel aus derselben Komposition. Prüfe den zweiten Satz nach dem Schnitt. |
| **CapCut** | Transkriptbasierter Schnitt und automatische Untertitel. Der Umfang des SRT-Exports kann sich je nach Plattform und Version unterscheiden. [CapCut-Anleitung zum Schnitt](https://www.capcut.com/de-de/resource/ki-video-bearbeiten-schritt-fuer-schritt) · [CapCut-Hilfe zu Untertiteln](https://www.capcut.com/help/how-to-recognise-subtitles) | Prüfe den SRT-Export auf deinem Gerät und öffne die exportierte Datei getrennt vom Projekt. |
| **RenderHour** | KI-Schnitt vorhandener Clips und Download als MP4 mit separater SRT-Datei, wenn Untertitel aktiviert sind. [RenderHour-Hilfe](https://renderhour.com/de/help) | Bitte um eine gezielte Änderung am ersten Schnitt und kontrolliere, ob die neue SRT-Datei zur überarbeiteten Fassung passt. |

Die Tabelle stützt sich auf die Anbieter-Dokumentation. Wenn du eine deutschsprachige Bedienoberfläche brauchst, prüfe sie separat. Ein Editor kann deutschsprachiges Material bearbeiten, auch wenn seine Menüs in einer anderen Sprache angezeigt werden.

## Textanweisung für den Test

> Entferne nur die Pause von Sekunde 4 bis Sekunde 6. Lass beide gesprochenen Sätze und die gezeigte Schaltfläche vollständig erhalten. Schreib in den Untertiteln „Größe ändern“, genauso wie auf der Schaltfläche. Zeig mir die Vorschau. Der erste Untertitel soll bei 00:00,400 bleiben, der zweite bei 00:04,400 beginnen.

Passe den Wortlaut und die Zeiten an deine Aufnahme an. Wenn du nach einem Schnitt eine bestehende SRT weiterverwendest, verschiebe nur die betroffenen Zeilen. Eine globale Verschiebung um zwei Sekunden würde im Beispiel auch die korrekte erste Zeile verschieben. Sobald mehrere Stellen gekürzt werden, halte die letzte Schnittfassung fest und prüfe die Zeilen einzeln gegen das fertige Video.

Für die Freigabe reichen drei konkrete Fragen. Ist der Name der Schaltfläche richtig geschrieben? Beginnt die Zeile beim gesprochenen Satz? Gehören MP4 und SRT zur selben Version? Wenn der Zielplayer eine separate Untertiteldatei braucht, teste das Dateipaar dort und achte auf doppelt angezeigte Untertitel.

[Eigenes Video in Valmera bearbeiten](https://valmera.io/ai-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=ki_videoeditor_dach). Für regelmäßig anfallende Schulungs- oder Demovideos kannst du die Bearbeitung an Valmera Enterprise geben. Nenne bei der Anfrage die Videos pro Monat, die gewünschten Sprachen und ob ihr neben dem MP4 eine getrennte Untertiteldatei benötigt. [Bearbeitung für Unternehmen anfragen](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=ki_videoeditor_dach#enterprise)
