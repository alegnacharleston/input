name = raw_input("What is your name?>")
age = raw_input("What is your age?>")
print "Hi {}, you are {}".format(name, age)
age_twenty = int(age) + 20
print "Hi {}, you are {} now and will be {} twenty years from now.".format(name, age, age_twenty)
