def main_menu():
    print("\nMain Menu:")
    print("1. AD Carry")
    print("2. Support")
    print("3. Jungle")
    print("4. EXIT")

def AD_Carry():
    print("\nAD_Carrys")
    print("1. Varus")
    print("2. Zeri")
    print("3. Smolder")  
    print("4. Back to Main Menu")      
def Support():
    print("\nSupports")
    print("1. Lulu")
    print("2. Tahm Kench")
    print("3. Maokai")
    print("4. Back to Main Menu")
def Jungle():
    print("\nJungler")
    print("1. Nunu")
    print("2. Viego")
    print("3. Xin Zhao")
    print("4. Back to Main Menu")
def detaild_info(option):
    if option == "1":
            print("\nVarus Win rate is 49.22, pick rate is 5.12 and Varus ban rate is 1.47")
    elif option == "2":
            print("\nZeri's win rate is 48.94, pick rate is 4.28 and zeri's ban rate is 1.47")
    elif option == "3":
            print("\nSmolder's win rate is 47.50, pick rate is 7.68 and Smolder's ban rate is 20.49")
    elif option == "4":
            print("\nLulu's win rate is 52.36, pick rate is 11.81 and Lulu's ban rate is 8.48")
    elif option == "5":
            print("\nTahm Kench's win rate is 53.03, pick rate is 1.47 and Tahm Kench's ban rate is 1.47")
    elif option == "6":
            print("\nMaokai's win rate is 50.17, pick rate is 1.55 and Maokai's ban rate is 0.34")
    elif option == "7":
            print("\nNunu's win rate is 51.8, pick rate is 2.69 and Nunu's ban rate is 0.63")
    elif option == "8":
            print("\nViego's win rate is 51.13, pick rate is 13.43 and Viego's ban rate is 6.69")
    elif option == "9":
            print("\nXin Zhao's win rate is 52.84, pick rate is 4.68 and Xin Zhao's ban rate is 1.26")
        

def main():
    while True:
        main_menu()
        chosen = input("Select an option: ")

        if chosen == "1":
                while True:
                    AD_Carry()
                    adc_choice = input("Select an ADC champ: ")
                    if adc_choice in ["1", "2", "3"]:
                        detaild_info(adc_choice)
                    elif adc_choice == "4":
                        break
                    else:
                        print("invalid choice. please select again.")

        elif chosen == "2":
                    while True:
                        Support()
                        Sup_choice = input("Select an Sup champ: ")
                        if Sup_choice in ["1", "2", "3"]:
                            detaild_info(str(int(Sup_choice) + 3))
                        elif Sup_choice == "4":
                            break
                        else:
                            print("invalid choice. please select again.")
           
        elif chosen == "3":
                    while True:
                        Jungle()
                        Jug = input("Select an Jug champ: ")
                        if Jug in ["1", "2", "3"]:
                            detaild_info(str(int(Jug) + 6))
                        elif Jug == "4":
                            break
                        else:
                            print("invalid choice. please select again.")
           
        elif chosen == "4":
            print("Exiting...")
            break
        else: 
            print("invalid choice. please select again")
        
if __name__ == "__main__":
  main()
