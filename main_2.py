class Satellite():
    
    def __init__(self,nom ='', masse = 100, vitesse = 0):
        self.nom = nom
        self.masse = masse
        self.vitesse = vitesse
        
        
    def impulsion(self, force, duree):
        self.vitesse += (force*duree)/self.masse
    
    
    def afficher_vitesse(self):
        print("La vitesse du satellite", self.nom, "=",self.vitesse, '(m/s)')
    
   
    def energie(self):
        self.E = (self.masse * (self.vitesse*self.vitesse)) / 2
        return self.E
    

s = Satellite('Spoutnik',250,10)
s.impulsion(500, 15)
s.afficher_vitesse()
print("l'Energie cinétique du satellite = ",s.energie(),"(J)")