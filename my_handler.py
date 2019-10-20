import requests

def handler(event, context):
	r = requests.get('https://www.lequipe.fr')
	print(r.text[0:500])
	if r.status_code == 200:
		return 'Sucess!'
	else:
		return 'Failure'