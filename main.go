package main

import (
	"fmt"
	"os"

	"github.com/rs/zerolog"
	"github.com/spf13/pflag"
)

var (
	version   = ""
	buildTime = ""
)

func init() {
	// Loads from configuration file, if it exists

	pflag.Usage = func() {
		fmt.Fprintf(os.Stderr, `To Do`)
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
		pflag.PrintDefaults()
	}

	//pflag.Bool("debug", false, "Sets log level to debug.")
	pflag.Parse()

	zerolog.SetGlobalLevel(zerolog.InfoLevel)
}

func main() {
	base := int64(4)
	exp := int64(13)
	modulus := int64(497)

	fmt.Println(ModExpGoBigInteger(base, exp, modulus))
	fmt.Println(ModExpGoBigIntegerExp(base, exp, modulus))
	fmt.Println(ModExp(base, exp, modulus))
	fmt.Println(ModExpWithSquaring(base, exp, modulus))
}
