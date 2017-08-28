package main

import (
	"crypto/rand"
	"crypto/rsa"
	"math/big"
	random "math/rand"
)

// Keys ...
type Keys struct {
	PrivateKey *PrivateKey
	PublicKey  *PublicKey
}

// PrivateKey ...
type PrivateKey struct {
	p *big.Int
	q *big.Int
	a *big.Int
}

// PublicKey ...
type PublicKey struct {
	N *big.Int
	g *big.Int
	h *big.Int
}

func getKeys(l int) *Keys {
	sk, err := rsa.GenerateKey(rand.Reader, l)
	if err != nil {
		panic(err)
	}

	a := big.NewInt(random.Int63() % 100)
	privateKey := &PrivateKey{
		p: sk.Primes[0],
		q: sk.Primes[1],
		a: a,
	}

	n2 := new(big.Int).Mul(sk.N, sk.N)
	g := new(big.Int).Exp(a, big.NewInt(2), n2)
	h := new(big.Int).Exp(g, a, n2)
	publicKey := &PublicKey{
		N: sk.N,
		g: g,
		h: h,
	}

	return &Keys{
		PrivateKey: privateKey,
		PublicKey:  publicKey,
	}
}
