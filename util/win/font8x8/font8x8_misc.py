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

// for later use
'''

Font8x8Misc = [
    0x1F + (0x33 << 8) + (0x33 << 16) + (0x5F << 24) + (0x63 << 32) + (0xF3 << 40) + (0x63 << 48) + (0xE3 << 56),   ## U+20A7 (Spanish Pesetas/Pt)
    0x70 + (0xD8 << 8) + (0x18 << 16) + (0x3C << 24) + (0x18 << 32) + (0x18 << 40) + (0x1B << 48) + (0x0E << 56),   ## U+0192 (dutch florijn)
    0x3C + (0x36 << 8) + (0x36 << 16) + (0x7C << 24) + (0x00 << 32) + (0x7E << 40) + (0x00 << 48) + (0x00 << 56),   ## U+ (underlined superscript a)
    0x1C + (0x36 << 8) + (0x36 << 16) + (0x1C << 24) + (0x00 << 32) + (0x3E << 40) + (0x00 << 48) + (0x00 << 56),   ## U+ (underlined superscript 0)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x3F << 24) + (0x03 << 32) + (0x03 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+2310 (gun pointing right)
    0x30 + (0x18 << 8) + (0x0C << 16) + (0x18 << 24) + (0x30 << 32) + (0x00 << 40) + (0x7E << 48) + (0x00 << 56),   ## U+ (less than or equal)
    0x0C + (0x18 << 8) + (0x30 << 16) + (0x18 << 24) + (0x0C << 32) + (0x00 << 40) + (0x7E << 48) + (0x00 << 56),   ## U+ (greater than or equal)
    0x0C + (0x18 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+ (grave)
    0x0E + (0x00 << 8) + (0x66 << 16) + (0x66 << 24) + (0x3C << 32) + (0x18 << 40) + (0x18 << 48) + (0x00 << 56),   ## U+ (Y grave)
    0x00 + (0x07 << 8) + (0x00 << 16) + (0x33 << 24) + (0x33 << 32) + (0x3E << 40) + (0x30 << 48) + (0x1F << 56)    ## U+ (y grave)
]
