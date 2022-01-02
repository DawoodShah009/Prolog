# First of all we integrated Python version 3.7 with Prolog version swipl-w64-764.
# Problem Statment:
# We have a Family Tree, our task is to use python as a frontend and prolog as a backend  coding languages.
# So we can find our favourite relatives from family tree. 

from pyswip import Prolog, Functor, Variable, Query, call
prolog = Prolog()
prolog.consult("Family_Tree.pl")
Menu = True

print("|==================================================FAMILY TREE================================================|")
print("|                                                                                                             |")
print("|_____________________________________________________________________________________________________________|")
print("|                   chotakhan <----> chotirani                             barakhan <----> barirani           |")
print("|                      /        |          \                                    /              \              |")
print("|                     /         |           \                                  /                \             |")
print("|                    /          |            \                                /                  \            |")
print("|    salim <----> kausar      nadir          asad                           nahid                 sumra       |")
print("|            |                   ^--------/-----^---------|---------------\-------^                   ^       |")
print("|            |                           /      ^---------|----------------\--------------|----------\^       |")
print("|            |                          /                 |                 \             |           \       |")
print("|            |                        burhan           rashid              akram          |            \      |")
print("|          rizwan                                                                        salima       sanam   |")
print("|           ^ -------------------------------------------|----------------------------------------------^     |")
print("|                                                        |                                                    |")
print("|                                                      rabia                                                  |")
print("|                                                                                                             |")
print("|_____________________________________________________________________________________________________________|")
print(" ")
print(" ")
print("    For Baap : 1")
print("    For Maan : 2")
print("    For Beti : 3")
print("    For Beta : 4")
print("    For Dada : 5")
print("    For Nana : 6")
print("    For Dadi : 7")
print("    For Nani : 8")
print("    For Biwi : 9")
print("    For Sala : 10")
print("    For Behn : 11")
print("    For Bhai : 12")
print("    For Khala : 13")
print("    For Chacha : 14")
print("    For Sussar : 15")
print("    For Exit : 20")
print(" ")
while  Menu == True:
        
              
    input_num = int(input("Enter respective number for the relation you want to identify:\n"))
    if input_num == 20:
        Menu = False
    if input_num == 1:
        P=input("If you want to check all the relations for your seleted number enter 'Of' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("baap(Baap,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have father. ")    
        else: 
            print(variable_a)
            
    elif input_num == 2:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("maan(Maan,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have mother. ")    
        else: 
            print(variable_a)
            
    elif input_num == 3:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("beti(Beti,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have daughter. ")    
        else: 
            print(variable_a)
            
    if input_num == 4:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("beta(Beta,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have son. ")    
        else: 
            print(variable_a)
            
    if input_num == 5:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("dada(Dada,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have grandfather. ")    
        else: 
            print(variable_a)
            
    if input_num == 6:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("nana(Nana,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have grandfather. ")    
        else: 
            print(variable_a)

    if input_num == 7:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("dadi(Dadi,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have grandmother. ")    
        else: 
            print(variable_a)

    if input_num == 8:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("nani(Nani,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have grandmother. ")    
        else: 
            print(variable_a)

    if input_num == 9:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("mianbiwi(Her_Husband_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She is not married. ")    
        else: 
            print(variable_a)

    if input_num == 10:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("sala(Brother_in_Law_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have son. ")    
        else: 
            print(variable_a)

    if input_num == 11:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("behn(Sister_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have sister. ")    
        else: 
            print(variable_a)

    if input_num == 12:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("bhai(Brother_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have brother. ")    
        else: 
            print(variable_a)

    if input_num == 13:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("khala(Aunt_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have aunt. ")    
        else: 
            print(variable_a)

    if input_num == 14:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("chacha(Uncle_is,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have uncle. ")    
        else: 
            print(variable_a)

    if input_num == 15:
        P=input("If you want to check all the relations for your seleted number enter 'All' otherwise\
Enter the name of person from the family tree whoes relation you want to check:\n")
        variable_a =list(prolog.query("sussar(Father_in_Law,"+str(P)+")"))
        if variable_a == []:
            print(" He/She doesn't have Father_in_Law. ")    
        else: 
            print(variable_a)

    