# NLP Enron Email Investigation
Analyse von E‑Mail‑Kommunikation mittels Natural Language Processing, Entity Extraction, Timelines, Heatmaps und Netzwerkgraphen.

## 📌 Projektüberblick
Dieses Projekt untersucht E‑Mail‑Kommunikation aus dem Enron‑Datensatz mithilfe moderner NLP‑Methoden. Ziel ist es, Personen, Organisationen und Orte zu extrahieren, Kommunikationsmuster sichtbar zu machen und zeitliche sowie strukturelle Beziehungen zwischen Akteuren aufzudecken.

Der Fokus liegt auf:

- Named Entity Recognition (NER)
- zeitlichen Analysen (Timelines)
- Heatmaps für Personen und Keywords
- Netzwerkgraphen zur Visualisierung von Beziehungen
- reproduzierbaren Python‑Pipelines
- professioneller Projektstruktur

Das Projekt dient als Data‑Science‑Portfolio‑Beispiel und zeigt, wie man unstrukturierte Textdaten in verwertbare Erkenntnisse transformiert.

## 🧰 Technologien & Methoden
- Python (pandas, numpy, matplotlib, seaborn)
- spaCy für Named Entity Recognition
- NetworkX für Netzwerkgraphen
- dateutil für robustes Datums‑Parsing
- Jupyter Notebooks für explorative Analysen
- Git & GitHub für Versionierung und Workflow

# 🔍 Kernfunktionen
## Named Entity Recognition (NER)
Extraktion und Bereinigung von Entitäten wie Personen, Organisationen und Orten. Die Entitäten werden mit den E‑Mails verknüpft, um zeitliche und strukturelle Analysen zu ermöglichen.

## Timeline‑Analysen
Visualisierung, wann bestimmte Personen oder Keywords erwähnt werden.
Beispiele:
- Kommunikationsspitzen
- Aktivitätsmuster

## Heatmaps für Personen und Keywords
Heatmaps zeigen, welche Personen an welchen Tagen besonders häufig erwähnt werden.
Dies ermöglicht:
- Erkennen von Schlüsselpersonen
- Identifikation von Ereignisclustern
- Mustererkennung über Zeit

## Netzwerkgraphen
Graphen visualisieren Beziehungen zwischen Personen basierend auf Co‑Occurrences, gemeinsamen E‑Mails oder gemeinsamen Erwähnungen.
