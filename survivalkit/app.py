#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🆘 SurvivalKit-CLI Main Application
主应用程序

Interactive terminal application for emergency preparedness.
交互式终端应急准备应用程序。
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.menus import Menu
from ui.colors import Colors, bold, green, yellow, cyan, red, success, warning, header
from data import first_aid, survival
from core.morse import MorseCode
from core.coordinates import CoordinateConverter
from core.checklist import ChecklistGenerator


class SurvivalKitApp:
    """Main SurvivalKit CLI application."""

    def __init__(self):
        self.menu = Menu()
        self.running = True

    def run(self):
        """Run the main application loop."""
        while self.running:
            choice = self.show_main_menu()
            if choice == -1:
                self.exit_app()
                break

            handlers = [
                self.first_aid_menu,
                self.survival_menu,
                self.tools_menu,
                self.checklist_menu,
                self.about,
            ]

            if 0 <= choice < len(handlers):
                handlers[choice]()

    def show_main_menu(self) -> int:
        """Display main menu and get selection."""
        self.menu.clear()
        self.menu.show_header()

        options = [
            ("🏥", "急救知识", "First Aid Knowledge Base"),
            ("🏕️", "野外生存", "Wilderness Survival Skills"),
            ("🧰", "实用工具", "Utility Tools (Morse, Coordinates)"),
            ("📋", "应急清单", "Emergency Checklists"),
            ("ℹ️", "关于", "About SurvivalKit-CLI"),
        ]

        print()
        for i, (emoji, label, desc) in enumerate(options, 1):
            print(f"  {cyan(str(i))}. {emoji}  {bold(label)}")
            print(f"     {dim(desc)}")
            print()

        print(cyan("─" * self.menu.width))
        print(dim("  输入编号选择  |  Q 退出"))
        print()

        try:
            choice = input("  请选择: ").strip().lower()
            if choice in ("q", "quit", "exit"):
                return -1
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return idx
            print(warning("  ⚠️  无效选项"))
            self.menu.pause()
            return self.show_main_menu()
        except (ValueError, KeyboardInterrupt, EOFError):
            return -1

    def first_aid_menu(self):
        """First aid knowledge submenu."""
        categories = first_aid.list_categories()
        keys = first_aid.get_all_keys()

        while True:
            self.menu.clear()
            self.menu.show_header()
            print(bold("  🏥 急救知识"))
            print()

            for i, (emoji, name, name_en) in enumerate(categories, 1):
                print(f"  {cyan(str(i))}. {emoji}  {bold(name)}")
                print(f"     {dim(name_en)}")
                print()

            print(f"  {cyan('0')}. 🔙  返回主菜单")
            print()
            print(cyan("─" * self.menu.width))

            try:
                choice = input("\n  请选择: ").strip()
                if choice == "0":
                    break
                idx = int(choice) - 1
                if 0 <= idx < len(keys):
                    self.show_content(first_aid.get_category(keys[idx]))
            except (ValueError, KeyboardInterrupt, EOFError):
                break

    def survival_menu(self):
        """Wilderness survival submenu."""
        categories = survival.list_categories()
        keys = survival.get_all_keys()

        while True:
            self.menu.clear()
            self.menu.show_header()
            print(bold("  🏕️ 野外生存"))
            print()

            for i, (emoji, name, name_en) in enumerate(categories, 1):
                print(f"  {cyan(str(i))}. {emoji}  {bold(name)}")
                print(f"     {dim(name_en)}")
                print()

            print(f"  {cyan('0')}. 🔙  返回主菜单")
            print()
            print(cyan("─" * self.menu.width))

            try:
                choice = input("\n  请选择: ").strip()
                if choice == "0":
                    break
                idx = int(choice) - 1
                if 0 <= idx < len(keys):
                    self.show_content(survival.get_category(keys[idx]))
            except (ValueError, KeyboardInterrupt, EOFError):
                break

    def show_content(self, category: dict):
        """Display category content."""
        if not category:
            return

        self.menu.clear()
        self.menu.show_header()
        print(bold(f"  {category.get('icon', '📖')} {category.get('name', '')}"))
        print(dim(f"  {category.get('name_en', '')}"))
        print(cyan("─" * self.menu.width))
        print()

        content = category.get("content", "")
        for line in content.split("\n"):
            if line.startswith("#"):
                print()
                print(bold(line.replace("#", "▶").strip()))
            elif line.startswith("-"):
                print(f"  {green('•')} {line[1:].strip()}")
            elif line.startswith(">"):
                print(f"  {yellow('💡')} {line[1:].strip()}")
            elif line.strip() == "":
                print()
            else:
                print(f"  {line}")

        print()
        print(cyan("─" * self.menu.width))
        self.menu.pause()

    def tools_menu(self):
        """Utility tools submenu."""
        while True:
            self.menu.clear()
            self.menu.show_header()
            print(bold("  🧰 实用工具"))
            print()

            tools = [
                ("1", "📻", "摩斯电码", "Morse Code Encoder/Decoder"),
                ("2", "🗺️", "坐标转换", "Coordinate Converter"),
                ("3", "📏", "距离计算", "Distance Calculator"),
                ("0", "🔙", "返回主菜单", "Back to Main Menu"),
            ]

            for num, emoji, name, desc in tools:
                print(f"  {cyan(num)}. {emoji}  {bold(name)}")
                print(f"     {dim(desc)}")
                print()

            print(cyan("─" * self.menu.width))

            try:
                choice = input("\n  请选择: ").strip()
                if choice == "0":
                    break
                elif choice == "1":
                    self.morse_tool()
                elif choice == "2":
                    self.coordinate_tool()
                elif choice == "3":
                    self.distance_tool()
            except (KeyboardInterrupt, EOFError):
                break

    def morse_tool(self):
        """Morse code tool."""
        self.menu.clear()
        self.menu.show_header()
        print(bold("  📻 摩斯电码工具"))
        print()

        print("  1. 文本 → 摩斯电码")
        print("  2. 摩斯电码 → 文本")
        print("  3. 查看对照表")
        print()

        try:
            choice = input("  请选择功能: ").strip()

            if choice == "1":
                text = input("\n  输入文本: ").strip()
                if text:
                    encoded = MorseCode.encode(text)
                    visual = MorseCode.to_visual(encoded)
                    timing = MorseCode.get_timing(encoded)
                    print(f"\n  编码结果: {cyan(encoded)}")
                    print(f"  视觉表示: {visual}")
                    print(f"  发送时长: ~{timing['duration_sec']}秒")

            elif choice == "2":
                morse = input("\n  输入摩斯电码 (用空格分隔): ").strip()
                if morse:
                    decoded = MorseCode.decode(morse)
                    print(f"\n  解码结果: {cyan(decoded)}")

            elif choice == "3":
                print("\n" + MorseCode.get_cheatsheet())

        except Exception as e:
            print(warning(f"\n  错误: {e}"))

        print()
        self.menu.pause()

    def coordinate_tool(self):
        """Coordinate conversion tool."""
        self.menu.clear()
        self.menu.show_header()
        print(bold("  🗺️ 坐标转换工具"))
        print()

        try:
            lat = float(input("  输入纬度 (DD): ").strip())
            lon = float(input("  输入经度 (DD): ").strip())

            formatted = CoordinateConverter.format_coordinates(lat, lon)

            print(f"\n  {bold('DD (十进制度数):')}")
            print(f"    纬度: {formatted['dd']['latitude']}")
            print(f"    经度: {formatted['dd']['longitude']}")

            print(f"\n  {bold('DMS (度分秒):')}")
            print(f"    纬度: {cyan(formatted['dms']['latitude'])}")
            print(f"    经度: {cyan(formatted['dms']['longitude'])}")

            print(f"\n  {bold('UTM (通用横轴墨卡托):')}")
            utm = formatted['utm']
            print(f"    区域: {cyan(utm['zone'])}")
            print(f"    东距: {utm['easting']} m")
            print(f"    北距: {utm['northing']} m")

        except ValueError as e:
            print(warning(f"\n  输入错误: {e}"))
        except Exception as e:
            print(warning(f"\n  错误: {e}"))

        print()
        self.menu.pause()

    def distance_tool(self):
        """Distance calculation tool."""
        self.menu.clear()
        self.menu.show_header()
        print(bold("  📏 距离计算工具"))
        print()

        try:
            print("  起点坐标:")
            lat1 = float(input("    纬度: ").strip())
            lon1 = float(input("    经度: ").strip())

            print("\n  终点坐标:")
            lat2 = float(input("    纬度: ").strip())
            lon2 = float(input("    经度: ").strip())

            result = CoordinateConverter.get_distance(lat1, lon1, lat2, lon2)

            print(f"\n  {bold('计算结果:')}")
            print(f"    直线距离: {cyan(str(result['kilometers']))} km")
            print(f"             {cyan(str(result['miles']))} miles")
            print(f"             {cyan(str(result['meters']))} m")
            print(f"    方位角:   {cyan(str(result['bearing_degrees']))}° ({result['bearing_direction']})")

        except ValueError as e:
            print(warning(f"\n  输入错误: {e}"))
        except Exception as e:
            print(warning(f"\n  错误: {e}"))

        print()
        self.menu.pause()

    def checklist_menu(self):
        """Emergency checklist submenu."""
        scenarios = ChecklistGenerator.list_scenarios()
        keys = ChecklistGenerator.get_scenario_keys()

        while True:
            self.menu.clear()
            self.menu.show_header()
            print(bold("  📋 应急清单"))
            print()

            for i, (emoji, name, name_en) in enumerate(scenarios, 1):
                print(f"  {cyan(str(i))}. {emoji}  {bold(name)}")
                print(f"     {dim(name_en)}")
                print()

            print(f"  {cyan('0')}. 🔙  返回主菜单")
            print()
            print(cyan("─" * self.menu.width))

            try:
                choice = input("\n  请选择: ").strip()
                if choice == "0":
                    break
                idx = int(choice) - 1
                if 0 <= idx < len(keys):
                    self.show_checklist(keys[idx])
            except (ValueError, KeyboardInterrupt, EOFError):
                break

    def show_checklist(self, key: str):
        """Display a checklist."""
        self.menu.clear()
        self.menu.show_header()

        content = ChecklistGenerator.generate(key)
        for line in content.split("\n"):
            if line.startswith("📋") or line.startswith("⚡") or line.startswith("🔄") or line.startswith("📦"):
                print()
                print(bold(line))
            elif line.startswith("☐"):
                print(f"  {line}")
            elif line.startswith("="):
                print(cyan(line))
            else:
                print(line)

        print()
        print(cyan("─" * self.menu.width))
        self.menu.pause()

    def about(self):
        """Show about information."""
        self.menu.clear()
        self.menu.show_header()

        about_text = """
  🆘 SurvivalKit-CLI v1.0.0

  轻量级终端应急知识库与离线生存工具箱
  Lightweight Terminal Emergency Knowledge Base
  & Offline Survival Toolkit

  ───────────────────────────────────────

  ✨ 核心特性:
    • 零依赖，纯Python标准库
    • 完全离线运行
    • 跨平台兼容
    • 丰富的应急知识库
    • 实用工具（摩斯电码、坐标转换）
    • 场景化应急清单

  📦 技术栈:
    • Python 3.8+
    • 零外部依赖

  📄 开源协议: MIT License

  🦞 由 龙虾每日项目孵化专家 打造
     Lobster Daily Incubator

  💡 灵感来源: GitHub Trending - project-nomad
     （差异化轻量版）

  ───────────────────────────────────────

  在紧急情况下，知识就是力量。
  In emergency situations, knowledge is power.
        """

        print(about_text)
        print()
        self.menu.pause()

    def exit_app(self):
        """Exit the application."""
        self.menu.clear()
        print()
        print(header("  🆘 SurvivalKit-CLI"))
        print()
        print(success("  感谢使用！请牢记："))
        print()
        print("  💡 预防胜于治疗")
        print("  💡 知识就是生存的力量")
        print("  💡 分享知识，拯救生命")
        print()
        print(dim("  在紧急情况下保持冷静，运用所学知识。"))
        print()
        print(cyan("  再见，愿您平安！🙏"))
        print()


def main():
    """Application entry point."""
    try:
        app = SurvivalKitApp()
        app.run()
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
