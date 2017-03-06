class Directory:
	def __init__(self, max_users):
		self.user_count = 0
		self.max_users = max_users
		self.directory = list(None for x in range(0, self.max_users))

	def promptNewUser(self):
		single_user = list(None for x in range(0, 6))
		first_name = raw_input("Enter first name > ")
		last_name = raw_input("Enter last name > ")
		phone = raw_input("Enter phone number > ")
		email = raw_input("Enter email address > ")
		city = raw_input("Enter city > ")
		single_user[0] = self.user_count
		single_user[1] = first_name
		single_user[2] = last_name
		single_user[3] = phone
		single_user[4] = email
		single_user[5] = city
		
		return single_user

	def addUser(self, user):
		if self.user_count == self.max_users:
			print "Sorry directory is full..."
		else:
			print "Inserting user into index " + str(self.user_count)
			self.directory[self.user_count] = user
			self.user_count += 1

	def getUserCount(self):
		print self.user_count

	def deleteUser(self, id):
		del self.directory[id]
		return self.directory

product_team = Directory(2)

for i in range(0, product_team.max_users):
	new_member = product_team.promptNewUser()
	product_team.addUser(new_member)

print product_team.directory
print product_team.user_count
print "Deleting user at index 1..."
product_team.deleteUser(1)
print product_team.directory