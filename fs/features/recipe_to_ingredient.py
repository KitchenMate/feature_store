import pandas as pd

from fs.feature import Feature


class RecipeToIngredient(Feature):

    def __init__(self):
        Feature.__init__(self)

    def create_feature(self):
        recipes = pd.read_sql_query(f"""
            select id, name from recipes
            where root_recipe_id = id
        """, con=self.fridge.engine)
        print(recipes)  
        return "recipe_to_ingredients", ['recipes', 'ingredients'], recipes

a = RecipeToIngredient()
a.create_feature()

