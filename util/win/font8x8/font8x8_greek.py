'''
/**
 * 8x8 monochrome bitmap fonts for rendering
 * Author: Daniel Hepper <daniel@hepper.net>
 *
 * License: Public Domain
 *
 * Based on:
 * // Summary: font8x8.h
 * // 8x8 monochrome bitmap fonts for rendering
 * //
 * // Author:
 * //     Marcel Sondaar
 * //     International Business Machines (public domain VGA fonts)
 * //
 * // License:
 * //     Public Domain
 *
 * Fetched from: http://dimensionalrift.homelinux.net/combuster/mos3/?p=viewsource&file=/modules/gfx/font8_8.asm
 **/

// Constant: font8x8_0390
// Contains an 8x8 font map for unicode points U+0390 - U+03C9 (greek characters)
'''

Font8x8Greek = [
    0x2D + (0x00 << 8) + (0x0C << 16) + (0x0C << 24) + (0x0C << 32) + (0x2C << 40) + (0x18 << 48) + (0x00 << 56), ## U+0390 (iota with tonos and diaeresis)
    0x0C + (0x1E << 8) + (0x33 << 16) + (0x33 << 24) + (0x3F << 32) + (0x33 << 40) + (0x33 << 48) + (0x00 << 56), ## U+0391 (Alpha)
    0x3F + (0x66 << 8) + (0x66 << 16) + (0x3E << 24) + (0x66 << 32) + (0x66 << 40) + (0x3F << 48) + (0x00 << 56), ## U+0392 (Beta)
    0x3F + (0x33 << 8) + (0x03 << 16) + (0x03 << 24) + (0x03 << 32) + (0x03 << 40) + (0x03 << 48) + (0x00 << 56), ## U+0393 (Gamma)
    0x08 + (0x1C << 8) + (0x1C << 16) + (0x36 << 24) + (0x36 << 32) + (0x63 << 40) + (0x7F << 48) + (0x00 << 56), ## U+0394 (Delta)
    0x7F + (0x46 << 8) + (0x16 << 16) + (0x1E << 24) + (0x16 << 32) + (0x46 << 40) + (0x7F << 48) + (0x00 << 56), ## U+0395 (Epsilon)
    0x7F + (0x63 << 8) + (0x31 << 16) + (0x18 << 24) + (0x4C << 32) + (0x66 << 40) + (0x7F << 48) + (0x00 << 56), ## U+0396 (Zeta)
    0x33 + (0x33 << 8) + (0x33 << 16) + (0x3F << 24) + (0x33 << 32) + (0x33 << 40) + (0x33 << 48) + (0x00 << 56), ## U+0397 (Eta)
    0x1C + (0x36 << 8) + (0x63 << 16) + (0x7F << 24) + (0x63 << 32) + (0x36 << 40) + (0x1C << 48) + (0x00 << 56), ## U+0398 (Theta)
    0x1E + (0x0C << 8) + (0x0C << 16) + (0x0C << 24) + (0x0C << 32) + (0x0C << 40) + (0x1E << 48) + (0x00 << 56), ## U+0399 (Iota)
    0x67 + (0x66 << 8) + (0x36 << 16) + (0x1E << 24) + (0x36 << 32) + (0x66 << 40) + (0x67 << 48) + (0x00 << 56), ## U+039A (Kappa)
    0x08 + (0x1C << 8) + (0x1C << 16) + (0x36 << 24) + (0x36 << 32) + (0x63 << 40) + (0x63 << 48) + (0x00 << 56), ## U+039B (Lambda)
    0x63 + (0x77 << 8) + (0x7F << 16) + (0x7F << 24) + (0x6B << 32) + (0x63 << 40) + (0x63 << 48) + (0x00 << 56), ## U+039C (Mu)
    0x63 + (0x67 << 8) + (0x6F << 16) + (0x7B << 24) + (0x73 << 32) + (0x63 << 40) + (0x63 << 48) + (0x00 << 56), ## U+039D (Nu)
    0x7F + (0x63 << 8) + (0x00 << 16) + (0x3E << 24) + (0x00 << 32) + (0x63 << 40) + (0x7F << 48) + (0x00 << 56), ## U+039E (Xi)
    0x1C + (0x36 << 8) + (0x63 << 16) + (0x63 << 24) + (0x63 << 32) + (0x36 << 40) + (0x1C << 48) + (0x00 << 56), ## U+039F (Omikron)
    0x7F + (0x36 << 8) + (0x36 << 16) + (0x36 << 24) + (0x36 << 32) + (0x36 << 40) + (0x36 << 48) + (0x00 << 56), ## U+03A0 (Pi)
    0x3F + (0x66 << 8) + (0x66 << 16) + (0x3E << 24) + (0x06 << 32) + (0x06 << 40) + (0x0F << 48) + (0x00 << 56), ## U+03A1 (Rho)
    0x00 + (0x01 << 8) + (0x02 << 16) + (0x04 << 24) + (0x4F << 32) + (0x90 << 40) + (0xA0 << 48) + (0x40 << 56), ## U+03A2
    0x7F + (0x63 << 8) + (0x06 << 16) + (0x0C << 24) + (0x06 << 32) + (0x63 << 40) + (0x7F << 48) + (0x00 << 56), ## U+03A3 (Sigma 2)
    0x3F + (0x2D << 8) + (0x0C << 16) + (0x0C << 24) + (0x0C << 32) + (0x0C << 40) + (0x1E << 48) + (0x00 << 56), ## U+03A4 (Tau)
    0x33 + (0x33 << 8) + (0x33 << 16) + (0x1E << 24) + (0x0C << 32) + (0x0C << 40) + (0x1E << 48) + (0x00 << 56), ## U+03A5 (Upsilon)
    0x18 + (0x7E << 8) + (0xDB << 16) + (0xDB << 24) + (0xDB << 32) + (0x7E << 40) + (0x18 << 48) + (0x00 << 56), ## U+03A6 (Phi)
    0x63 + (0x63 << 8) + (0x36 << 16) + (0x1C << 24) + (0x36 << 32) + (0x63 << 40) + (0x63 << 48) + (0x00 << 56), ## U+03A7 (Chi)
    0xDB + (0xDB << 8) + (0xDB << 16) + (0x7E << 24) + (0x18 << 32) + (0x18 << 40) + (0x3C << 48) + (0x00 << 56), ## U+03A8 (Psi)
    0x3E + (0x63 << 8) + (0x63 << 16) + (0x63 << 24) + (0x36 << 32) + (0x36 << 40) + (0x77 << 48) + (0x00 << 56), ## U+03A9 (Omega)
    0x33 + (0x00 << 8) + (0x1E << 16) + (0x0C << 24) + (0x0C << 32) + (0x0C << 40) + (0x1E << 48) + (0x00 << 56), ## U+0399 (Iota with diaeresis)
    0x33 + (0x00 << 8) + (0x33 << 16) + (0x33 << 24) + (0x1E << 32) + (0x0C << 40) + (0x1E << 48) + (0x00 << 56), ## U+03A5 (Upsilon with diaeresis)
    0x70 + (0x00 << 8) + (0x6E << 16) + (0x3B << 24) + (0x13 << 32) + (0x3B << 40) + (0x6E << 48) + (0x00 << 56), ## U+03AC (alpha aigu)
    0x38 + (0x00 << 8) + (0x1E << 16) + (0x03 << 24) + (0x0E << 32) + (0x03 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03AD (epsilon aigu)
    0x38 + (0x00 << 8) + (0x1F << 16) + (0x33 << 24) + (0x33 << 32) + (0x33 << 40) + (0x33 << 48) + (0x30 << 56), ## U+03AE (eta aigu)
    0x38 + (0x00 << 8) + (0x0C << 16) + (0x0C << 24) + (0x0C << 32) + (0x2C << 40) + (0x18 << 48) + (0x00 << 56), ## U+03AF (iota aigu)
    0x2D + (0x00 << 8) + (0x33 << 16) + (0x33 << 24) + (0x33 << 32) + (0x33 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03B0 (upsilon with tonos and diaeresis)
    0x00 + (0x00 << 8) + (0x6E << 16) + (0x3B << 24) + (0x13 << 32) + (0x3B << 40) + (0x6E << 48) + (0x00 << 56), ## U+03B1 (alpha)
    0x00 + (0x1E << 8) + (0x33 << 16) + (0x1F << 24) + (0x33 << 32) + (0x1F << 40) + (0x03 << 48) + (0x03 << 56), ## U+03B2 (beta)
    0x00 + (0x00 << 8) + (0x33 << 16) + (0x33 << 24) + (0x1E << 32) + (0x0C << 40) + (0x0C << 48) + (0x00 << 56), ## U+03B3 (gamma)
    0x38 + (0x0C << 8) + (0x18 << 16) + (0x3E << 24) + (0x33 << 32) + (0x33 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03B4 (delta)
    0x00 + (0x00 << 8) + (0x1E << 16) + (0x03 << 24) + (0x0E << 32) + (0x03 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03B5 (epsilon)
    0x00 + (0x3F << 8) + (0x06 << 16) + (0x03 << 24) + (0x03 << 32) + (0x1E << 40) + (0x30 << 48) + (0x1C << 56), ## U+03B6 (zeta)
    0x00 + (0x00 << 8) + (0x1F << 16) + (0x33 << 24) + (0x33 << 32) + (0x33 << 40) + (0x33 << 48) + (0x30 << 56), ## U+03B7 (eta)
    0x00 + (0x00 << 8) + (0x1E << 16) + (0x33 << 24) + (0x3F << 32) + (0x33 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03B8 (theta)
    0x00 + (0x00 << 8) + (0x0C << 16) + (0x0C << 24) + (0x0C << 32) + (0x2C << 40) + (0x18 << 48) + (0x00 << 56), ## U+03B9 (iota)
    0x00 + (0x00 << 8) + (0x33 << 16) + (0x1B << 24) + (0x0F << 32) + (0x1B << 40) + (0x33 << 48) + (0x00 << 56), ## U+03BA (kappa)
    0x00 + (0x03 << 8) + (0x06 << 16) + (0x0C << 24) + (0x1C << 32) + (0x36 << 40) + (0x63 << 48) + (0x00 << 56), ## U+03BB (lambda)
    0x00 + (0x00 << 8) + (0x66 << 16) + (0x66 << 24) + (0x66 << 32) + (0x3E << 40) + (0x06 << 48) + (0x03 << 56), ## U+03BC (mu)
    0x00 + (0x00 << 8) + (0x33 << 16) + (0x33 << 24) + (0x33 << 32) + (0x1E << 40) + (0x0C << 48) + (0x00 << 56), ## U+03BD (nu)
    0x1E + (0x03 << 8) + (0x0E << 16) + (0x03 << 24) + (0x03 << 32) + (0x1E << 40) + (0x30 << 48) + (0x1C << 56), ## U+03BE (xi)
    0x00 + (0x00 << 8) + (0x1E << 16) + (0x33 << 24) + (0x33 << 32) + (0x33 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03BF (omikron)
    0x00 + (0x00 << 8) + (0x7F << 16) + (0x36 << 24) + (0x36 << 32) + (0x36 << 40) + (0x36 << 48) + (0x00 << 56), ## U+03C0 (pi)
    0x00 + (0x00 << 8) + (0x3C << 16) + (0x66 << 24) + (0x66 << 32) + (0x36 << 40) + (0x06 << 48) + (0x06 << 56), ## U+03C1 (rho)
    0x00 + (0x00 << 8) + (0x3E << 16) + (0x03 << 24) + (0x03 << 32) + (0x1E << 40) + (0x30 << 48) + (0x1C << 56), ## U+03C2 (sigma 1)
    0x00 + (0x00 << 8) + (0x7E << 16) + (0x1B << 24) + (0x1B << 32) + (0x1B << 40) + (0x0E << 48) + (0x00 << 56), ## U+03C3 (sigma 2)
    0x00 + (0x00 << 8) + (0x7E << 16) + (0x18 << 24) + (0x18 << 32) + (0x58 << 40) + (0x30 << 48) + (0x00 << 56), ## U+03C4 (tau)
    0x00 + (0x00 << 8) + (0x33 << 16) + (0x33 << 24) + (0x33 << 32) + (0x33 << 40) + (0x1E << 48) + (0x00 << 56), ## U+03C5 (upsilon)
    0x00 + (0x00 << 8) + (0x76 << 16) + (0xDB << 24) + (0xDB << 32) + (0x7E << 40) + (0x18 << 48) + (0x00 << 56), ## U+03C6 (phi)
    0x00 + (0x63 << 8) + (0x36 << 16) + (0x1C << 24) + (0x1C << 32) + (0x36 << 40) + (0x63 << 48) + (0x00 << 56), ## U+03C7 (chi)
    0x00 + (0x00 << 8) + (0xDB << 16) + (0xDB << 24) + (0xDB << 32) + (0x7E << 40) + (0x18 << 48) + (0x00 << 56), ## U+03C8 (psi)
    0x00 + (0x00 << 8) + (0x36 << 16) + (0x63 << 24) + (0x6B << 32) + (0x7F << 40) + (0x36 << 48) + (0x00 << 56), ## U+03C9 (omega)
]