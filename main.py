

class Livre:
    def __init__(self, titre, auteur, anne_date):
        self.titre = titre
        self.auteur = auteur
        self.anne_date = anne_date



class LogicLivre:
    def __init__(self, livre_bank_list, livre_bank_dic, livre_emprunt):
        self.livre_bank_list = livre_bank_list
        self.livre_bank_dic = livre_bank_dic
        self.livre_emprunt = livre_emprunt
        self.livre_id = 0

    def ajoute_un_livre(self):
        titre_livre = input("Entrer le titre du livre :")
        auteur_livre = input("Entrer l'auteur du livre :")
        date_de_publication = input("Entrer la date de publication :")


        """cree un livre ici """
        livre = Livre(titre=titre_livre, auteur=auteur_livre, anne_date=date_de_publication)
        self.livre_id += 1

        self.livre_bank_dic = {

            "id": self.livre_id,
            "titre": livre.titre,
            "auteur": livre.auteur,
            "date": livre.anne_date
        }


        self.livre_bank_list.append(self.livre_bank_dic)
        print("*success* Le livre a ete ajouter dans le pagner")

    def voir_tout_les_livre(self):
        index = 0
        print(f"List des livre disponible | Total: {len(self.livre_bank_list)} |".upper())
        print("")
        for film_ in self.livre_bank_list:
            index += 1
            print(f"[{index}]. {film_['titre']} | {film_['auteur']} | {film_['date']}")


    def emprunt_du_livre(self):
        print(" ")
        print("livre disponible".upper())
        self.voir_tout_les_livre()
        print(" ")
        try:
            index = int(input("Entrer index du livre que vous voulez emprunte :"))

            print("Convertion Failed")

            if self.verification_(index, self.livre_bank_list):
                print("Desoler l'index es n'existe pas")
            else:
                emprunt = self.livre_bank_list[index - 1]
                self.livre_emprunt.append(emprunt)
                self.livre_bank_list.remove(emprunt)
                print("*success* Le livre a ete ajouter dans le pagner")
        except:
            print(" ")
            print("Le numéro d'index doit être un nombre entier et non une chaîne|".upper())

    # verification ( pour controller une erreur )
    def verification_(self, index, bank_list):
        return  index > len(bank_list)

    def afficher_emprunt(self):
        print(f" livre Emprunt | TOTAL : {len(self.livre_emprunt)} |".upper())
        index = 0
        for livre_ in self.livre_emprunt:
            index += 1
            print(f"[{index}]. {livre_['titre']} | {livre_['auteur']} | {livre_['date']}")

    def retourner_un_livre(self):
        print("List des livre impruntes")
        self.afficher_emprunt()
        print("")

        try:
            index = int(input("Entrer index du livre que vous voulez emprunte :"))
            if self.verification_(index, self.livre_emprunt):
                print("Desoler l'index es n'existe pas")
            else:
                retourner = self.livre_emprunt[index - 1]
                self.livre_emprunt.remove(retourner)
                self.livre_bank_list.append(retourner)
                print("*success* le livre a ete retourner .")
        except:
            print(" ")
            print("Le numéro d'index doit être un nombre entier et non une chaîne|".upper())


class Manuel:
    def __int__(self):
        pass

    def afficher_le_manuel(self):
        print("")
        print(" [ A ] Ajouter un livre")
        print(f" [ L ] Voir touts les livres")
        print(" [ E ] Enregistrer un imprudent ")
        print(" [ R ] Retourner un livre")
        print(" [ T ] Afficher l’état des emprunts")
        print(" [ Q ] Quitter")





# logic principal ( nous somme dans le main ici)

livre_emprunt = [ ]
livre_list = [ ]
livre_dic = { }
logic_livre = LogicLivre(livre_list, livre_dic, livre_emprunt)
continue_a_lancer = True
manuel = Manuel()


while continue_a_lancer:

    manuel.afficher_le_manuel()
    print(" ")
    choix = input("Entrer votre choix ( A, L ,E ,R , Q , T ) :")

    if choix.lower() == "A".lower():
        logic_livre.ajoute_un_livre()

    elif choix.lower() == "L".lower():
        logic_livre.voir_tout_les_livre()
    elif choix.lower() == "E".lower():

        if (len(livre_list)) == 0:
            print(f"*error* |STOCK VIDE| le stock disponible est de est {len(livre_list)}")
        else:
            logic_livre.emprunt_du_livre()

    elif choix.lower() == "R".lower():
        logic_livre.retourner_un_livre()
    elif choix.lower() == "T".lower():
        if len(livre_emprunt) == 0:
            print("")
            print(f"*warning* Stock des empruntes est de | {len(livre_emprunt)} |")
        else:
            logic_livre.afficher_emprunt()

    elif choix.lower() == "Q".lower():
        print("")
        continue_a_lancer = False
        print("| * | Merci et a la prochaine | * |")
        print("")
        print("Auteur:  SOH TAGNE ACHILLE IVES")

    else:
        print(f"*error* Desoler mais le choix { choix } n'existe pas :")












