import os
import shutil
import time
#from distutils.dir_util import copy_tree


def main():
    backup()
    

def backup():
    #defines the directories being used for backups and displays information to the user.
    src_dir = "C:\\Users\\Dangles\\OneDrive\\Desktop\\Python Projects\\GPC Script\\source"
    back_dir = "C:\\Users\\Dangles\\OneDrive\\Desktop\\Python Projects\\GPC Script\\backup"
    
    print("Backing up files from" + src_dir)
    time.sleep(1.5)
    print("Listing files...")
    time.sleep(1.5)
    print(os.listdir(src_dir))
    time.sleep(1.5)
    #asks the user if they would like to copy individual files or the whole directory
    whole_or_indv_check = "true"
    while whole_or_indv_check == "true":
        #this asks the user if they would like to back up everything or just an individual file
        print("Would you like to copy the all the contents of this directory OR individual files?")
        whole_or_indv = input("Please enter WHOLE or SINGLE: ")
        #converts input text to lowercase to make validation easier
        whole_or_indv = whole_or_indv.lower()
        
        #if they want every file, the script loops through every file in the source directory, printing the name, copying it, and adding a slight delay
        if whole_or_indv == "whole":
            print("Backing up whole directory!")
            src_dir_items = os.listdir(src_dir)
            for x in src_dir_items:
                print(x)
                shutil.copy(src_dir + "\\" + x, back_dir)
                time.sleep(0.2)
            #once the loop is finished, it closes out of the script
            time.sleep(1)
            print("Back up has been completed successfully!")
            time.sleep(2)
            exit()
        
        #if the user wants to add individual files, it will break out of this loop
        elif whole_or_indv == "single":
            break
        
        #trips if the user has literacy problems
        else:
            print("Please enter a valid input!")
            
    
    #initializes while loop condition 
    cont_loop = "true"
    #while loop runs continuously until user says they do not want to add more files to the back up
    while cont_loop == "true":
        #asks the user what the name of the file they want to backup
        file_name = input("Enter the name of the name of the first file you would like to copy, include extension: ")
        
        #copies the file
        shutil.copy(src_dir + "\\" + file_name, back_dir)
        print("Backing up " + file_name + "!" )
        
        #asks user if they would like to continue backing up files, uses while loop to keep the process running if a user inputs a wrong answer
        cont_loop_val = "true"
        while cont_loop_val == "true":
            cont_loop_inp = input("Would you like to back up more files? ")
            cont_loop_inp = cont_loop_inp.lower()
            print(cont_loop_inp)
            
            #triggers if the user is done adding files
            if cont_loop_inp == "no":
                print("You entered NO")
                cont_loop = "false"
                print("Back up is complete!")
                time.sleep(1.5)
                break
            
            #resets the loop and allows for more files to be added.
            elif cont_loop_inp == "yes":
                print("You entered YES")
                cont_loop = "true"
                break
            
            #literacy check #2
            else:
                print("Please enter a valid input.")

            
main()