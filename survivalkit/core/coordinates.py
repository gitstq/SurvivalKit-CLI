#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🗺️ Coordinate Conversion Engine
坐标转换引擎

Convert between DD, DMS, and UTM coordinate formats.
支持DD、DMS、UTM坐标格式互转。
"""

import math
from typing import Tuple, Optional


class CoordinateConverter:
    """Coordinate format converter."""

    @staticmethod
    def dd_to_dms(dd: float, is_latitude: bool = True) -> str:
        """
        Convert Decimal Degrees to DMS format.
        将十进制度数转换为度分秒格式。

        Args:
            dd: Decimal degrees
            is_latitude: True for latitude, False for longitude

        Returns:
            DMS string like "40°26′46″N"
        """
        direction = ''
        if is_latitude:
            direction = 'N' if dd >= 0 else 'S'
        else:
            direction = 'E' if dd >= 0 else 'W'

        dd = abs(dd)
        degrees = int(dd)
        minutes_float = (dd - degrees) * 60
        minutes = int(minutes_float)
        seconds = round((minutes_float - minutes) * 60, 2)

        return f"{degrees}°{minutes}′{seconds}″{direction}"

    @staticmethod
    def dms_to_dd(dms: str) -> float:
        """
        Convert DMS string to Decimal Degrees.
        将度分秒字符串转换为十进制度数。

        Args:
            dms: String like "40°26′46″N" or "40:26:46N"

        Returns:
            Decimal degrees
        """
        import re
        # Normalize separators
        normalized = dms.replace('°', ':').replace('′', ':').replace('″', ':').replace("'", ':').replace('"', ':')
        normalized = normalized.replace(' ', '')

        # Extract parts
        pattern = r'([\d.]+):([\d.]+):([\d.]+)([NSEW])'
        match = re.match(pattern, normalized, re.IGNORECASE)

        if not match:
            raise ValueError(f"Invalid DMS format: {dms}")

        degrees = float(match.group(1))
        minutes = float(match.group(2))
        seconds = float(match.group(3))
        direction = match.group(4).upper()

        dd = degrees + minutes / 60 + seconds / 3600

        if direction in ('S', 'W'):
            dd = -dd

        return round(dd, 6)

    @staticmethod
    def dd_to_utm(lat: float, lon: float) -> dict:
        """
        Convert latitude/longitude to UTM coordinates.
        将经纬度转换为UTM坐标。

        Returns dict with zone, easting, northing.
        """
        # UTM zone
        zone_number = int((lon + 180) / 6) + 1

        # UTM zone letter
        zone_letters = "CDEFGHJKLMNPQRSTUVWXX"
        if -80 <= lat <= 84:
            zone_letter = zone_letters[int((lat + 80) / 8)]
        else:
            zone_letter = '?'

        # Simplified UTM conversion (WGS84)
        # This is an approximation for practical use
        a = 6378137.0  # WGS84 semi-major axis
        f = 1 / 298.257223563  # flattening
        e2 = 2 * f - f ** 2  # eccentricity squared

        # Central meridian
        lon0 = (zone_number - 1) * 6 - 180 + 3
        lon0_rad = math.radians(lon0)

        lat_rad = math.radians(lat)
        lon_rad = math.radians(lon)

        N = a / math.sqrt(1 - e2 * math.sin(lat_rad) ** 2)
        T = math.tan(lat_rad) ** 2
        C = e2 * math.cos(lat_rad) ** 2 / (1 - e2)
        A = math.cos(lat_rad) * (lon_rad - lon0_rad)

        M = a * ((1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256) * lat_rad
                 - (3 * e2 / 8 + 3 * e2 ** 2 / 32 + 45 * e2 ** 3 / 1024) * math.sin(2 * lat_rad)
                 + (15 * e2 ** 2 / 256 + 45 * e2 ** 3 / 1024) * math.sin(4 * lat_rad)
                 - (35 * e2 ** 3 / 3072) * math.sin(6 * lat_rad))

        # UTM scale factor at central meridian
        k0 = 0.9996

        easting = k0 * N * (A + (1 - T + C) * A ** 3 / 6
                            + (5 - 18 * T + T ** 2 + 72 * C - 58 * 0.006739497) * A ** 5 / 120)
        easting = easting + 500000

        northing = k0 * (M + N * math.tan(lat_rad) * (A ** 2 / 2
                                                       + (5 - T + 9 * C + 4 * C ** 2) * A ** 4 / 24
                                                       + (61 - 58 * T + T ** 2 + 600 * C - 330 * 0.006739497) * A ** 6 / 720))

        if lat < 0:
            northing = northing + 10000000

        return {
            "zone": f"{zone_number}{zone_letter}",
            "easting": round(easting, 2),
            "northing": round(northing, 2),
            "hemisphere": "N" if lat >= 0 else "S"
        }

    @staticmethod
    def get_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> dict:
        """
        Calculate distance between two coordinates using Haversine formula.
        使用Haversine公式计算两点间距离。
        """
        R = 6371000  # Earth radius in meters

        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)

        a = (math.sin(delta_lat / 2) ** 2
             + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance_m = R * c
        distance_km = distance_m / 1000

        # Calculate bearing
        y = math.sin(delta_lon) * math.cos(lat2_rad)
        x = (math.cos(lat1_rad) * math.sin(lat2_rad)
             - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(delta_lon))
        bearing_rad = math.atan2(y, x)
        bearing = (math.degrees(bearing_rad) + 360) % 360

        # Cardinal direction
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        direction = directions[round(bearing / 45) % 8]

        return {
            "meters": round(distance_m, 2),
            "kilometers": round(distance_km, 3),
            "miles": round(distance_km * 0.621371, 3),
            "bearing_degrees": round(bearing, 2),
            "bearing_direction": direction
        }

    @staticmethod
    def format_coordinates(lat: float, lon: float) -> dict:
        """Format coordinates in all supported formats."""
        return {
            "dd": {
                "latitude": lat,
                "longitude": lon
            },
            "dms": {
                "latitude": CoordinateConverter.dd_to_dms(lat, True),
                "longitude": CoordinateConverter.dd_to_dms(lon, False)
            },
            "utm": CoordinateConverter.dd_to_utm(lat, lon)
        }


def demo():
    """Demonstrate coordinate conversion."""
    print("=" * 50)
    print("坐标转换演示")
    print("=" * 50)

    # Beijing coordinates
    lat, lon = 39.9042, 116.4074

    print(f"\n输入坐标 (DD): {lat}, {lon}")
    print(f"  北京天安门")

    formatted = CoordinateConverter.format_coordinates(lat, lon)

    print(f"\nDMS格式:")
    print(f"  纬度: {formatted['dms']['latitude']}")
    print(f"  经度: {formatted['dms']['longitude']}")

    print(f"\nUTM格式:")
    utm = formatted['utm']
    print(f"  区域: {utm['zone']}")
    print(f"  东距: {utm['easting']} m")
    print(f"  北距: {utm['northing']} m")

    # Distance calculation
    lat2, lon2 = 31.2304, 121.4737  # Shanghai
    dist = CoordinateConverter.get_distance(lat, lon, lat2, lon2)
    print(f"\n距离计算 (北京 → 上海):")
    print(f"  距离: {dist['kilometers']} km")
    print(f"  方位: {dist['bearing_degrees']}° ({dist['bearing_direction']})")

    # DMS conversion test
    dms_str = "39:54:15.12N"
    dd = CoordinateConverter.dms_to_dd(dms_str)
    print(f"\nDMS转DD测试:")
    print(f"  输入: {dms_str}")
    print(f"  输出: {dd}")


if __name__ == "__main__":
    demo()
