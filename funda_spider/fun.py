import requests
import time
import threading
import pandas as pd
import get_cookies

'''
cookies = {'_vis_opt_exp_67_combi': '2', '_vis_opt_exp_81_exclude': '1', '_ga': 'GA1.2.1502718080.1561463733', '_gid': 'GA1.2.1646304843.1561463733', '_vis_opt_s': '1%7C', 'SNLB2': '12-001', '_vwo_sn': '0%3A1', '_vis_opt_test_cookie': '1', '_vwo_ds': '3%3Aa_0%2Ct_0%3A0%241561463723%3A23.3810494%3A%3A%3A%3A1', 'D_ZID': 'B7582915-2342-3B54-9343-BC1DCE799E8E', 'satisfaction-survey-chance': '0.0403899275885848', 'fonts-loaded': 'true', 'INLB': '01-004', 'sr': '0%7cfalse', 'D_SID': '213.46.252.136:48rZgOaLq07BxrV0Qr6LtG+9ZX6f1oCFngMEVSQzTPk', 'D_UID': 'D644992F-2B1E-3E41-9DE9-F217B4362A49', '.ASPXANONYMOUS': '4V5eW9xpxKl3EkqZq8zIBv4lcHtHlKJzUXRaBTg5iCG5uOS5DfKvk0gLrD0PqmD1sknqjSbDyPTzkKIcVGWAfn4hfTnoLb8FBqUB1iW71ervGlotG8otKQ6aALP4MaNLDjjJUCLn1dz5YorxzHNosKif--g1', '_vwo_uuid_v2': 'D15EFEB276818AA2126C9C28B803EC581|b916da0e2f06e5601dfa81595da1a0aa', 'html-classes': 'js supports-placeholder', 'D_HID': 'A4A9E92C-2A48-3C2C-8A88-C4964FA76B91', 'D_IID': 'D383A0CE-44F4-3CD9-A86F-F857C5DAE6B6', 'D_ZUID': '03044E65-40B9-39DC-B123-50B3846BD9DA', '_vwo_uuid': 'D15EFEB276818AA2126C9C28B803EC581', '__RequestVerificationToken': 'tDON4sgpOIM-o_KwfC0sjX3NodUMYfxV7ZcnZLGxAMNlLJ8D9WrJLi0-aQAInnJeaDput6sP7jq1PanBIRBgzBJDo9c1'}
'''


cookies = get_cookies.get_cookies()
cookie_string = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])




headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,nl;q=0.6',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': cookie_string,
#'..ASPXANONYMOUS=d0oK0LM1NdCj5Jj81GX6xZCQ2RoA8LXNtZgyqdpEUbZA6HeGTGn_8Fg6rS8qtSGhEMPhHCzkAQ9WNwsQPJOz2ZcJru6sMaSMPmq5gjexZt8jXJfP17NXvS1uQaI92DoKwyAxOlbmfhmx8roCgeP2Yly7A3o1; sr=0%7cfalse; INLB=01-002; html-classes=js supports-placeholder; _vwo_uuid_v2=D78F6C8B5734A4EB42802737D85D9997B|bb168ce01705a1c8e305a7b53c0daf84; fonts-loaded=true; D_IID=791293A9-C17B-3312-B7D2-ACEC88EBCF6F; D_UID=6D9DEFD3-9936-33CF-BAD9-B8A336E733D5; D_ZID=FA92A681-5C62-3D00-A6E0-FFCFA2DFE000; D_ZUID=4AAFAD98-FC9A-397B-BFD0-CC4CAD64ABF8; D_HID=FE2E611F-6D24-3E8E-82DC-A8B080B475A7; D_SID=85.145.109.88:KlfxLH44zOxwMWXky4Fdeo0TMw982Lv2FwcHBwJhkZY; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D78F6C8B5734A4EB42802737D85D9997B; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241560642413%3A15.2871134%3A%3A%3A%3A0; _ga=GA1.2.2014485093.1560642416; _gid=GA1.2.1849743777.1560642416; cookiePolicy_16=allowPersonalisatie=True&allowAdvertenties=True; oil_data={%22opt_in%22:true%2C%22version%22:%221.3.0-RELEASE%22%2C%22localeVariantName%22:%22enEN_00%22%2C%22localeVariantVersion%22:0%2C%22customPurposes%22:[]%2C%22consentString%22:%22BOiNyJoOiNyJoBQABBENCX-AAAAoR6_-faqaRo25-P7J9kRFAL6lgBrPSFAQKQAIQAeCJWBiKgUkyDUoCUEIAoBAAARASCJARBgQEAESgAuAAJAgAgCCAAAIBAAAAAAAAAAAAAAAAA%22%2C%22configVersion%22:0}; rtb-platform=improve; satisfaction-survey-chance=0.0438349624368525; __RequestVerificationToken=iYFvdjp0cFTjaPyPxg2Qz0kjxnX4rdaVIPbkDn1YlLtIOXJ7bPEM3A7tM9DjF95SRidYCg9uIsQDtLrRV9iX-FRA01I1; _vis_opt_exp_80_exclude=1; _vis_opt_exp_75_combi=1; __utma=72423812.2014485093.1560642416.1560685213.1560685213.1; __utmc=72423812; __utmz=72423812.1560685213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=72423812.1.10.1560685213; lzo=koop=%2fkoop%2fheel-nederland%2f&huur=%2fhuur%2fheel-nederland%2f&europe=%2feurope%2fheel-europa%2fhuur%2f&nieuwbouw=%2fnieuwbouw%2fheel-nederland%2f; _vwo_sn=40055%3A7; SNLB2=12-001; utag_main=v_id:016b5d8981a1001abec4ed9a3ddd03068001806000bd0$_sn:4$_ss:0$_st:1560687325603$vapi_domain:funda.nl$dc_visit:4$ses_id:1560682473031%3Bexp-session$_pn:7%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session',
'Host': 'www.funda.nl',
'Referer': 'https://www.funda.nl/en/koop/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

url = 'https://www.funda.nl/en/koop/heel-nederland/'
s = requests.Session()
html = s.get(url = url,headers = headers, verify=False).text


with open('funda.html','wb') as h:
    h.write(html.encode('utf-8'))


#print(html)
