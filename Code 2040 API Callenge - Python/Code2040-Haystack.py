import requests, json

# Storing values
token = 'b3f6d2afee95203a48a0f2b42aff9ac0'
url_haystack = 'http://challenge.code2040.org/api/haystack'
url_validate = 'http://challenge.code2040.org/api/haystack/validate'
haystack = {'token':token}

response = requests.post(url_haystack, data = haystack)

# converts json to python dictionary
DICT = json.loads(response.text)

# Store needle and Haystack in variables
Needle = DICT['needle']
Parse_Haystack = DICT['haystack']

# Used for debugging
# print Needle + '\n'
# print ",".join([str(x) for x in Parse_Haystack] ) + '\n'

# Get length of List(Parse_Haystack) & find needle's index
length = len(Parse_Haystack)

for j in range(0,length):
	if Needle == Parse_Haystack[j]:
		INDEX = j
		# print "Found it! %d"  % (INDEX)

validate = {'token':token,'needle':INDEX}
response = requests.post(url_validate, data = validate)
print response.text
