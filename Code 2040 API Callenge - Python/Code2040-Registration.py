import requests # included packages


# Dictionary - JSON format ???
registration = {'token': 'b3f6d2afee95203a48a0f2b42aff9ac0', 'github': 'https://github.com/JayHogue/Code2040-Challenge/blob/master/README.md'}

# API Enpoint
url = 'http://challenge.code2040.org/api/register'
data = registration

# Posts data to API Endpoint ??? Figure out what this is is doing
# Figure out what the the HTTP methods do
response = requests.post(url, data)

print response.text