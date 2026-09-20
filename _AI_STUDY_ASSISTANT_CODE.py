print("=================================")
print("       AI STUDY ASSISTANT")
print("=================================")

subjects = []
notes={}
while True:

    print("\n1. View Subjects")
    print("2. Add Subject")
    print("3. Add Notes")
    print("4. View Notes")
    print("5. Delete Subject")
    print("6. Edit Subject")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        if len(subjects) == 0:
            print("No subjects added yet.")

        else:
            print("\nYour Subjects:")
            for i in range(len(subjects)):
                print(i + 1, ".", subjects[i])

    elif choice == "2":

        subject = input("\nEnter subject name: ")

        subjects.append(subject)

        print("Subject added successfully!")

    elif choice == "3":
        if len(subjects)==0:
            print("\nPlease add a subject first.")
            
        else:
            print("\nSelect a subject.")
            
            for i in range(len(subjects)):
                print(i+1,".",subjects[i])

            try:    
                subject_choice=int(input("\nEnter subject number:"))
                
                if subject_choice>=1 and subject_choice<=len(subjects):
                    selected_subject=subjects[subject_choice-1]
                    
                    note=input("\nEnter your note:")
                    
                    if selected_subject not in notes:
                        notes[selected_subject]=[]
                    notes[selected_subject].append(note)
                    print("\nNote added successfully!")
                        
                else:
                    print("\nInvalid subject number!")
            except ValueError:
                print("\nEnter a valid input please!")

    elif choice == "4":

        if len(subjects) == 0:
            print("\nPlease add a subject first.")

        else:
            print("\nSelect a subject:")

            for i in range(len(subjects)):
                print(i + 1, ".", subjects[i])
                
            try: 
                subject_choice = int(input("\nEnter subject number: "))

                if subject_choice >= 1 and subject_choice <= len(subjects):

                    selected_subject = subjects[subject_choice - 1]

                    print("\nNotes for", selected_subject + ":")

                    if selected_subject not in notes or len(notes[selected_subject]) == 0:
                        print("No notes for this subject yet.")

                    else:
                        for i in range(len(notes[selected_subject])):
                            print(i + 1, ".", notes[selected_subject][i])

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
            print("\nSelect the you want to Edit:")

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
            

    elif choice == "7":
        print("\nThank you for using AI Study Assistant!")
        break

    else:
        print("\nInvalid choice!")
