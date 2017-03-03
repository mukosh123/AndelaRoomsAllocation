class Project:
	def __init__(self):
		self.all_rooms = {}
		self.all_staff = {}
		self.all_fellows = {}


	def create_room(self, room_name, room_type):
		self.all_rooms[room_name] = room_type
		return self.all_rooms

	def add_person(self, name, category, option = False):
		import random
		office_rooms = []
		livin_space_rooms = []
		for room in self.all_rooms:
			if self.all_rooms[room] == 'office':
				office_rooms.append(room)
			elif self.all_rooms[room] == 'Living_space':
				living_space_rooms.append(room)
		if category == 'Staff':
			self.all_staff[name] = random.choice(office_rooms)
			return self.all_staff
		elif category == 'Fellow' and option == False:
			self.all_fellows[name] = {'office' : random.choice(office_rooms)}
			return self.all_fellows
		elif category == 'Fellow' and option == True:
			self.all_fellows[name] = {'office' : random.choice(office_rooms)}
			self.all_fellows[name] = {'living_space' : random.choice(living_space_rooms)}
			return self.all_fellows




	