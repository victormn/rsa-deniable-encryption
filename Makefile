# Deniable Encryption Makefile

VERSION    = $(shell cat VERSION)

# Set build flags
LDFLAGS = -ldflags "-X main.version=${VERSION}"
SOURCES = $(shell find . -maxdepth 1 -name '*.go')

BINARY = deniable

all: $(BINARY)

$(BINARY):
	go build -o $(BINARY) ${LDFLAGS} $(SOURCES)

run: $(BINARY)
	./$(BINARY)