import json

class Comparison:
    def hex_names(message):      
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