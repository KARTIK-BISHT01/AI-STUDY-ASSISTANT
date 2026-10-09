import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector as mysqltor

myconn = mysqltor.connect(host="localhost", user="root", password="abcd", database="ai_study_assistant")
cursor = myconn.cursor()

current_subjects = []

def refresh_subjects():
    global current_subjects
    subject_listbox.delete(0, tk.END)
    cursor.execute("select * from subjects")
    current_subjects = cursor.fetchall()
    for i, row in enumerate(current_subjects, start=1):
        subject_listbox.insert(tk.END, f"{i} - {row[1]}")

def add_subject():
    name = subject_entry.get()
    if name.strip() == "":
        messagebox.showwarning("Error", "Subject name can't be empty!")
        return
    cursor.execute("insert into subjects (subject_name) values (%s)", (name,))
    myconn.commit()
    subject_entry.delete(0, tk.END)
    refresh_subjects()

def delete_subject():
    selection = subject_listbox.curselection()
    if not selection:
        messagebox.showwarning("Error", "Select a subject first!")
        return
    sub_id = current_subjects[selection[0]][0]
    cursor.execute("delete from subjects where id = %s", (sub_id,))
    myconn.commit()
    refresh_subjects()

def edit_subject():
    selection = subject_listbox.curselection()
    if not selection:
        messagebox.showwarning("Error", "Select a subject first!")
        return
    sub_id = current_subjects[selection[0]][0]
    new_name = simpledialog.askstring("Edit Subject", "Enter new subject name:")
    if new_name:
        cursor.execute("update subjects set subject_name = %s where id = %s", (new_name, sub_id))
        myconn.commit()
        refresh_subjects()

def open_notes_window():
    selection = subject_listbox.curselection()
    if not selection:
        messagebox.showwarning("Error", "Select a subject first!")
        return

    sub_id = current_subjects[selection[0]][0]
    sub_name = current_subjects[selection[0]][1]

    current_notes = []

    notes_window = tk.Toplevel(window)
    notes_window.title(f"Notes for {sub_name}")
    notes_window.geometry("400x400")

    notes_listbox = tk.Listbox(notes_window, width=50)
    notes_listbox.pack(pady=10)

    notes_entry = tk.Entry(notes_window, width=40)
    notes_entry.pack(pady=5)

    def refresh_notes():
        nonlocal current_notes
        notes_listbox.delete(0, tk.END)
        cursor.execute("select * from notes where subject_id = %s", (sub_id,))
        current_notes = cursor.fetchall()
        for i, row in enumerate(current_notes, start=1):
            notes_listbox.insert(tk.END, f"{i} - {row[2]}")

    def add_note():
        text = notes_entry.get()
        if text.strip() == "":
            messagebox.showwarning("Error", "Note can't be empty!")
            return
        cursor.execute("insert into notes (subject_id, note_text) values (%s, %s)", (sub_id, text))
        myconn.commit()
        notes_entry.delete(0, tk.END)
        refresh_notes()

    def delete_note():
        sel = notes_listbox.curselection()
        if not sel:
            messagebox.showwarning("Error", "Select a note first!")
            return
        note_id = current_notes[sel[0]][0]
        cursor.execute("delete from notes where id = %s", (note_id,))
        myconn.commit()
        refresh_notes()

    def edit_note():
        sel = notes_listbox.curselection()
        if not sel:
            messagebox.showwarning("Error", "Select a note first!")
            return
        note_id = current_notes[sel[0]][0]
        new_text = simpledialog.askstring("Edit Note", "Enter new note text:")
        if new_text:
            cursor.execute("update notes set note_text = %s where id = %s", (new_text, note_id))
            myconn.commit()
            refresh_notes()

    tk.Button(notes_window, text="Add Note", command=add_note).pack(pady=2)
    tk.Button(notes_window, text="Edit Selected", command=edit_note).pack(pady=2)
    tk.Button(notes_window, text="Delete Selected", command=delete_note).pack(pady=2)

    refresh_notes()

def on_closing():
    myconn.close()
    window.destroy()

window = tk.Tk()
window.title("AI Study Assistant")
window.geometry("400x450")

subject_listbox = tk.Listbox(window, width=50)
subject_listbox.pack(pady=10)

subject_entry = tk.Entry(window, width=40)
subject_entry.pack(pady=5)

tk.Button(window, text="Add Subject", command=add_subject).pack(pady=2)
tk.Button(window, text="Edit Selected", command=edit_subject).pack(pady=2)
tk.Button(window, text="Delete Selected", command=delete_subject).pack(pady=2)
tk.Button(window, text="View Notes for Selected", command=open_notes_window).pack(pady=2)
tk.Button(window, text="Exit", command=on_closing).pack(pady=2)

window.protocol("WM_DELETE_WINDOW", on_closing)

refresh_subjects()
window.mainloop()
