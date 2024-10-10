import requests
import pandas as pd
url = "https://apicrm.theaddress.app/api/national_id_export?per_page=8000"
payload = {}
headers = {
  'EXPORT-MEDIA': 'ICHPtmQKK2oPh6HdncGadg=='
}
response = requests.request("GET", url, headers=headers, data=payload)
Dataset = pd.DataFrame()
Address1 = []
Address2 = []
for m in (response.json()['data']):
  Address1.append(m['id_address1'])
  Address2.append(m['id_address2'])


Dataset['Address1'] = Address1
Dataset['Address2'] = Address2
Dataset.to_csv('Address.csv', index=False)