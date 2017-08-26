# Deniable Encryption Makefile

VERSION    = $(shell cat VERSION)
BUILD_TIME = $(shell date +%FT%T%z)

# Set build flags
LDFLAGS = -ldflags "-X main.version=${VERSION} -X main.buildTime=${BUILD_TIME}"

BINARY = deniable

.PHONY: all
	all: $(BINARY)

$(BINARY): main.go VERSION vendor
	@echo "Building $(BINARY)..."
	CGO_ENABLED=0 go build -a -installsuffix cgo ${LDFLAGS} -o ${BINARY} main.go

vendor: Gopkg.lock Gopkg.toml
	@echo "Updating vendor/..."
	@echo "Installing/updating dep..."
	@go get -u -v github.com/golang/dep/cmd/dep
	dep ensure -v
	@touch vendor
	@echo "vendor/ is up to date"

.PHONY: run
run:
	go run ${LDFLAGS} *

.PHONY: clean
clean:
	rm -rf $(BINARY)