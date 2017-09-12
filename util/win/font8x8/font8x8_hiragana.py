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

// Contains an 8x8 font map for unicode points U+3040 - U+309F (Hiragana)
// Constant: font8x8_3040
'''

Font8x8Hiragana = [
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3040
    0x04 + (0x3F << 8) + (0x04 << 16) + (0x3C << 24) + (0x56 << 32) + (0x4D << 40) + (0x26 << 48) + (0x00 << 56),   ## U+3041 (Hiragana a)
    0x04 + (0x3F << 8) + (0x04 << 16) + (0x3C << 24) + (0x56 << 32) + (0x4D << 40) + (0x26 << 48) + (0x00 << 56),   ## U+3042 (Hiragana A)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x11 << 24) + (0x21 << 32) + (0x25 << 40) + (0x02 << 48) + (0x00 << 56),   ## U+3043 (Hiragana i)
    0x00 + (0x01 << 8) + (0x11 << 16) + (0x21 << 24) + (0x21 << 32) + (0x25 << 40) + (0x02 << 48) + (0x00 << 56),   ## U+3044 (Hiragana I)
    0x00 + (0x1C << 8) + (0x00 << 16) + (0x1C << 24) + (0x22 << 32) + (0x20 << 40) + (0x18 << 48) + (0x00 << 56),   ## U+3045 (Hiragana u)
    0x3C + (0x00 << 8) + (0x3C << 16) + (0x42 << 24) + (0x40 << 32) + (0x20 << 40) + (0x18 << 48) + (0x00 << 56),   ## U+3046 (Hiragana U)
    0x1C + (0x00 << 8) + (0x3E << 16) + (0x10 << 24) + (0x38 << 32) + (0x24 << 40) + (0x62 << 48) + (0x00 << 56),   ## U+3047 (Hiragana e)
    0x1C + (0x00 << 8) + (0x3E << 16) + (0x10 << 24) + (0x38 << 32) + (0x24 << 40) + (0x62 << 48) + (0x00 << 56),   ## U+3048 (Hiragana E)
    0x24 + (0x4F << 8) + (0x04 << 16) + (0x3C << 24) + (0x46 << 32) + (0x45 << 40) + (0x22 << 48) + (0x00 << 56),   ## U+3049 (Hiragana o)
    0x24 + (0x4F << 8) + (0x04 << 16) + (0x3C << 24) + (0x46 << 32) + (0x45 << 40) + (0x22 << 48) + (0x00 << 56),   ## U+304A (Hiragana O)
    0x04 + (0x24 << 8) + (0x4F << 16) + (0x54 << 24) + (0x52 << 32) + (0x12 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+304B (Hiragana KA)
    0x44 + (0x24 << 8) + (0x0F << 16) + (0x54 << 24) + (0x52 << 32) + (0x52 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+304C (Hiragana GA)
    0x08 + (0x1F << 8) + (0x08 << 16) + (0x3F << 24) + (0x1C << 32) + (0x02 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+304D (Hiragana KI)
    0x44 + (0x2F << 8) + (0x04 << 16) + (0x1F << 24) + (0x0E << 32) + (0x01 << 40) + (0x1E << 48) + (0x00 << 56),   ## U+304E (Hiragana GI)
    0x10 + (0x08 << 8) + (0x04 << 16) + (0x02 << 24) + (0x04 << 32) + (0x08 << 40) + (0x10 << 48) + (0x00 << 56),   ## U+304F (Hiragana KU)
    0x28 + (0x44 << 8) + (0x12 << 16) + (0x21 << 24) + (0x02 << 32) + (0x04 << 40) + (0x08 << 48) + (0x00 << 56),   ## U+3050 (Hiragana GU)
    0x00 + (0x22 << 8) + (0x79 << 16) + (0x21 << 24) + (0x21 << 32) + (0x22 << 40) + (0x10 << 48) + (0x00 << 56),   ## U+3051 (Hiragana KE)
    0x40 + (0x22 << 8) + (0x11 << 16) + (0x3D << 24) + (0x11 << 32) + (0x12 << 40) + (0x08 << 48) + (0x00 << 56),   ## U+3052 (Hiragana GE)
    0x00 + (0x00 << 8) + (0x3C << 16) + (0x00 << 24) + (0x02 << 32) + (0x02 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+3053 (Hiragana KO)
    0x20 + (0x40 << 8) + (0x16 << 16) + (0x20 << 24) + (0x01 << 32) + (0x01 << 40) + (0x0E << 48) + (0x00 << 56),   ## U+3054 (Hiragana GO)
    0x10 + (0x7E << 8) + (0x10 << 16) + (0x3C << 24) + (0x02 << 32) + (0x02 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3055 (Hiragana SA)
    0x24 + (0x4F << 8) + (0x14 << 16) + (0x2E << 24) + (0x01 << 32) + (0x01 << 40) + (0x0E << 48) + (0x00 << 56),   ## U+3056 (Hiragana ZA)
    0x00 + (0x02 << 8) + (0x02 << 16) + (0x02 << 24) + (0x42 << 32) + (0x22 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3057 (Hiragana SI)
    0x20 + (0x42 << 8) + (0x12 << 16) + (0x22 << 24) + (0x02 << 32) + (0x22 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3058 (Hiragana ZI)
    0x10 + (0x7E << 8) + (0x18 << 16) + (0x14 << 24) + (0x18 << 32) + (0x10 << 40) + (0x0C << 48) + (0x00 << 56),   ## U+3059 (Hiragana SU)
    0x44 + (0x2F << 8) + (0x06 << 16) + (0x05 << 24) + (0x06 << 32) + (0x04 << 40) + (0x03 << 48) + (0x00 << 56),   ## U+305A (Hiragana ZU)
    0x20 + (0x72 << 8) + (0x2F << 16) + (0x22 << 24) + (0x1A << 32) + (0x02 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+305B (Hiragana SE)
    0x80 + (0x50 << 8) + (0x3A << 16) + (0x17 << 24) + (0x1A << 32) + (0x02 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+305C (Hiragana ZE)
    0x1E + (0x08 << 8) + (0x04 << 16) + (0x7F << 24) + (0x08 << 32) + (0x04 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+305D (Hiragana SO)
    0x4F + (0x24 << 8) + (0x02 << 16) + (0x7F << 24) + (0x08 << 32) + (0x04 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+305E (Hiragana ZO)
    0x02 + (0x0F << 8) + (0x02 << 16) + (0x72 << 24) + (0x02 << 32) + (0x09 << 40) + (0x71 << 48) + (0x00 << 56),   ## U+305F (Hiragana TA)
    0x42 + (0x2F << 8) + (0x02 << 16) + (0x72 << 24) + (0x02 << 32) + (0x09 << 40) + (0x71 << 48) + (0x00 << 56),   ## U+3060 (Hiragana DA)
    0x08 + (0x7E << 8) + (0x08 << 16) + (0x3C << 24) + (0x40 << 32) + (0x40 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+3061 (Hiragana TI)
    0x44 + (0x2F << 8) + (0x04 << 16) + (0x1E << 24) + (0x20 << 32) + (0x20 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3062 (Hiragana DI)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x1C << 24) + (0x22 << 32) + (0x20 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3063 (Hiragana tu)
    0x00 + (0x1C << 8) + (0x22 << 16) + (0x41 << 24) + (0x40 << 32) + (0x20 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3064 (Hiragana TU)
    0x40 + (0x20 << 8) + (0x1E << 16) + (0x21 << 24) + (0x20 << 32) + (0x20 << 40) + (0x1C << 48) + (0x00 << 56),   ## U+3065 (Hiragana DU)
    0x00 + (0x3E << 8) + (0x08 << 16) + (0x04 << 24) + (0x04 << 32) + (0x04 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+3066 (Hiragana TE)
    0x00 + (0x3E << 8) + (0x48 << 16) + (0x24 << 24) + (0x04 << 32) + (0x04 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+3067 (Hiragana DE)
    0x04 + (0x04 << 8) + (0x08 << 16) + (0x3C << 24) + (0x02 << 32) + (0x02 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+3068 (Hiragana TO)
    0x44 + (0x24 << 8) + (0x08 << 16) + (0x3C << 24) + (0x02 << 32) + (0x02 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+3069 (Hiragana DO)
    0x32 + (0x02 << 8) + (0x27 << 16) + (0x22 << 24) + (0x72 << 32) + (0x29 << 40) + (0x11 << 48) + (0x00 << 56),   ## U+306A (Hiragana NA)
    0x00 + (0x02 << 8) + (0x7A << 16) + (0x02 << 24) + (0x0A << 32) + (0x72 << 40) + (0x02 << 48) + (0x00 << 56),   ## U+306B (Hiragana NI)
    0x08 + (0x09 << 8) + (0x3E << 16) + (0x4B << 24) + (0x65 << 32) + (0x55 << 40) + (0x22 << 48) + (0x00 << 56),   ## U+306C (Hiragana NU)
    0x04 + (0x07 << 8) + (0x34 << 16) + (0x4C << 24) + (0x66 << 32) + (0x54 << 40) + (0x24 << 48) + (0x00 << 56),   ## U+306D (Hiragana NE)
    0x00 + (0x00 << 8) + (0x3C << 16) + (0x4A << 24) + (0x49 << 32) + (0x45 << 40) + (0x22 << 48) + (0x00 << 56),   ## U+306E (Hiragana NO)
    0x00 + (0x22 << 8) + (0x7A << 16) + (0x22 << 24) + (0x72 << 32) + (0x2A << 40) + (0x12 << 48) + (0x00 << 56),   ## U+306F (Hiragana HA)
    0x80 + (0x51 << 8) + (0x1D << 16) + (0x11 << 24) + (0x39 << 32) + (0x15 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+3070 (Hiragana BA)
    0x40 + (0xB1 << 8) + (0x5D << 16) + (0x11 << 24) + (0x39 << 32) + (0x15 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+3071 (Hiragana PA)
    0x00 + (0x00 << 8) + (0x13 << 16) + (0x32 << 24) + (0x51 << 32) + (0x11 << 40) + (0x0E << 48) + (0x00 << 56),   ## U+3072 (Hiragana HI)
    0x40 + (0x20 << 8) + (0x03 << 16) + (0x32 << 24) + (0x51 << 32) + (0x11 << 40) + (0x0E << 48) + (0x00 << 56),   ## U+3073 (Hiragana BI)
    0x40 + (0xA0 << 8) + (0x43 << 16) + (0x32 << 24) + (0x51 << 32) + (0x11 << 40) + (0x0E << 48) + (0x00 << 56),   ## U+3074 (Hiragana PI)
    0x1C + (0x00 << 8) + (0x08 << 16) + (0x2A << 24) + (0x49 << 32) + (0x10 << 40) + (0x0C << 48) + (0x00 << 56),   ## U+3075 (Hiragana HU)
    0x4C + (0x20 << 8) + (0x08 << 16) + (0x2A << 24) + (0x49 << 32) + (0x10 << 40) + (0x0C << 48) + (0x00 << 56),   ## U+3076 (Hiragana BU)
    0x4C + (0xA0 << 8) + (0x48 << 16) + (0x0A << 24) + (0x29 << 32) + (0x48 << 40) + (0x0C << 48) + (0x00 << 56),   ## U+3077 (Hiragana PU)
    0x00 + (0x00 << 8) + (0x04 << 16) + (0x0A << 24) + (0x11 << 32) + (0x20 << 40) + (0x40 << 48) + (0x00 << 56),   ## U+3078 (Hiragana HE)
    0x20 + (0x40 << 8) + (0x14 << 16) + (0x2A << 24) + (0x11 << 32) + (0x20 << 40) + (0x40 << 48) + (0x00 << 56),   ## U+3079 (Hiragana BE)
    0x20 + (0x50 << 8) + (0x24 << 16) + (0x0A << 24) + (0x11 << 32) + (0x20 << 40) + (0x40 << 48) + (0x00 << 56),   ## U+307A (Hiragana PE)
    0x7D + (0x11 << 8) + (0x7D << 16) + (0x11 << 24) + (0x39 << 32) + (0x55 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+307B (Hiragana HO)
    0x9D + (0x51 << 8) + (0x1D << 16) + (0x11 << 24) + (0x39 << 32) + (0x55 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+307C (Hiragana BO)
    0x5D + (0xB1 << 8) + (0x5D << 16) + (0x11 << 24) + (0x39 << 32) + (0x55 << 40) + (0x09 << 48) + (0x00 << 56),   ## U+307D (Hiragana PO)
    0x7E + (0x08 << 8) + (0x3E << 16) + (0x08 << 24) + (0x1C << 32) + (0x2A << 40) + (0x04 << 48) + (0x00 << 56),   ## U+307E (Hiragana MA)
    0x00 + (0x07 << 8) + (0x24 << 16) + (0x24 << 24) + (0x7E << 32) + (0x25 << 40) + (0x12 << 48) + (0x00 << 56),   ## U+307F (Hiragana MI)
    0x04 + (0x0F << 8) + (0x64 << 16) + (0x06 << 24) + (0x05 << 32) + (0x26 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+3080 (Hiragana MU)
    0x00 + (0x09 << 8) + (0x3D << 16) + (0x4A << 24) + (0x4B << 32) + (0x45 << 40) + (0x2A << 48) + (0x00 << 56),   ## U+3081 (Hiragana ME)
    0x02 + (0x0F << 8) + (0x02 << 16) + (0x0F << 24) + (0x62 << 32) + (0x42 << 40) + (0x3C << 48) + (0x00 << 56),   ## U+3082 (Hiragana MO)
    0x00 + (0x00 << 8) + (0x12 << 16) + (0x1F << 24) + (0x22 << 32) + (0x12 << 40) + (0x04 << 48) + (0x00 << 56),   ## U+3083 (Hiragana ya)
    0x00 + (0x12 << 8) + (0x3F << 16) + (0x42 << 24) + (0x42 << 32) + (0x34 << 40) + (0x04 << 48) + (0x00 << 56),   ## U+3084 (Hiragana YA)
    0x00 + (0x00 << 8) + (0x11 << 16) + (0x3D << 24) + (0x53 << 32) + (0x39 << 40) + (0x11 << 48) + (0x00 << 56),   ## U+3085 (Hiragana yu)
    0x00 + (0x11 << 8) + (0x3D << 16) + (0x53 << 24) + (0x51 << 32) + (0x39 << 40) + (0x11 << 48) + (0x00 << 56),   ## U+3086 (Hiragana YU)
    0x00 + (0x08 << 8) + (0x38 << 16) + (0x08 << 24) + (0x1C << 32) + (0x2A << 40) + (0x04 << 48) + (0x00 << 56),   ## U+3087 (Hiragana yo)
    0x08 + (0x08 << 8) + (0x38 << 16) + (0x08 << 24) + (0x1C << 32) + (0x2A << 40) + (0x04 << 48) + (0x00 << 56),   ## U+3088 (Hiragana YO)
    0x1E + (0x00 << 8) + (0x02 << 16) + (0x3A << 24) + (0x46 << 32) + (0x42 << 40) + (0x30 << 48) + (0x00 << 56),   ## U+3089 (Hiragana RA)
    0x00 + (0x20 << 8) + (0x22 << 16) + (0x22 << 24) + (0x2A << 32) + (0x24 << 40) + (0x10 << 48) + (0x00 << 56),   ## U+308A (Hiragana RI)
    0x1F + (0x08 << 8) + (0x3C << 16) + (0x42 << 24) + (0x49 << 32) + (0x54 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+308B (Hiragana RU)
    0x04 + (0x07 << 8) + (0x04 << 16) + (0x0C << 24) + (0x16 << 32) + (0x55 << 40) + (0x24 << 48) + (0x00 << 56),   ## U+308C (Hiragana RE)
    0x3F + (0x10 << 8) + (0x08 << 16) + (0x3C << 24) + (0x42 << 32) + (0x41 << 40) + (0x30 << 48) + (0x00 << 56),   ## U+308D (Hiragana RO)
    0x00 + (0x00 << 8) + (0x08 << 16) + (0x0E << 24) + (0x38 << 32) + (0x4C << 40) + (0x2A << 48) + (0x00 << 56),   ## U+308E (Hiragana wa)
    0x04 + (0x07 << 8) + (0x04 << 16) + (0x3C << 24) + (0x46 << 32) + (0x45 << 40) + (0x24 << 48) + (0x00 << 56),   ## U+308F (Hiragana WA)
    0x0E + (0x08 << 8) + (0x3C << 16) + (0x4A << 24) + (0x69 << 32) + (0x55 << 40) + (0x32 << 48) + (0x00 << 56),   ## U+3090 (Hiragana WI)
    0x06 + (0x3C << 8) + (0x42 << 16) + (0x39 << 24) + (0x04 << 32) + (0x36 << 40) + (0x49 << 48) + (0x00 << 56),   ## U+3091 (Hiragana WE)
    0x04 + (0x0F << 8) + (0x04 << 16) + (0x6E << 24) + (0x11 << 32) + (0x08 << 40) + (0x70 << 48) + (0x00 << 56),   ## U+3092 (Hiragana WO)
    0x08 + (0x08 << 8) + (0x04 << 16) + (0x0C << 24) + (0x56 << 32) + (0x52 << 40) + (0x21 << 48) + (0x00 << 56),   ## U+3093 (Hiragana N)
    0x40 + (0x2E << 8) + (0x00 << 16) + (0x3C << 24) + (0x42 << 32) + (0x40 << 40) + (0x38 << 48) + (0x00 << 56),   ## U+3094 (Hiragana VU)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3095
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3096
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3097
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3098
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+3099 (voiced combinator mark)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+309A (semivoiced combinator mark)
    0x40 + (0x80 << 8) + (0x20 << 16) + (0x40 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+309B (Hiragana voiced mark)
    0x40 + (0xA0 << 8) + (0x40 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+309C (Hiragana semivoiced mark)
    0x00 + (0x00 << 8) + (0x08 << 16) + (0x08 << 24) + (0x10 << 32) + (0x30 << 40) + (0x0C << 48) + (0x00 << 56),   ## U+309D (Hiragana iteration mark)
    0x20 + (0x40 << 8) + (0x14 << 16) + (0x24 << 24) + (0x08 << 32) + (0x18 << 40) + (0x06 << 48) + (0x00 << 56),   ## U+309E (Hiragana voiced iteration mark)
    0x00 + (0x00 << 8) + (0x00 << 16) + (0x00 << 24) + (0x00 << 32) + (0x00 << 40) + (0x00 << 48) + (0x00 << 56),   ## U+309F
]