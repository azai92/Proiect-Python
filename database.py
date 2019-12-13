from tkinter import  *
import sqlite3

root = Tk()

# Conectare la baza de date

conn = sqlite3.connect('baza_de_date.db')

# Creare Cursor
c = conn.cursor()

# Creare Tabel
#c.execute("""CREATE TABLE adrese (
#        prenume text,
#        nume text,
#        adresa text,
#        oras text,
#        judet text,
#        cod_postal integer)""")


# Creare functie stergere inregistrare
def delete():
    # Conectare la baza de date
    conn = sqlite3.connect('baza_de_date.db')
    # Creare cursor
    c = conn.cursor()

    # Stergere inregistrare
    c.execute('DELETE from adrese WHERE oid = ' + delete_box.get())

    # Commit
    conn.commit()
    # Close
    conn.close()

# Creare functie submit

def submit():
    # Conectare la baza de date
    conn = sqlite3.connect('baza_de_date.db')
    # Creare cursor
    c = conn.cursor()

    # Inserare in tabel
    c.execute('INSERT INTO adrese VALUES (:prenume, :nume, :adresa, :oras, :judet, :cod_postal)',
              {
                  'prenume': prenume.get(),
                  'nume': nume.get(),
                  'adresa': adresa.get(),
                  'oras': oras.get(),
                  'judet': judet.get(),
                  'cod_postal': cod_postal.get()

              })
    # Commit
    conn.commit()

    # Close
    conn.close()

    # Clear la text box

    prenume.delete(0, END)
    nume.delete(0, END)
    adresa.delete(0, END)
    oras.delete(0, END)
    judet.delete(0, END)
    cod_postal.delete(0, END)

# Creare functie interogare
def query():
    # Conectare la baza de date
    conn = sqlite3.connect('baza_de_date.db')
    # Creare cursor
    c = conn.cursor()

    # Interogare baza de date
    c.execute('SELECT *, oid FROM adrese')
    records = c.fetchall()
    print(records)

    # Parcurgere inregistrari
    print_records = ''

    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[6]) + '\n'

    query_label = Label(root, text = print_records)
    query_label.grid(row = 11, column = 0, columnspan = 2)

    # Commit
    conn.commit()
    # Close
    conn.close()


# Creare casute de text
prenume = Entry(root, width = 30)
prenume.grid(row = 0, column = 1, padx = 20)
nume = Entry(root, width = 30)
nume.grid(row = 1, column = 1, padx = 20)
adresa = Entry(root, width = 30)
adresa.grid(row = 2, column = 1, padx = 20)
oras = Entry(root, width = 30)
oras.grid(row = 3, column = 1, padx = 20)
judet = Entry(root, width = 30)
judet.grid(row = 4, column = 1, padx = 20)
cod_postal = Entry(root, width = 30)
cod_postal.grid(row = 5, column = 1, padx = 20)
delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1)


# Creare etichete
prenume_label = Label(root, text = 'Prenume')
prenume_label.grid(row = 0, column = 0)
nume_label = Label(root, text = 'Nume')
nume_label.grid(row = 1, column = 0)
adresa_label = Label(root, text = 'Adresa')
adresa_label.grid(row = 2, column = 0)
oras_label = Label(root, text = 'Oras')
oras_label.grid(row = 3, column = 0)
judet_label = Label(root, text = 'Judet')
judet_label.grid(row = 4, column = 0)
cod_postal_label = Label(root, text = 'Cod Postal')
cod_postal_label.grid(row = 5, column = 0)
delete_box_label = Label(root, text = 'Numar ID')
delete_box_label.grid(row = 9, column = 0)


# Creare buton de submit
submit_btn = Button(root, text = 'Insereaza Inregistrarile', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Creare buton de interogare
query_btn = Button(root, text = 'Afiseaza inregistrarile', command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Creare buton de stergere
delete_btn = Button(root, text = 'Sterge inregistrarile (dupa ID)', command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Commit
conn.commit()
#Close
conn.close()

root.mainloop()