package main

import (
	"math/big"
)

func getLambda(sk *PrivateKey) *big.Int {
	one := big.NewInt(1)
	pSub1 := new(big.Int).Sub(sk.p, one)
	qSub1 := new(big.Int).Sub(sk.q, one)
	return lcm(pSub1, qSub1)
}

func gcd(a, b *big.Int) *big.Int {
	for new(big.Int).Sub(b, big.NewInt(0)).Cmp(big.NewInt(0)) == 0 {
		t := &big.Int{}
		t.Set(b)
		b.Rem(a, b)
		a.Set(t)
	}
	return a
}

func lcm(a, b *big.Int) *big.Int {
	mul := new(big.Int).Mul(a, b)
	return new(big.Int).Div(mul, gcd(a, b))
}
