from app import Directory

# =============================
# TESTS
# =============================

# TEST Instantiate a Directory with a max size of 2 and get empty initia
# list with None type in each index
product_team = Directory(2)
print "\nShould be an a list of size 2 with None objects in each index"
print product_team.directory

# TEST interactively collect user data for a single user in 'empty' list
new_member = product_team.promptNewUser()
product_team.addUser(new_member)
print "\nShould be a list of size 2 with a single user added.  All other indices should be None type"
print product_team.directory

# TEST return count of users in the directory
print "\nShould return 1"
print product_team.user_count

# TEST interactively collect user data for an additional single user
# in directory
second_member = product_team.promptNewUser()
product_team.addUser(second_member)
print "\nShould be a list of size 2 with two users added.  No more None values should appear"
print product_team.directory

# TEST return count of users in the directory with additional user accounted for
print "\nShould return 2"
print product_team.user_count

# TEST return of user object with an ID value of 0 (the first user in the directory)
print "\nShould return the first user entered"
print product_team.getUserById(0)

# TEST throw error if invalid id is given for get user by id
print "\nShould throw an error for invalid id"
print product_team.getUserById(4)

# TEST throw an error when trying to add another user beyonf the max user count
# specified during instantiation
third_member = product_team.promptNewUser()
print "\nShould throw an error when trying to add a third user"
product_team.addUser(third_member)

# TEST returning the full name of the second user entered into the directory
print "\nShould print the full name of the second user entered"
print product_team.getUserFullNameById(1)
