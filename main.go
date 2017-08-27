package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"math/big"
	"os"

	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/pflag"
	"github.com/spf13/viper"
)

var (
	version = ""
)

func init() {
	if version == "" {
		bytes, err := ioutil.ReadFile("VERSION")
		if err != nil {
			panic(err)
		}
		version = string(bytes)
	}

	pflag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Deniable encryption application to prevent brute-force attacks\n")
		fmt.Fprintf(os.Stderr, "Usage of:\n")
		pflag.PrintDefaults()
	}

	pflag.Bool("debug", false, "Sets log level to debug.")
	viper.BindPFlag("debug", pflag.Lookup("debug"))
	pflag.Parse()

	if !viper.GetBool("debug") {
		zerolog.SetGlobalLevel(zerolog.InfoLevel)
	}
}

func main() {
	ctx := context.Background()
	logger := log.With().Str("version", version).Logger()
	ctx = logger.WithContext(ctx)

	m := big.NewInt(int64(99999999))

	coins := CreateCoins()
	logger.Debug().
		Str("pk_d", coins.PrivateKey.D.String()).
		Int("pk_e", coins.PrivateKey.E).
		Str("pk_n", coins.PrivateKey.N.String()).
		Int64("a", coins.A).
		Str("g", coins.G.String()).
		Str("h", coins.H.String()).
		Msg("Coins was created")

	c := encryption(ctx, m, coins)
	decryption(ctx, c, coins)
}
