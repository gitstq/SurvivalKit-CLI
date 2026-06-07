#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📋 Emergency Checklist Generator
应急清单生成器

Generate scenario-based emergency checklists.
按场景生成应急清单。
"""

from typing import List, Dict


class ChecklistGenerator:
    """Generate emergency preparedness checklists."""

    SCENARIOS = {
        "earthquake": {
            "name": "地震应急",
            "name_en": "Earthquake Emergency",
            "icon": "🏚️",
            "before": [
                "固定高大家具（书架、衣柜）",
                "准备应急包（72小时物资）",
                "确认安全避难位置",
                "了解建筑安全出口",
                "备份重要文件（云端/异地）",
                "准备家庭应急联络卡",
            ],
            "during": [
                "保持冷静，不要惊慌",
                "室内：躲在坚固家具旁，保护头部",
                "远离窗户、玻璃、外墙",
                "电梯中：按下所有楼层，出梯躲避",
                "室外：远离建筑、电线、广告牌",
                "驾车：停车远离高架桥，留在车内",
            ],
            "after": [
                "检查伤情，进行急救",
                "关闭煤气、电源总闸",
                "收听广播获取信息",
                "不要使用明火（防煤气泄漏）",
                "准备余震应对",
                "按约定与家人汇合",
            ],
        },
        "flood": {
            "name": "洪水应急",
            "name_en": "Flood Emergency",
            "icon": "🌊",
            "before": [
                "关注气象预警",
                "准备应急包和救生衣",
                "将贵重物品移至高处",
                "准备沙袋堵门",
                "规划撤离路线",
                "给手机充满电",
            ],
            "during": [
                "立即向高处转移",
                "不要涉水行走（暗流、井盖）",
                "远离电线杆、变压器",
                "被困时拨打求救电话",
                "使用哨子、手电筒发信号",
                "不要乘坐电梯",
            ],
            "after": [
                "等待官方通知再返家",
                "检查房屋结构安全",
                "消毒被淹物品",
                "不要饮用未经处理的水",
                "拍照记录损失",
                "注意防疫（蚊蝇滋生）",
            ],
        },
        "wilderness": {
            "name": "野外探险",
            "name_en": "Wilderness Adventure",
            "icon": "🏕️",
            "before": [
                "告知他人行程计划",
                "检查装备（帐篷、睡袋、炉具）",
                "准备急救包",
                "携带导航工具（地图/GPS/指南针）",
                "准备足够食物和水",
                "检查天气预报",
            ],
            "during": [
                "保持方向感，标记路径",
                "定时休息补充水分",
                "注意野生动物",
                "生火后彻底熄灭",
                "食物悬挂防熊",
                "迷路时STOP原则",
            ],
            "after": [
                "报平安",
                "检查装备损耗",
                "总结经验",
                "处理垃圾（Leave No Trace）",
            ],
        },
        "power_outage": {
            "name": "停电应急",
            "name_en": "Power Outage",
            "icon": "🔌",
            "before": [
                "储备手电筒、蜡烛",
                "准备充电宝、电池",
                "储备即食食品",
                "了解停电应急开关",
                "备用保暖用品",
            ],
            "during": [
                "拔掉敏感电器插头",
                "关闭冰箱门保持低温",
                "使用蜡烛注意防火",
                "收听应急广播",
                "减少手机使用保存电量",
                "检查邻居是否需要帮助",
            ],
            "after": [
                "逐步恢复电器使用",
                "检查食物是否变质",
                "补充应急物资",
            ],
        },
        "first_aid_kit": {
            "name": "急救包清单",
            "name_en": "First Aid Kit",
            "icon": "🧰",
            "items": [
                "☐ 创可贴（各种尺寸）",
                "☐ 无菌纱布/绷带",
                "☐ 医用胶带",
                "☐ 消毒剂（碘伏/酒精）",
                "☐ 抗生素软膏",
                "☐ 止痛药（布洛芬/对乙酰氨基酚）",
                "☐ 抗过敏药",
                "☐ 止泻药",
                "☐ 体温计",
                "☐ 镊子",
                "☐ 安全别针",
                "☐ 医用手套",
                "☐ 急救手册",
                "☐ 个人药品",
                "☐ 手电筒",
                "☐ 哨子",
            ],
        },
        "bug_out_bag": {
            "name": "应急逃生包 (72小时)",
            "name_en": "Bug Out Bag (72 Hours)",
            "icon": "🎒",
            "items": [
                "☐ 水（3升/人）或净水片",
                "☐ 即食食品（3天量）",
                "☐ 手电筒 + 备用电池",
                "☐ 收音机（手摇/电池）",
                "☐ 急救包",
                "☐ 多功能刀具",
                "☐ 打火石/火柴",
                "☐ 应急毯/睡袋",
                "☐ 换洗衣物",
                "☐ 雨衣/ poncho",
                "☐ 现金（小额）",
                "☐ 身份证件复印件",
                "☐ 手机充电器/充电宝",
                "☐ 哨子",
                "☐ 绳索（伞绳）",
                "☐ 地图",
                "☐ 笔记本和笔",
                "☐ 口罩",
                "☐ 卫生用品",
                "☐ 重要联系人清单",
            ],
        },
    }

    @classmethod
    def list_scenarios(cls):
        """List all available scenarios."""
        return [
            (data["icon"], data["name"], data["name_en"])
            for key, data in cls.SCENARIOS.items()
        ]

    @classmethod
    def generate(cls, scenario_key: str) -> str:
        """Generate checklist for a scenario."""
        scenario = cls.SCENARIOS.get(scenario_key)
        if not scenario:
            return f"未知场景: {scenario_key}"

        lines = [
            f"{scenario['icon']} {scenario['name']}清单",
            f"   {scenario['name_en']} Checklist",
            "=" * 50,
            "",
        ]

        if "before" in scenario:
            lines.append("📋 事前准备 (Before):")
            for item in scenario["before"]:
                lines.append(f"  ☐ {item}")
            lines.append("")

        if "during" in scenario:
            lines.append("⚡ 应急行动 (During):")
            for item in scenario["during"]:
                lines.append(f"  ☐ {item}")
            lines.append("")

        if "after" in scenario:
            lines.append("🔄 事后恢复 (After):")
            for item in scenario["after"]:
                lines.append(f"  ☐ {item}")
            lines.append("")

        if "items" in scenario:
            lines.append("📦 物品清单 (Items):")
            for item in scenario["items"]:
                lines.append(f"  {item}")
            lines.append("")

        return "\n".join(lines)

    @classmethod
    def get_scenario_keys(cls):
        """Get all scenario keys."""
        return list(cls.SCENARIOS.keys())


def demo():
    """Demonstrate checklist generation."""
    print("=" * 50)
    print("应急清单生成器演示")
    print("=" * 50)

    for key in ["first_aid_kit", "bug_out_bag", "earthquake"]:
        print("\n" + ChecklistGenerator.generate(key))
        print("\n" + "-" * 50)


if __name__ == "__main__":
    demo()
