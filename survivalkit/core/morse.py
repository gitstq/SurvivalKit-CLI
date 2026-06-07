#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📻 Morse Code Engine
摩斯电码引擎

Encode/decode Morse code with audio simulation support.
支持编码/解码和音频模拟的摩斯电码引擎。
"""

# International Morse Code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse dictionary
REVERSE_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}


class MorseCode:
    """Morse code encoder/decoder."""

    @staticmethod
    def encode(text: str) -> str:
        """Encode text to Morse code."""
        result = []
        for char in text.upper():
            if char in MORSE_CODE_DICT:
                result.append(MORSE_CODE_DICT[char])
            else:
                result.append('?')
        return ' '.join(result)

    @staticmethod
    def decode(morse: str) -> str:
        """Decode Morse code to text."""
        result = []
        for code in morse.strip().split():
            if code in REVERSE_MORSE:
                result.append(REVERSE_MORSE[code])
            elif code == '/':
                result.append(' ')
            else:
                result.append('?')
        return ''.join(result)

    @staticmethod
    def to_visual(morse: str) -> str:
        """Convert Morse code to visual representation (■/□)."""
        visual = []
        for char in morse:
            if char == '.':
                visual.append('■')
            elif char == '-':
                visual.append('■■■')
            elif char == ' ':
                visual.append('  ')
            elif char == '/':
                visual.append('    ')
        return ''.join(visual)

    @staticmethod
    def get_timing(morse: str) -> dict:
        """Get timing information for Morse code."""
        units = 0
        for char in morse:
            if char == '.':
                units += 2  # dot + space
            elif char == '-':
                units += 4  # dash + space
            elif char == ' ':
                units += 2  # letter space
            elif char == '/':
                units += 4  # word space
        # Approximate duration at 20 WPM (1 unit = 60ms)
        duration_ms = units * 60
        return {
            "units": units,
            "duration_ms": duration_ms,
            "duration_sec": round(duration_ms / 1000, 2)
        }

    @staticmethod
    def get_cheatsheet() -> str:
        """Get Morse code reference sheet."""
        lines = ["📻 摩斯电码对照表", "=" * 40, ""]
        letters = [f"{k}: {v}" for k, v in list(MORSE_CODE_DICT.items())[:26]]
        numbers = [f"{k}: {v}" for k, v in list(MORSE_CODE_DICT.items())[26:36]]

        lines.append("字母 (Letters):")
        for i in range(0, len(letters), 4):
            lines.append("  " + "  |  ".join(letters[i:i+4]))

        lines.append("")
        lines.append("数字 (Numbers):")
        for i in range(0, len(numbers), 5):
            lines.append("  " + "  |  ".join(numbers[i:i+5]))

        lines.append("")
        lines.append("常用标点 (Common Punctuation):")
        punct = [f"{k}: {v}" for k, v in list(MORSE_CODE_DICT.items())[36:]]
        lines.append("  " + "  |  ".join(punct[:4]))
        lines.append("  " + "  |  ".join(punct[4:8]))

        return "\n".join(lines)


def demo():
    """Demonstrate Morse code functionality."""
    print("=" * 50)
    print("摩斯电码演示")
    print("=" * 50)

    test_text = "SOS HELP"
    encoded = MorseCode.encode(test_text)
    decoded = MorseCode.decode(encoded)

    print(f"原文: {test_text}")
    print(f"编码: {encoded}")
    print(f"视觉: {MorseCode.to_visual(encoded)}")
    print(f"解码: {decoded}")

    timing = MorseCode.get_timing(encoded)
    print(f"时长: {timing['duration_sec']}秒")

    print("\n" + MorseCode.get_cheatsheet())


if __name__ == "__main__":
    demo()
