import unittest
from project import Project

class TestCreateRoom(unittest.TestCase):

    def test_create_room_successfully(self):
        my_class_instance = Project()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class_instance.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)


    def test_correct_office_room_created(self):
    	my_class_instance = Project()
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	self.assertEqual(blue_office['Blue'], 'office')


    def test_correct_living_space_room_created(self):
    	my_class_instance = Project()
    	python_living_space = my_class_instance.create_room('Python', 'Living Space')
    	self.assertEqual(python_living_space['Python'], 'Living Space')

    
    def test_add_staff_succesfully(self):
    	my_class_instance = Project()
    	initial_staff_count = len(my_class_instance.all_staff)
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_staff = my_class_instance.add_person('Joe', 'Staff')
    	self.assertTrue(new_staff)
    	new_staff_count = len(my_class_instance.all_staff)
    	self.assertEqual(new_staff_count - initial_staff_count, 1)


    def test_correct_staff_added(self):
    	my_class_instance = Project()
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_staff = my_class_instance.add_person('Joe', 'Staff')
    	self.assertTrue('Joe' in my_class_instance.all_staff)


    def test_add_fellow_succesfully(self):
    	my_class_instance = Project()
    	initial_fellow_count = len(my_class_instance.all_fellows)
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_fellow = my_class_instance.add_person('Ben', 'Fellow')
    	self.assertTrue(new_fellow)
    	new_fellow_count = len(my_class_instance.all_fellows)
    	self.assertEqual(new_fellow_count - initial_fellow_count, 1)


    def test_correct_fellow_added(self):
    	my_class_instance = Project()
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_fellow = my_class_instance.add_person('Ben', 'Fellow')
    	self.assertTrue('Ben' in my_class_instance.all_fellows)


    def test_staff_allocated_an_existing_office(self):
    	my_class_instance = Project()
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_staff = my_class_instance.add_person('Joe', 'Staff')
    	staff_room = new_staff['Joe']
    	self.assertTrue(staff_room in my_class_instance.all_rooms)

    def test_fellow_allocated_an_existing_office(self):
    	my_class_instance = Project()
    	blue_office = my_class_instance.create_room('Blue', 'office')
    	red_office = my_class_instance.create_room('Red', 'office')
    	green_office = my_class_instance.create_room('Green', 'office')
    	new_fellow = my_class_instance.add_person('Ben', 'Fellow')
    	fellow_office = new_fellow['Ben']['office']
    	self.assertTrue(fellow_office in my_class_instance.all_rooms)
    	




