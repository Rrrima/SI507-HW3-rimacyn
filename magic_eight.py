def askq():
	while(1):
		question = input('What is your question?\n')
		if question[-1] == '?':
			break;
		else:
			print('Sorry, I can only answer questions.')
	return answer

askq()
