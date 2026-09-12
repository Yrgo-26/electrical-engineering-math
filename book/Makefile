# Build the book: LuaLaTeX until the contents and the references settle, at most three passes.
#
#   make                   build elteknisk-matematik.pdf, the Swedish edition (also: make sv)
#   make en                build electrical-engineering-mathematics.pdf, the English edition
#   make VERSION=v1.1.0    the same, with the release's version on the title page
#   make clean             remove everything the build writes
#
# The lessons' images are typeset straight from their files under lectures/, so a change to one
# of those is a change to the book on the next build. Each edition's sources are in its own
# directory, sv/ and en/, and the two share the design, mathbook.sty and mathbook.lua, and the
# images.

ROOT       := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)
BOOK       := $(ROOT)/book
BUILD      := $(BOOK)/build
PDF        := elteknisk-matematik.pdf
PDF_EN     := electrical-engineering-mathematics.pdf
VERSION    ?=
LATEX      := lualatex -interaction=nonstopmode -halt-on-error -file-line-error \
              -output-directory=$(BUILD)

DESIGN     := mathbook.sty mathbook.lua
SOURCES_SV := sv/book.tex $(DESIGN) \
              $(wildcard sv/front/*.tex sv/chapters/*/*.tex sv/back/*.tex sv/back/*/*.tex)
SOURCES_EN := en/book.tex $(DESIGN) \
              $(wildcard en/front/*.tex en/chapters/*/*.tex en/back/*.tex en/back/*/*.tex)
IMAGES     := $(shell find $(ROOT)/lectures -name '*.png')

.PHONY: all sv en clean FORCE

all: $(PDF)

sv: $(PDF)

en: $(PDF_EN)

# The version the last build was made for. The file is rewritten only when VERSION changes, so a
# new version, or none after one, rebuilds the title page and nothing else does.
$(BUILD)/version: FORCE
	@mkdir -p $(BUILD)
	@echo '$(VERSION)' | cmp -s - $@ || echo '$(VERSION)' > $@

# $(call pass,JOB,MAIN): one LuaLaTeX pass over MAIN, writing $(BUILD)/JOB.pdf, with the version
# defined before anything is read.
pass = cd $(BOOK) && $(LATEX) -jobname=$1 '\def\bookversion{$(VERSION)}\input{$2}' >/dev/null \
       || (tail -40 $(BUILD)/$1.log; exit 1)

# $(call typeset,JOB,MAIN): the whole build of one edition. Every exercise links to the page of
# its answer, so a third pass is needed whenever the second moved an answer to another page.
define typeset
@mkdir -p $(BUILD)
$(call pass,$1,$2)
$(call pass,$1,$2)
@if grep -q "Rerun to get" $(BUILD)/$1.log; then \
    echo "cd $(BOOK) && lualatex ... (third pass)"; $(call pass,$1,$2); fi
@grep -E "^(Overfull|Underfull)|Warning" $(BUILD)/$1.log | sort | uniq -c | sort -rn | head -20 || true
@! grep -q "There were undefined references" $(BUILD)/$1.log || \
    (grep "undefined" $(BUILD)/$1.log | sort -u | head -20; \
     echo "error: undefined references; see $(BUILD)/$1.log"; exit 1)
cp $(BUILD)/$1.pdf $@
endef

$(PDF): $(SOURCES_SV) $(IMAGES) $(BUILD)/version
	$(call typeset,book-sv,sv/book.tex)

$(PDF_EN): $(SOURCES_EN) $(IMAGES) $(BUILD)/version
	$(call typeset,book-en,en/book.tex)

clean:
	rm -rf $(BUILD) $(PDF) $(PDF_EN)
