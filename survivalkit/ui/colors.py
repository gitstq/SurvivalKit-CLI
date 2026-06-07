#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 Terminal Color & Style Definitions
终端颜色与样式定义

Zero-dependency color support with auto-detection.
零依赖颜色支持，自动检测终端能力。
"""

import os
import sys


class Colors:
    """ANSI color codes with automatic fallback support."""

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    # Reset
    RESET = "\033[0m"

    @classmethod
    def enabled(cls) -> bool:
        """Check if terminal supports colors."""
        if os.environ.get("NO_COLOR"):
            return False
        if os.environ.get("FORCE_COLOR"):
            return True
        return sys.stdout.isatty()

    @classmethod
    def wrap(cls, text: str, *codes: str) -> str:
        """Wrap text with color codes if supported."""
        if not cls.enabled():
            return text
        return "".join(codes) + text + cls.RESET


# Convenience functions
def red(text: str) -> str:
    return Colors.wrap(text, Colors.RED)


def green(text: str) -> str:
    return Colors.wrap(text, Colors.GREEN)


def yellow(text: str) -> str:
    return Colors.wrap(text, Colors.YELLOW)


def blue(text: str) -> str:
    return Colors.wrap(text, Colors.BLUE)


def cyan(text: str) -> str:
    return Colors.wrap(text, Colors.CYAN)


def magenta(text: str) -> str:
    return Colors.wrap(text, Colors.MAGENTA)


def bold(text: str) -> str:
    return Colors.wrap(text, Colors.BOLD)


def dim(text: str) -> str:
    return Colors.wrap(text, Colors.DIM)


def header(text: str) -> str:
    return Colors.wrap(text, Colors.BOLD, Colors.CYAN)


def success(text: str) -> str:
    return Colors.wrap(text, Colors.BOLD, Colors.GREEN)


def warning(text: str) -> str:
    return Colors.wrap(text, Colors.BOLD, Colors.YELLOW)


def error(text: str) -> str:
    return Colors.wrap(text, Colors.BOLD, Colors.RED)


def info(text: str) -> str:
    return Colors.wrap(text, Colors.BLUE)


def emoji_status(emoji: str, text: str) -> str:
    """Create an emoji-prefixed status line."""
    return f"{emoji}  {text}"
