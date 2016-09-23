import requests, json
from datetime import timedelta
import dateutil.parser

# Storing values
token = 'b3f6d2afee95203a48a0f2b42aff9ac0'
url_dating = 'http://challenge.code2040.org/api/dating'
url_validate = 'http://challenge.code2040.org/api/dating/validate'
post_token = {'token':token}

# Retrieves datestamp and interval
response = requests.post(url_dating, data = post_token)

# Stores response as a dictionary
DICT = json.loads(response.text)

# Stores datestamp and interval strings
datestamp = DICT["datestamp"]
interval = DICT["interval"]

# Adding datestamp and interval
seconds_interval = timedelta(seconds=interval)
date = dateutil.parser.parse(datestamp)
Date_Sum = date + seconds_interval

# remove timezone
Date_Sum = Date_Sum.replace(tzinfo=None)

# Reformat back to ISO 8601 format
Date_Sum = Date_Sum.isoformat() + 'Z'

# Sends answer to endpoint
answer = {'token': token, 'datestamp': Date_Sum}
response = requests.post(url_validate, data = answer)
print response.text 