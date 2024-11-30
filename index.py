tasks = {}
def get_id(tasks):
	if not len(tasks):
	return 1
	return max(tasks.keys()) + 1
def priority():
            try:
            while True:
             user_prioryty= int(input(f'Enter priority 1:low,2:middle,3:hight'))
            if user_prioryty==1:
            return "low"
            elif user_prioryty==2:
           return 'middle'
           elif user_prioryty==3:
           return 'hight'
           else:"Please enter number 1-3"
           except ValueError:
  'Do not correct value'