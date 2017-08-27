package main

import (
	"context"
	"fmt"
	"math/big"
	"time"

	"github.com/rs/zerolog/log"
)

func encryption(ctx context.Context, message *big.Int, coins *Coins) (cipher *big.Int) {
	defer func(begin time.Time) {
		log.Ctx(ctx).Debug().
			Int64("latency(ns)", time.Since(begin).Nanoseconds()).
			Str("plain_text", fmt.Sprintf("%v", message)).
			Str("cipher", fmt.Sprintf("%v", cipher)).
			Msg("Message encrypted")
	}(time.Now())

	pk := coins.PrivateKey

	hr := new(big.Int).Exp(coins.G, coins.R, nil)
	term := new(big.Int).Add(big.NewInt(1), new(big.Int).Mul(message, pk.N))
	mod := new(big.Int).Mod(term, new(big.Int).Mul(pk.N, pk.N))
	cipher = new(big.Int).Mul(hr, mod)
	return
}

func decryption(ctx context.Context, cipher *big.Int, coins *Coins) (message *big.Int) {
	defer func(begin time.Time) {
		log.Ctx(ctx).Debug().
			Int64("latency(ns)", time.Since(begin).Nanoseconds()).
			Str("cipher", fmt.Sprintf("%v", cipher)).
			Str("plain_text", fmt.Sprintf("%v", message)).
			Msg("Message decrypted")
	}(time.Now())

	pk := coins.PrivateKey

	hr := new(big.Int).Exp(coins.G, coins.R, nil)
	term := new(big.Int).Sub(new(big.Int).Div(cipher, hr), big.NewInt(1))
	quo := new(big.Int).Div(term, pk.N)
	message = new(big.Int).Mod(quo, new(big.Int).Mul(pk.N, pk.N))
	return
}
