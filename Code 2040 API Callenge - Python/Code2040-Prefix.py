import requests, json

# Storing values
token = 'b3f6d2afee95203a48a0f2b42aff9ac0'
url_prefix = 'http://challenge.code2040.org/api/prefix'
url_validate = 'http://challenge.code2040.org/api/prefix/validate'

ARRAY = {'token':token}

# Retrieves prefix and arrays
response = requests.post(url_prefix, data = ARRAY)

# Stores response as a dictionary
DICT = json.loads(response.text)

# Stores prefix and string arrays 
Prefix = DICT["prefix"]
ArrayofArrays = DICT["array"]
No_Prefix_Arrays = []

# Displays prefix and array contents, used for debugging
# print Prefix + '\n'
# print ",".join([str(x) for x in ArrayofArrays] ) + '\n'

# Get length of List & prefix
length = len(ArrayofArrays)  
prefix_length = len(Prefix)

# Using my string-fu to parse out strings begining with prefix
for j in range(0,length):
	if not ArrayofArrays[j].startswith(Prefix):
		No_Prefix_Arrays.append(ArrayofArrays[j])
		
	
# Displays final answer, used for debugging	
# print ",".join([str(x) for x in No_Prefix_Arrays] ) + '\n'

# Reformats everything back to json 
headers = {"Content-type": "application/json","Accept": "text/plain"}
answer = json.dumps({'token': token, 'array': No_Prefix_Arrays}, separators=(',', ':'))

# Sends answer to endpoint
response = requests.post(url_validate,data=answer,headers=headers)
print response.text