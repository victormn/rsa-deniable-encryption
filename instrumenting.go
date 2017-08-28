package main

import (
	"context"
	"fmt"
	"math/big"
	"time"

	"github.com/rs/zerolog/log"
)

// Encryption ...
func Encryption(ctx context.Context, mIn *big.Int, pk *PublicKey) (cipher, r, mOut *big.Int) {
	defer func(begin time.Time) {
		log.Ctx(ctx).Debug().
			Int64("latency(ns)", time.Since(begin).Nanoseconds()).
			Str("text", fmt.Sprintf("%v", mOut)).
			Str("cipher", fmt.Sprintf("%v", cipher)).
			Str("r", fmt.Sprintf("%v", r)).
			Msg("Encryption")
	}(time.Now())

	cipher, r, mOut = encryption(mIn, pk)
	return
}

// Decryption ...
func Decryption(ctx context.Context, cipher, r *big.Int, keys *Keys) (message *big.Int) {
	defer func(begin time.Time) {
		log.Ctx(ctx).Debug().
			Int64("latency(ns)", time.Since(begin).Nanoseconds()).
			Str("text", fmt.Sprintf("%v", message)).
			//Str("cipher", fmt.Sprintf("%v", cipher)).
			Str("r", fmt.Sprintf("%v", r)).
			Msg("Decryption")
	}(time.Now())

	message = decryption(cipher, r, keys)
	return
}

// CollisionFinder ...
func CollisionFinder(ctx context.Context, m1, m2, r1 *big.Int, keys *Keys) (r2 *big.Int) {
	defer func(begin time.Time) {
		log.Ctx(ctx).Debug().
			Int64("latency(ns)", time.Since(begin).Nanoseconds()).
			Str("m1", fmt.Sprintf("%v", m1)).
			Str("m2", fmt.Sprintf("%v", m2)).
			Str("r1", fmt.Sprintf("%v", r1)).
			Str("r2", fmt.Sprintf("%v", r2)).
			Msg("CollisionFinder")
	}(time.Now())

	r2 = collisionFinder(m1, m2, r1, keys)
	return
}
