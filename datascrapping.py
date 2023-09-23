from googlefinance import getQuotes
import json
print json.dumps(getQuotes('MRVL'), indent=2)