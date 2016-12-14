import requests, json

TOKEN = 'EAACEdEose0cBACNhjt8EwK58zZC9bZAZAWyr70IYGKcmsRxpPSePh1AjygXAljZAF0AUxxEZCl4Mu7G6UMG0zCA0teVx5qZBelpKfwfAkj0FEdnFX3a55PZCp1zqzUqznZBsOdBiIwyzZBkmt87AG3viu0cU5nOmu8M8TulLzLycCjwZDZD'

parameters = {'access_token': TOKEN}
result = requests.get('https://graph.facebook.com/me/feed', params=parameters).json()
print(result)

for i in result['data']:
	print(i)
	#break

    


	

'''
	
	try:
	    print("Date %s" %i['created_time'])
	    print("POST : %s" %i['description'])
	    print('\n\n')

	except:
		pass

	try:
	    print('Likes:')
	    for j in i['likes']['data']:
		    print(j['name'])
	    print("\n\n")

	except:
		pass
'''