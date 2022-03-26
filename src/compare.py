import json, re

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