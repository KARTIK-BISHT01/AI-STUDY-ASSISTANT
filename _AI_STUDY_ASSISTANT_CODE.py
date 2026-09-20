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
    print("5. Exit")

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
        

    elif choice == "5":
        print("\nThank you for using AI Study Assistant!")
        break

    else:
        print("\nInvalid choice!")
