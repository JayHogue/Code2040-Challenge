import requests 

# Storing values
token = 'b3f6d2afee95203a48a0f2b42aff9ac0'
string = ''

# Creating dictionary
sentence = {'token':token,'string':string}

# API Endpoints
url_reverse = 'http://challenge.code2040.org/api/reverse'
url_validate = 'http://challenge.code2040.org/api/reverse/validate'

# HTTP Post Request
response = requests.post(url_reverse, data = sentence)

# Print out unmodified and modified strings
# print response.text + '\n'
# print ''.join(reversed(response.text))

# Stores reversed string 
string = ''.join(reversed(response.text))


sentence = {'token':token,'string':string}

response = requests.post(url_validate, data = sentence)
print response.text 