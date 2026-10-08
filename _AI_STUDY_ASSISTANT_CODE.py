import mysql.connector as mysqltor
import json
print("=================================")
print("       AI STUDY ASSISTANT")
print("=================================")

myconn=mysqltor.connect(host="localhost",user="root",password="abcd",database="ai_study_assistant")
cursor=myconn.cursor()

try:
    with open("saved_data.json","r") as file:
        data=json.load(file)
        subjects=data["subjects"]
        notes=data["notes"]
    print("Welcome Back!")
except FileNotFoundError:
    subjects = []
    notes={}
    print("Hello New User!")
n=0

while True:

    print("\n1. View Subjects")
    print("2. Add Subject")
    print("3. Add Notes")
    print("4. View Notes")
    print("5. Delete Subject")
    print("6. Edit Subject")
    print("7. Delete Notes")
    print("8. Edit Notes")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        cursor.execute("select * from subjects")
        subjects = cursor.fetchall()

        if len(subjects) == 0:
            print("No subjects added yet.")

        else:
            print("\nYour Subjects:")
            for i in range(len(subjects)):
                sub_name=subjects[i]
                print(i + 1, ".", sub_name[1])

    elif choice == "2":

        subject = input("\nEnter subject name: ")
        cursor.execute("insert into subjects (subject_name) values(%s)",(subject,))
        myconn.commit()
        print("\nSubject added successfully!")
       
    elif choice == "3":
        cursor.execute("select * from subjects")
        subjects = cursor.fetchall()
        if len(subjects) == 0:
            print("\nPlease add a subject first.")
            
        else:
            print("\nSelect a subject.")
            
            for i in range(len(subjects)):
                sub_name=subjects[i]
                print(i+1,".",sub_name[1])

            try:    
                subject_choice=int(input("\nEnter subject number:"))
                
                if subject_choice>=1 and subject_choice<=len(subjects):
                    selected_subject=subjects[subject_choice-1]
                    sub_id=selected_subject[0]
                    
                    note=input("\nEnter your note:")
                    cursor.execute("insert into notes(subject_id,note_text) values(%s,%s)",(sub_id,note,))
                    myconn.commit()
                    print("/nNotes added successfully!")
                        
                else:
                    print("\nInvalid subject number!")
                    
            except ValueError:
                print("\nEnter a valid input please!")

    elif choice == "4":
        
        cursor.execute("select * from subjects")
        subjects = cursor.fetchall() 
        if len(subjects) == 0:
            print("\nPlease add a subject first.")

        else:
            print("\nSelect a subject:")

            for i in range(len(subjects)):
                sub_name=subjects[i]
                print(i + 1, ".", sub_name[1])
                
            try: 
                subject_choice = int(input("\nEnter subject number: "))

                if subject_choice >= 1 and subject_choice <= len(subjects):
                    selected_subject = subjects[subject_choice - 1]
                    sub_name=selected_subject[1]
                    sub_id=selected_subject[0]

                    print("\nNotes for", sub_name + ":")
                    
                    cursor.execute("select*from notes where subject_id = %s",(sub_id,))
                    notes=cursor.fetchall()

                    if len(notes) == 0:
                        print("No notes for this subject yet.")
                        
                    else:
                        for i in range(len(notes)):
                            n_name=notes[i]
                            print(i + 1, ".", n_name[2])

                else:
                    print("Invalid subject number!")
            except ValueError:
                print("\nEnter a valid input please!")
        
    elif choice =="5":
        if len(subjects) ==0:
            print("\nThere are No Subjects!")
            
        else:
            print("\nSelect the subject which you want to delete: ")

            for i in range(len(subjects)):
                print(i+1,".", subjects[i])
                
            try:
                subject_choice = int(input("\nEnter subject number: "))
                
                if subject_choice>=1 and subject_choice <= len(subjects):
                    if subjects[subject_choice-1] in notes:
                        deleted_notes=notes[subjects[subject_choice-1]]
                        del notes[subjects[subject_choice-1]]
                        deleted_subject=subjects.pop(subject_choice-1)
                        print("\nThe Deleted subject is: ", deleted_subject)
                        print("\nThe Deleted subject notes are: ", deleted_notes)

                    else:
                        deleted_subject=subjects.pop(subject_choice-1)
                        print("\nThe Deleted subject is: ", deleted_subject)
                        print("\nNo notes of this subject were added! ")
                        
                else:
                    print("\nNo such subject exist!")
                    
            except ValueError:
                print("\nPlease enter a valid input! ")
                    
    elif choice =="6":
        if len(subjects) ==0:
            print("\nNo subjects to Edit! ")
        else:
            print("\nSelect the subject you want to Edit:")

            for i in range(len(subjects)):
                print(i+1,".",subjects[i])
                
            try:
                subject_choice = int(input("\nEnter the subject number:"))

                if subject_choice>=1 and subject_choice<= len(subjects):
                    new_subname=input("\nEnter new subject name: ")
                    print("subject name changed from",subjects[subject_choice-1],"--->",new_subname)
                    old_subname=subjects[subject_choice-1]
                    subjects[subject_choice-1]=new_subname
                    
                    if old_subname in notes:
                        notes[new_subname]=notes[old_subname]
                        del notes[old_subname]
                        
                    else:
                        print("\nNo notes of this subject exists! ")
                        
                else:
                    print("\nNo such subject exists! ")
                    
            except ValueError:
                print("\nPlease enter a valid input! ")
            

    elif choice =="7":
        if len(subjects) ==0:
            print("\nAdd a subjects First!")
            
        else:
            print("\nSelect a subject First:")
            
            for i in range(len(subjects)):
                print(i+1,".",subjects[i])
                
            try:    
                subject_choice=int(input("\nEnter the subject number:"))
                
                if subject_choice>=1 and subject_choice<=len(subjects):
                    
                    if subjects[subject_choice-1] not in notes:
                        print("\nAdd notes First!")
                        
                    else:
                        print("\nSelect the note you want to Delete:")
                        
                        for i in notes[subjects[subject_choice-1]]:
                            n=n+1
                            print(n,".",i)
                        n=0    
                        
                        try:    
                            note_choice=int(input("\nEnter the serial number of the note which you want to delete:"))
                        
                            if note_choice>=1 and note_choice<=len(notes[subjects[subject_choice-1]]):
                                deleted_note=notes[subjects[subject_choice-1]].pop(note_choice-1)
                                print("\nDelete note:",deleted_note)
                                
                            else:
                                print("\nNo note at that serial number exists!")
                            
                        except ValueError:
                            print("\nEnter a valid input!")
                        
                else:
                    print("\nNo subject at that serial number exists!")
                     
            except ValueError:
                print("\nEnter a valid input!")
                    
    elif choice =="8":
        if len(subjects) ==0:
            print("\nAdd a subjects First!")
            
        else:
            print("\nSelect a subject First:")
            
            for i in range(len(subjects)):
                print(i+1,".",subjects[i])
                
            try:    
                subject_choice=int(input("\nEnter the subject number:"))
                
                if subject_choice>=1 and subject_choice<=len(subjects):
                    
                    if subjects[subject_choice-1] not in notes:
                        print("\nAdd notes First!")
                        
                    else:
                        print("\nSelect the note you want to Edit:")
                        
                        for i in notes[subjects[subject_choice-1]]:
                            n=n+1
                            print(n,".",i)
                        n=0    
                        
                        try:    
                            note_choice=int(input("\nEnter the serial number of the note which you want to Edit:"))
                        
                            if note_choice>=1 and note_choice<=len(notes[subjects[subject_choice-1]]):
                                New_note=input("\nAdd new note:")
                                old_note=notes[subjects[subject_choice-1]][note_choice-1]
                                print("Note changed in ",subjects[subject_choice-1]," from ",old_note," ----> ",New_note)
                                notes[subjects[subject_choice-1]][note_choice-1]=New_note
                                  
                            else:
                                print("\nNo note at that serial number exists!")
                            
                        except ValueError:
                            print("\nEnter a valid input!")
                        
                else:
                    print("\nNo subject at that serial number exists!")
                     
            except ValueError:
                print("\nEnter a valid input!")
        
            
    elif choice == "9":
        data={"subjects":subjects,"notes":notes}
        with open("saved_data.json","w") as file:
            json.dump(data,file)
        myconn.close()    
        print("\nThank you for using AI Study Assistant!")
        break

    else:
        print("\nInvalid choice!")
