
#Implicit Inheritance start
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"

class child(Parent):
	pass

dad = Parent()
son = child()

dad.implicit()
son.implicit()
#Implicit INHERITANCE END
#Overriding EXPLICITLY Start
class Parent1(object):
	def override(self):
		print "PARENT Override()"

class child1(Parent1):
	def override(self):
		print "CHILD Override()"

dad1 = Parent1()
son1 = child1()
dad1.override()
son1.override()
#Overriding EXPLICITLY End

#SPECIAL CASE ALTER BEFORE OR AFTER START
class Parent2(object):
	def altered(self):
		print "Parent altered()"

class Child2(Parent2):
	def altered(self):
		print "Child, Before Parent altered()"
		super(Child2, self).altered() #At this line I used super to call the altered function of Parent class
		print "Child, After Parent altered()"

dad2 = Parent2()
son2 = Child2()
dad2.altered()
son2.altered()
#SPECIAL CASE ALTER BEFORE OR AFTER START

#ALL COMBINED START
class Parent3(object):
	def implicit(self):
		print "Parent implicit()"
	def override(self):
		print "Parent Override()"
	def altered(self):
		print "Parent altered()"

class Child3(Parent3):
	def override(self):
		print "Child Override()"
	def altered(self):
		print "Child, Before Parent altered()"
		super(Child3, self).altered()
		print "Child, after Parent altered()"

dad3 = Parent3()
son3 = Child3()

dad3.implicit() #calling the Parent implicit function
son3.implicit() #No implicit function in Child hence outputs parents implicit function

dad3.override() #Calling the Parents override function
son3.override() #Calling the childs override function since it overrides the parent function

dad3.altered()# will only print the parents print function
son3.altered()# will print both since Parents altered function is also accessed using super keyword

#ALL COMBINED END

#ANOTHER WAY OF CALLING THE FUNCTIONS FROM THE PARENT CLASS START
class Other(object):
	def override(self):
		print "Other override()"
	def implicit(self):
		print "Other implicit()"
	def altered(self):
		print "Other altered()"

class child(Other):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()
	def override(self):
		print "Child Override()"
	def altered(self):
		print "Child before Other altered"
		self.other.altered()
		print "Child after Other altered"

SON = child()

SON.implicit() # This will print implicit function of Other class
SON.override() # This will print child override function
SON.altered() # This will print Both the altered functions
#ANOTHER WAY OF CALLING THE FUNCTIONS FROM THE PARENT CLASS END
