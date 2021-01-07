heureactuelle = input ("Quelle heure est-il ?")
h = int (heureactuelle)
reveil = input ("Dans combien d'heures doit sonner le réveil ?")
r = int (reveil)
a = ( h + r ) % 24
print ("Le réveil sonnera à", a, "heure.")
