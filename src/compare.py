import json, re
from collections import Counter

class Hexagon:
    def search_hex_name(message):      
        true_hex = ''
        with open('constants\maps.json', 'r') as hex_file:
            hexes = json.load(hex_file)
            for maphex in hexes:
                if message.lower() in maphex.lower():
                    true_hex = maphex
                    break
                else:
                    continue
            if not true_hex:
                return False
        return true_hex

    def split_hex_name(hex_name):
        hex_split = (re.findall('[A-Z][^A-Z]*', hex_name))
        if "Hex" in hex_split:
            hex_split.pop()
        full_hex_name = ' '.join(hex_split)
        return full_hex_name

    def decipher_icon_type(response):
        warden_icons, colonial_icons = ([] for i in range(2))

        with open('constants\map_icons.json', 'r') as map_icons:
            all_icons = json.load(map_icons)
            for icon in response["wardens"]:
                for k,v in all_icons.items():
                    if v is icon:
                        warden_icons.append(k)
            for icon in response["colonials"]:
                for k,v in all_icons.items():
                    if v is icon:
                        colonial_icons.append(k)
        counted_w = Counter(warden_icons)
        counted_c = Counter(colonial_icons)
        return counted_w, counted_c