package main

import (
	"math/big"
)

func encryption(mIn *big.Int, pk *PublicKey) (cipher, r, mOut *big.Int) {
	//r = big.NewInt(random.Int63() % 50)
	r = big.NewInt(42)
	hr := new(big.Int).Exp(pk.h, r, nil)
	n2 := new(big.Int).Mul(pk.N, pk.N)
	mOut = mIn

	term := new(big.Int).Add(big.NewInt(1), new(big.Int).Mul(mIn, pk.N))
	mod := new(big.Int).Mod(term, n2)
	cipher = new(big.Int).Mul(hr, mod)
	return
}

func decryption(cipher, r *big.Int, keys *Keys) *big.Int {
	pk := keys.PublicKey
	//sk := keys.PrivateKey

	n2 := new(big.Int).Mul(pk.N, pk.N)
	hr := new(big.Int).Exp(pk.h, r, nil)

	term := new(big.Int).Sub(new(big.Int).Div(cipher, hr), big.NewInt(1))
	quo := new(big.Int).Div(term, pk.N)
	return new(big.Int).Mod(quo, n2)

}

func collisionFinder(m1, m2, r1 *big.Int, keys *Keys) *big.Int {
	sk := keys.PrivateKey
	pk := keys.PublicKey

	diff := new(big.Int).Sub(m1, m2)
	lambda := getLambda(sk)
	d := big.NewInt(1)

	term1 := new(big.Int).Mul(diff, d)
	base := new(big.Int).Mul(term1, lambda)

	term2 := new(big.Int).Mul(pk.N, lambda)
	modular := new(big.Int).Div(term2, big.NewInt(2))

	mod := new(big.Int).Mod(base, modular)
	return new(big.Int).Add(r1, mod)
}
