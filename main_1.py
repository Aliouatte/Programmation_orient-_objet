# younesbelabid@yahoo.com #

class Pizza:
    def __init__(self, nom, prix,ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficher(self):
        print()
        veg_str = ""
        if self.vegetarienne:
            veg_str =  "- végétarienne"
        print("la pizza est une", self.nom, "son prix est", self.prix, "$", veg_str)
        print(" - ".join(self.ingredients))
        print()

class Pizzapersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.1
    dernier_numero = 0
    def __init__(self):
        Pizzapersonnalisee.dernier_numero +=1
        self.numero = Pizzapersonnalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero),0,[]) # -->
        self.demander_ingredients_utilisateur()
        self.calculer_prix_pizza()


    def demander_ingredients_utilisateur(self):
        print()
        print("Ingrédients de la pizza " + str(self.numero))
        while True:
            ingredient = input("Ajouter un ingredient (Enter pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"vous avez {len(self.ingredients)}, ingrédients : {' - '.join(self.ingredients)}")

    def calculer_prix_pizza(self):
        prix_tot_ingredients = self.PRIX_PAR_INGREDIENT * len(self.ingredients)
        self.prix = self.PRIX_DE_BASE + prix_tot_ingredients
        

pizzas = [
          Pizza("4 fromages", 8.5,("brie","emmental","compté","parmesan"), True),
          Pizza("Royales", 12.0,("brie","oignons","merguez","champignos")),
          Pizza("Orientale", 11.0,("oeuf","emmental","sauce tomate","jambon")),
          Pizza("4 saisons", 13.0,("brie","sauce tomate","viande hachée","parmesan")),
          Pizza("Végétarienne", 9.0,("brie","sauce tomate","champignos","parmesan"), True),
          Pizzapersonnalisee(),
          Pizzapersonnalisee()
        ]


for pizza in pizzas:
    pizza.afficher()
