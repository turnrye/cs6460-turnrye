all: coursework research paper catalog

.PHONY: research paper coursework catalog

research:
	cd survey-results && \
	python stats.py > analysis.md
paper:
	cd final-paper && \
	pandoc paper.md -o paper.pdf --template proceedings.tex --filter pandoc-citeproc --bibliography citations.bib --csl acm-sigchi-proceedings.csl 
coursework:
	cd coursework && \
	pandoc --filter pandoc-citeproc assignment-1.md -o assignment-1.pdf && \
	pandoc --filter pandoc-citeproc --bibliography assignment-2.bibtex assignment-2.md -o assignment-2.pdf && \
	pandoc --filter pandoc-citeproc assignment-3.md -o assignment-3.pdf && \
	pandoc --filter pandoc-citeproc --bibliography qualifier-question.bibtex qualifier-question.md -o qualifier-question.pdf && \
	pandoc --filter pandoc-citeproc --bibliography project-proposal.bibtex project-proposal.md -o project-proposal.pdf && \
	pandoc --filter pandoc-citeproc --bibliography milestone-1.bibtex milestone-1.md -o milestone-1.pdf && \
	pandoc --filter pandoc-citeproc --bibliography milestone-1.bibtex milestone-2.md -o milestone-2.pdf
project:
	pandoc --variable urlcolor=cyan README.md -o Catalog.pdf
