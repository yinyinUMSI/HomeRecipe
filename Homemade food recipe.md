Homemade food recipe
Homemade food recipes are memories of close people. It would be nice to share those memories and gives others a chance to taste the delicious food. The web app I want to develop encourages everyone to share their recipes and stories behind it. 

Functions:
Users can publish their own recipes, bookmark other’s recipes, comment the recipes.
When publishing a recipe, the user can write the steps of cooking it, the memories behind the recipe and whether it is suitable for children, vegan and vegetarian. Users can bookmark other’s recipe and get a collection to look through. The recipes can also be commented. Other users who have cooked according to the recipe can give some comments on how good it is. 
Data models
Users (User_id, name, recipe_id(published), recipe_id(bookmarked))
Recipes (recipe_id, recipe_name, content, memories, recipe_type)
Recipe type (Everyone, vegetarian, vegan, good for children)
Bookmarked recipe (recipe_id, bookmarked_time)
Comments (User_id, User_name, comment, comment_time)

Similar applications:
Tasty

Interactive elements:
Bookmarked recipes
Others’ recipes with tags and comments below
