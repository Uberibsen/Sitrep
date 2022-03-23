import urllib.request, json, requests

class API:
    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("200")
            self.formatted_print(response.json())
        else:
            print(
                f"Error: {response.status_code}")

    def get_war_report(api):
        base_url = "/worldconquest/war"
        url_get = str(f"{api}{base_url}")
        print(url_get)
        response = urllib.request.urlopen(url_get)
        if(response.getcode() == 200):
            data = response.read()
            report = json.loads(data)
        else:
            print("Error occured: ", response.getcode())
        return report

    def get_total_casualties(api):
        base_url = '/worldconquest/warReport/'
        url_get = str(f"{api}{base_url}")
        enlistments, warden_casualties, colonial_casualties = ([] for i in range(3))

        with open('constants\maps.json', 'r') as map_file:
            hexes = json.load(map_file)
            for maphex in hexes:
                hex_url = str(f"{url_get}{maphex}")
                response = urllib.request.urlopen(hex_url)
                if(response.getcode() == 200):
                    data = response.read()
                    hex_response = json.loads(data)
                else:
                    print("Error occured: ", response.getcode())
                enlistments.append(hex_response['totalEnlistments'])
                warden_casualties.append(hex_response['wardenCasualties'])
                colonial_casualties.append(hex_response['colonialCasualties'])
            days_at_war = hex_response['dayOfWar']
        return days_at_war, sum(enlistments), sum(warden_casualties), sum(colonial_casualties)