tasks={}
# 1-id
def get_id(tasks):
	if not len(tasks):
		return 1
	return max(tasks.keys())+1
# 2-string task
	def tasks_to_string(tasks):
		result=""
		for task_id,task_values in tasks.items():
			result+=f'{task_id}:{task_values['title']}|{task_values['desk']}|{task_values['priority']}|{task_value['status']}\n
			return result
			# 3-priority
	def priority_tasks():
	try:
	while True:
	priority==int(input("Choose priority task(1-low,2-middle,3-high):"))
	if priority==1:
	return "low"
	elif priority==2:
	return "middle"
	elif priority==3:
	return "high"
	else:
	print("Please,enter  a numberfrom 1-3 ")	
	except ValueError:
	print("Incorrect number")
	save_task(priority)
	# status
	def status():
	while True:
	try:
	status=int(input("Please,enter status task(1-low,2-middle,3-high):"))
	if priority==1:
	return "low"
	elif priority==2:
	return "middle"
	elif priority==3:
	return "high"
	else:
	print("Please,enter  a numberfrom 1-3 ")	
	except ValueError:
	print("Incorrect number")
# 4-write
	def write_task(tasks):
		with open("tasks.txt","w") as file:
			file.write(tasks_to_string(tasks))
			def read_task(filename):
			try:
			with open(filename,"r") as files:
			for line in file:
			parts=line.strip(split("|"))
			if len(parts)==5:
			task_id=int(parts[0])[:-1]
			tasks[tasl_id]={
				"title":parts[1],
				"desk":parts[2],
				"priority_text":parts[3],
				"status":parts[4]
			}
			except FileNotFoundError:
			print("Not found file.")
			return tasks
			# 5-sort
			def sort_task():
			view_task()
			sort_priority_status=input("Sort(priority/status):")
			# 6-view
		def view_task():
		try:
		with open("task.txt","r")	as file:
		content=file.read()
		print(content)
		except FileNotFoundError:
			print("Not found file.")
			return content
			# 7-delete
			def delete_task():
			view_task()
			try:
			delete_coice=int(input("Please,enter ID:"))
			if delete_choice in tasks:
			del task[delete_choice]
			save_task(task)
			print(f"Task c ID{delete_choice}delete")
			else print("Task with ID not find")
			except ValueError:
			print("Please,enter correct number.")
			# 8-update
			def update_task():
			view_task()
			try:
			update=int(input("Please,enter ID task:"))
			if update in tasks:
			new_title=input("Please,enter new name task:")
			new_desc=input("Please,enter new description task")
			priority=prioryti_def()
			status=status_def()
			task[update]={
				"title":new_title,
				"desc":new_desc,
				"priority":priority,
				"status":status
			}
			with open("tasks.txt","w") as file:
			content=save_task(task)
			file.write.__str__(content)
			else:
			print("Task with ID not find.")
			except ValueError:
			print("Please,enter number")
			except TabError:
			print("Updated")
		



	