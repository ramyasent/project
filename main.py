#hello
import os
import requests
lc_base_url = 'https://linkcheckerapi.elitesiteoptimizer.com/'
LC_SECURITY_KEY = "GhfmGu8IY5ndzG8GjC3euKrOv"
org_slug='reapp'
domain_slug='elitemcommerce'
request_url = os.path.join(lc_base_url, "summary_data", org_slug, domain_slug)

if start_date and end_date:
    request_params = {"key": LC_SECURITY_KEY,
                      "start_date": start_date,
                      "end_date": end_date,
                      "is_dashboard": True,
                      "status_code": True,
                      "section_name": section_name,
                      }
else:
    request_params = {"key": settings.LC_SECURITY_KEY,
                      "section_name": section_name,
                      "status_code": True
                      }
try:
    res = requests.get(request_url, params=request_params)
    status_code = res.status_code
except:
    status_code = None

if status_code == 200:
    res_json = res.json()
    print('res_json', res_json)