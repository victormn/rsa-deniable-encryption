package main

import (
	"crypto/rand"
	"crypto/rsa"
	"math/big"
	random "math/rand"
)

// Coins setup structure
type Coins struct {
	PrivateKey *rsa.PrivateKey
	A          int64
	G          *big.Int
	H          *big.Int
	R          *big.Int
}

// CreateCoins setup the coins
func CreateCoins() *Coins {
	pk, err := rsa.GenerateKey(rand.Reader, 256)
	if err != nil {
		panic(err)
	}

	a := random.Int63() % 99999
	g := new(big.Int).Exp(big.NewInt(a), big.NewInt(2), new(big.Int).Mul(pk.N, pk.N))
	h := new(big.Int).Exp(g, big.NewInt(a), new(big.Int).Mul(pk.N, pk.N))

	return &Coins{
		PrivateKey: pk,
		A:          a,
		G:          g,
		H:          h,
		R:          big.NewInt(17),
	}
}
