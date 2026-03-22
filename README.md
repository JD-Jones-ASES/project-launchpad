# Scholastica Codex

*AI-Accelerated Educational Publishing*

A proof of concept demonstrating that a single developer with AI tools can produce a complete K-12 curriculum — 40+ textbooks, multimedia learning modules, and interactive instruments — in weeks instead of years.

## What This Is

**Scholastica Codex** is both a free educational library and a technology demonstration. It proves that human-AI collaboration can compress the educational publishing timeline by orders of magnitude while maintaining quality across diverse subjects and grade levels.

- **40+ complete textbooks** spanning mathematics, science, philosophy, history, literature, language, and religion
- **1,657 content sections** extracted and structured for multimedia transformation
- **Automated pipeline** from LaTeX source to YouTube classroom (video, quiz, study guide, flashcards)
- **9 interactive web apps** for subject-specific practice

## The Curriculum Factory

The core technology is an end-to-end pipeline:

```
LaTeX Textbook → JSON Extraction → NotebookLM Artifacts → YouTube/Forms Publishing
```

Each textbook chapter is automatically decomposed into sections, uploaded to Google NotebookLM, and transformed into:
- Video overviews (Explainer or Cinematic format)
- Auto-graded quizzes (Google Forms)
- Study guides (Markdown)
- Flashcard sets (JSON)
- Slide decks (PPTX)

The pipeline is resume-safe, quota-aware, and runs unattended overnight.

**Tools:** Claude Code (Anthropic), Google NotebookLM, YouTube Data API v3, Google Forms API, LaTeX/latexmk, Python

## Content Library

| Subject | Titles | Levels |
|---------|--------|--------|
| **Mathematics** | Math I & II, Algebra I & II, Business Math + 3 workbooks | Middle–High |
| **Life Skills** | Logic & Reasoning, Charts & Graphs, Financial Literacy, The Thinking Toolkit | Middle–High |
| **Science** | Discover Science, Intermediate Science (32 units each) | Middle–High |
| **History & Government** | We the People, History & Humanities I–III, War: A Debate | Middle–High |
| **Philosophy** | Plato I & II, Aristotle I–III, Descartes, Machiavelli, Nietzsche | High–University |
| **Language & Literature** | The Open Page, Spanish, Latin/Greek Roots, Shakespeare, Boccaccio, Mencken, Short Stories, Gatsby, Technical Writing, Five Children and It | Elementary–University |
| **Religion** | Religious Roundtable, Monasticism | High |
| **Special Interest** | Nourish: An MS-Friendly Cookbook | Adults |

Most titles include separate Student and Teacher editions.

## Deliberate Variety

The breadth of subject matter is intentional. This collection includes Classical Christian texts alongside secular history, Nietzsche alongside monasticism, Mencken's provocations alongside elementary reading companions. The variety demonstrates that the framework is content-agnostic — it handles any subject, any perspective, any grade level.

## Disclaimers

- **AI-Assisted Content:** All materials were created through human-AI collaboration and are provided as-is. Content may contain errors. Review and verify before classroom use.
- **Not Professional Advice:** These materials do not constitute professional educational, financial, medical, legal, or religious advice.
- **Perspective:** Several titles reflect a Classical Christian educational perspective. Others are secular or intentionally provocative. All perspectives should be examined critically.
- **Beta Release:** This collection is a work in progress. [Report errors via GitHub Issues](https://github.com/JD-Jones-ASES/project-launchpad/issues/new?title=Resource%20Error%3A%20).

## Licensing

| Content | License |
|---------|---------|
| Educational Instruments (web apps) | MIT License |
| Curricular Resources (textbooks) | CC BY-SA 4.0 |

All content is freely available for use, remix, and redistribution with attribution.

## Technologies

- HTML5, CSS3, vanilla JavaScript — no frameworks, no backend
- Google Fonts: Cinzel (display) & Crimson Text (body)
- LaTeX/latexmk for textbook typesetting
- Python for pipeline orchestration
- Claude Code (Anthropic) for authoring and automation
- Google NotebookLM for multimedia generation
- YouTube Data API v3 + Google Forms API for publishing

## Investment

This project seeks partners in AI or venture capital who see the opportunity in AI-accelerated educational publishing. The content is free. The capability is the product. [Get in touch via GitHub Issues](https://github.com/JD-Jones-ASES/project-launchpad/issues).

Copyright 2025-2026 JD Jones
