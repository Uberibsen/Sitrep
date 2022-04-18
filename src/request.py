import urllib.request, json, requests
from urllib.error import HTTPError, URLError

class API:
    def call(api, url_modifier):
        url_request = str(f"{api}{url_modifier}")
        try:
            response = urllib.request.urlopen(url_request)
            if (response.getcode() == 200):
                data = response.read()
                hex_response = json.loads(data)
                return hex_response
        except (HTTPError, URLError) as err:
            return False

    def get_war_report(api):
        base_url = "/worldconquest/war"
        url_get = str(f"{api}{base_url}")
        response = API.call(api, base_url)
        if response:
            return response
        else:
            return False

    def get_total_casualties(api):
        base_url = '/worldconquest/warReport/'
        url_get = str(f"{api}{base_url}")
        enlistments, warden_casualties, colonial_casualties = ([] for i in range(3))

        with open('constants\maps.json', 'r') as map_file:
            hexes = json.load(map_file)
            for maphex in hexes:
                hex_url = str(f"{url_get}{maphex}")
                hex_response = API.call(api, base_url)
                if response:
                    continue
                else:
                    return False
                enlistments.append(hex_response['totalEnlistments'])
                warden_casualties.append(hex_response['wardenCasualties'])
                colonial_casualties.append(hex_response['colonialCasualties'])
            days_at_war = hex_response['dayOfWar']
        return days_at_war, sum(enlistments), sum(warden_casualties), sum(colonial_casualties)
        
    def get_hex_info(api, hex_name):
        base_url = '/worldconquest/warReport/'
        url_modifier = str(f"{base_url}{hex_name}")
        hex_response = API.call(api, url_modifier)

        if hex_response is False:
            return False

        enlistments = hex_response['totalEnlistments']
        warden_casualties = hex_response['wardenCasualties']
        colonial_casualties = hex_response['colonialCasualties']
        return enlistments, warden_casualties, colonial_casualties

    def get_captured_structures(api, hex_name):
        base_url = '/worldconquest/maps/'
        url_modifier = str(f"{base_url}{hex_name}/dynamic/public")
        hex_response = API.call(api, url_modifier)

        if hex_response is False:
            return False

        captured_structures = {"neutral":[], "wardens":[], "colonials": []}       
        for structure in hex_response["mapItems"]:
            team = structure['teamId']
            icon = structure['iconType']
            if team == "WARDENS":
                captured_structures["wardens"].append(icon)
            if team == "COLONIALS":
                captured_structures["colonials"].append(icon)
            if team == "NONE":
                captured_structures["neutral"].append(icon)
        return captured_structures       