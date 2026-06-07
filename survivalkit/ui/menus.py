#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📋 Terminal Menu System
终端菜单系统

Interactive TUI menus using only standard library.
仅使用标准库的交互式TUI菜单。
"""

import sys
import shutil
from typing import List, Tuple, Optional, Callable
from .colors import Colors, bold, cyan, green, yellow, red, dim, header, success, warning


class Menu:
    """Interactive terminal menu."""

    def __init__(self, title: str = "", subtitle: str = ""):
        self.title = title
        self.subtitle = subtitle
        self.width = min(shutil.get_terminal_size().columns - 4, 80)

    def clear(self):
        """Clear terminal screen."""
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    def draw_box(self, content: List[str], style: str = "single") -> str:
        """Draw a box around content."""
        lines = []
        top = "┌" + "─" * (self.width - 2) + "┐"
        bottom = "└" + "─" * (self.width - 2) + "┘"
        lines.append(cyan(top))
        for line in content:
            padded = line[:self.width - 4]
            lines.append(cyan("│ ") + padded + " " * (self.width - 4 - len(padded)) + cyan(" │"))
        lines.append(cyan(bottom))
        return "\n".join(lines)

    def show_header(self):
        """Display application header."""
        print()
        banner = [
            "  🆘  SURVIVAL KIT CLI  🆘  ",
            "  轻量级终端应急知识库与离线生存工具箱  ",
        ]
        for line in banner:
            print(header(line.center(self.width)))
        if self.title:
            print()
            print(bold("  📍 " + self.title))
        if self.subtitle:
            print(dim("  " + self.subtitle))
        print()
        print(cyan("─" * self.width))
        print()

    def show_options(self, options: List[Tuple[str, str, str]], selected: int = 0) -> int:
        """
        Show interactive options menu.
        Returns selected index.
        """
        self.clear()
        self.show_header()

        for i, (emoji, label, desc) in enumerate(options):
            prefix = "▶ " if i == selected else "  "
            color = green if i == selected else dim
            print(f"{prefix}{emoji}  {color(bold(label))}")
            if desc:
                print(f"     {dim(desc)}")
            print()

        print(cyan("─" * self.width))
        print(dim("  ↑/↓ 选择  |  Enter 确认  |  Q 退出"))
        print()

        # Simple input-based selection (cross-platform, no curses needed)
        while True:
            try:
                choice = input("  请输入选项编号 (或 ↑↓ 方向键): ").strip().lower()

                if choice in ("q", "quit", "exit"):
                    return -1

                if choice in ("", "\x1b[A"):  # Up arrow or empty
                    selected = (selected - 1) % len(options)
                    return selected
                elif choice == "\x1b[B":  # Down arrow
                    selected = (selected + 1) % len(options)
                    return selected

                # Number input
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(options):
                        return idx
                except ValueError:
                    pass

                # Direct key for quick access (1-9)
                if len(choice) == 1 and choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(options):
                        return idx

                print(warning("  ⚠️  无效输入，请重试"))

            except (KeyboardInterrupt, EOFError):
                return -1

    def show_message(self, message: str, msg_type: str = "info"):
        """Display a formatted message."""
        icons = {
            "info": "ℹ️ ",
            "success": "✅ ",
            "warning": "⚠️ ",
            "error": "❌ ",
            "tip": "💡 ",
        }
        colors = {
            "info": cyan,
            "success": success,
            "warning": warning,
            "error": error,
            "tip": yellow,
        }
        icon = icons.get(msg_type, "ℹ️ ")
        color = colors.get(msg_type, cyan)
        print(f"\n  {icon} {color(message)}\n")

    def pause(self, message: str = "按 Enter 继续..."):
        """Pause and wait for user input."""
        try:
            input(f"\n  {dim(message)}")
        except (KeyboardInterrupt, EOFError):
            pass

    def confirm(self, message: str) -> bool:
        """Ask for confirmation."""
        try:
            response = input(f"\n  {yellow(message)} [y/N]: ").strip().lower()
            return response in ("y", "yes", "是", "确认")
        except (KeyboardInterrupt, EOFError):
            return False

    def input_text(self, prompt: str, default: str = "") -> str:
        """Get text input from user."""
        try:
            full_prompt = f"\n  {cyan(prompt)}"
            if default:
                full_prompt += f" [{default}]"
            full_prompt += ": "
            response = input(full_prompt).strip()
            return response if response else default
        except (KeyboardInterrupt, EOFError):
            return default

    def show_content(self, title: str, content: str):
        """Display formatted content with title."""
        self.clear()
        self.show_header()
        print(bold(f"  📖 {title}"))
        print(cyan("─" * self.width))
        print()
        for line in content.split("\n"):
            if line.startswith("#"):
                print(bold(line.replace("#", "▶")))
            elif line.startswith("-"):
                print(f"  {green('•')} {line[1:].strip()}")
            elif line.startswith(">"):
                print(f"  {yellow('💡')} {line[1:].strip()}")
            elif line.strip() == "":
                print()
            else:
                print(f"  {line}")
        print()
        print(cyan("─" * self.width))
