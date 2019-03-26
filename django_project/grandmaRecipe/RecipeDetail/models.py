from django.db import models

# Create your models here.

#This defines a table which contains all fields of a recipe(name, ingredients, cooking steps, memory behind, and 4 categories)
# The four categories will each link to a table. 
class Recipe(models.Model):
	name = models.charField(max_length=128, null=False)
	ingredient = models.charField(max_length=255, null=True, blank=True)
	steps = models.charField(max_length=255, null=True, blank=True)
	memory = models.charField(max_length=255, null=False, blank=False)
	ingCate = models.ForeignKey(Mainingredient, on_delete=models.CASCADE)
	scenCate = models.ForeignKey(Scenario, on_delete=models.CASCADE)
	typeCate = models.ForeignKey(Coursetype, on_delete=models.CASCADE)
	peopleCate = models.ForeignKey(Specialgroup, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

#The following four tables are linked with Recipe table
class Mainingredient(models.Model):
	name = models.charField(max_length=30, null=False)

	def __str__(self):
		return self.name

class Scenario(models.Model):
	name = models.charField(max_length=30, null=False)

	def __str__(self):
		return self.name

class Coursetype(models.Model):
	name = models.charField(max_length=30, null=False)

	def __str__(self):
		return self.name

class Specialgroup(models.Model):
	name = models.charField(max_length=30, null=False)

	def __str__(self):
		return self.name

#The following defines a user(user name, email and password)
class User(models.Model):
	name = models.charField(max_length=30, null=False)
	email = models.emailField(unique=True)
	password = models.charField(max_length=10, null=False)

	def __str__(self):
		return self.name

#The following defines a comment(content)
class Comment(models.Model):
	name = models.charField(max_length=255, null=Flase, blank=False)

	def __str__(self):
		return self.name

#The following tables are for many-to-many relationship
class Recipe_User(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "User" + str(self.user.id) + "Recipe" +str(self.recipe.id)

class Comment_User(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "User" + str(self.user.id) + "Comment" +str(self.comment.id)

class Recipe_Comment(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Recipe" + str(self.recipe.id) + "Comment" +str(self.comment.id)