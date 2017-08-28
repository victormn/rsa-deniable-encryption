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

	m1 := big.NewInt(int64(9))
	m2 := big.NewInt(int64(10))

	keys := getKeys(32)
	logger.Debug().
		Str("sk_p", keys.PrivateKey.p.String()).
		Str("sk_q", keys.PrivateKey.q.String()).
		Str("sk_a", keys.PrivateKey.a.String()).
		Str("pk_N", keys.PublicKey.N.String()).
		Str("pk_g", keys.PublicKey.g.String()).
		Str("pk_h", keys.PublicKey.h.String()).
		Msg("Keys was created")

	c, r1, m1 := Encryption(ctx, m1, keys.PublicKey)
	Decryption(ctx, c, r1, keys)
	r2 := CollisionFinder(ctx, m1, m2, r1, keys)
	Decryption(ctx, c, r2, keys)
}
