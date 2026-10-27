.PHONY: pdf clean verify
pdf:
	mkdir -p dist build
	cd sources && latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=../build revision.tex
	cd sources && latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=../build examen_blanc.tex
	cp build/revision.pdf dist/Revision_ASI_Courses_de_fond.pdf
	cp build/examen_blanc.pdf dist/Examen_Blanc_ASI_Corrige.pdf
verify:
	python3 scripts/verify_documents.py
	pdfinfo dist/Revision_ASI_Courses_de_fond.pdf | grep Pages
	pdfinfo dist/Examen_Blanc_ASI_Corrige.pdf | grep Pages
clean:
	rm -rf build