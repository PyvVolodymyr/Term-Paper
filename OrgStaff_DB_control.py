import sqlite3
import tkinter as tk
from tkinter import ttk
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

### ------------------------- Головне вікто програми -------------------------

root = tk.Tk()
root.title('Organization`s Staff DataBase control')
root['bg'] = 'light grey'
root.geometry('1200x700')
root.resizable(height = False, width = False)

main = tk.Frame(root, bg = 'white')
main.place(x = 0, y = 28)

toolbar = tk.Frame(root, bg = 'light grey', bd = 0)
toolbar.pack(fill = tk.X)

### Виведення таблиці "Архів зарплат"
def salary_archive_view():
    main.tree.destroy() # Очищення фрейма

    ### Створення стовпців
    main.tree = ttk.Treeview(main, columns = ('id', 'slr2016/1', 'slr2016/2', 'slr2016/3', 'slr2016/4', 'slr2017/1', 'slr2017/2', 'slr2017/3', 'slr2017/4',
                                              'slr2018/1', 'slr2018/2', 'slr2018/3', 'slr2018/4', 'slr2019/1', 'slr2019/2', 'slr2019/3', 'slr2019/4',
                                              'slr2020/1', 'slr2020/2', 'slr2020/3', 'slr2020/4'), height = 32, show = 'headings')
    
    main.tree.column('id', width = 40, anchor = tk.CENTER)
    main.tree.column('slr2016/1', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2016/2', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2016/3', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2016/4', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2017/1', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2017/2', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2017/3', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2017/4', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2018/1', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2018/2', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2018/3', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2018/4', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2019/1', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2019/2', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2019/3', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2019/4', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2020/1', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2020/2', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2020/3', width = 57, anchor = tk.CENTER)
    main.tree.column('slr2020/4', width = 70, anchor = tk.W)
    
    main.tree.heading('id', text = 'ID')
    main.tree.heading('slr2016/1', text = '2016/1')
    main.tree.heading('slr2016/2', text = '2016/2')
    main.tree.heading('slr2016/3', text = '2016/3')
    main.tree.heading('slr2016/4', text = '2016/4')
    main.tree.heading('slr2017/1', text = '2017/1')
    main.tree.heading('slr2017/2', text = '2017/2')
    main.tree.heading('slr2017/3', text = '2017/3')
    main.tree.heading('slr2017/4', text = '2017/4')
    main.tree.heading('slr2018/1', text = '2018/1')
    main.tree.heading('slr2018/2', text = '2018/2')
    main.tree.heading('slr2018/3', text = '2018/3')
    main.tree.heading('slr2018/4', text = '2018/4')
    main.tree.heading('slr2019/1', text = '2019/1')
    main.tree.heading('slr2019/2', text = '2019/2')
    main.tree.heading('slr2019/3', text = '2019/3')
    main.tree.heading('slr2019/4', text = '2019/4')
    main.tree.heading('slr2020/1', text = '2020/1')
    main.tree.heading('slr2020/2', text = '2020/2')
    main.tree.heading('slr2020/3', text = '2020/3')
    main.tree.heading('slr2020/4', text = '2020/4', anchor = tk.W)

    ### Читання і виведення бази даних
    cursor.execute('''SELECT * FROM salary_archive''')
    data = cursor.fetchall()
    for i in data:
        main.tree.insert('', 'end', values = i)

    ### Недопустити зміну ширини стовпців
    def handle_click(event):
        if main.tree.identify_region(event.x, event.y) == "separator":
            return 'break'
    main.tree.bind('<Button-1>', handle_click)

    main.tree.pack()

### Виведення таблиці "Співробітники"
def staff_view():
    main.tree.destroy() # Очищення фрейма

    ### Створення стовпців
    main.tree = ttk.Treeview(main, columns = ('id', 'name', 'birthday', 'sex', 'family status', 'education', 'salary'), height = 32, show = 'headings')

    main.tree.column('id', width = 75, anchor = tk.CENTER)
    main.tree.column('name', width = 300, anchor = tk.CENTER)
    main.tree.column('birthday', width = 150, anchor = tk.CENTER)
    main.tree.column('sex', width = 75, anchor = tk.CENTER)
    main.tree.column('family status', width = 200, anchor = tk.CENTER)
    main.tree.column('education', width = 200, anchor = tk.CENTER)
    main.tree.column('salary', width = 200, anchor = tk.CENTER)

    main.tree.heading('id', text = 'ID')
    main.tree.heading('name', text = 'ПІБ')
    main.tree.heading('birthday', text = 'Дата народження')
    main.tree.heading('sex', text = 'Стать')
    main.tree.heading('family status', text = 'Сімейний статус')
    main.tree.heading('education', text = 'Освіта')
    main.tree.heading('salary', text = 'Зарплата')

    ### Читання і виведення бази даних
    cursor.execute('''SELECT * FROM staff''')
    data = cursor.fetchall()
    for i in data:
        main.tree.insert('', 'end', values = i)

    ### Недопустити зміну ширини стовпців
    def handle_click(event):
        if main.tree.identify_region(event.x, event.y) == "separator":
            return 'break'
    main.tree.bind('<Button-1>', handle_click)

    main.tree.pack()

### Виведення таблиці "Посади"
def positions_view():
    main.tree.destroy() # Очищення фрейма

    ### Створення стовпців
    main.tree = ttk.Treeview(main, columns = ('id', 'department_number', 'department_name', 'position'), height = 32, show = 'headings')
    
    main.tree.column('id', width = 200, anchor = tk.CENTER)
    main.tree.column('department_number', width = 200, anchor = tk.CENTER)
    main.tree.column('department_name', width = 400, anchor = tk.CENTER)
    main.tree.column('position', width = 400, anchor = tk.CENTER)

    main.tree.heading('id', text = 'ID')
    main.tree.heading('department_number', text = 'Номер відділу')
    main.tree.heading('department_name', text = 'Назва відділу')
    main.tree.heading('position', text = 'Посада')

    ### Читання і виведення бази даних
    cursor.execute('''SELECT * FROM positions''')
    data = cursor.fetchall()
    for i in data:
        main.tree.insert('', 'end', values = i)

    ### Недопустити зміну ширини стовпців
    def handle_click(event):
        if main.tree.identify_region(event.x, event.y) == "separator":
            return 'break'
    main.tree.bind('<Button-1>', handle_click)

    main.tree.pack()

### Ввести посаду(через дочірнє вікно)
def set_position():
    if (not main.tree.selection()[0]): return 0
    set_position_window = tk.Toplevel()
    set_position_window.title('Ввести посду')
    set_position_window['bg'] = 'light grey'
    set_position_window.geometry('400x350')
    set_position_window.resizable(height = False, width = False)

    label_entry_department_number = tk.Label(set_position_window, text = 'Номер відділу', bg = 'light grey')
    label_entry_department_number.place(x = 10, y = 40)
    entry_department_number = ttk.Entry(set_position_window)
    entry_department_number.place(x = 200, y = 40)

    label_entry_department_name = tk.Label(set_position_window, text = 'Назва відділу', bg = 'light grey')
    label_entry_department_name.place(x = 10, y = 80)
    entry_department_name = ttk.Entry(set_position_window)
    entry_department_name.place(x = 200, y = 80)

    label_entry_position = tk.Label(set_position_window, text = 'Посада', bg = 'light grey')
    label_entry_position.place(x = 10, y = 120)
    entry_position = ttk.Entry(set_position_window)
    entry_position.place(x = 200, y = 120)

    def update_data(department_number, department_name, position):
        cursor.execute('''UPDATE positions SET department_number = ?, department_name = ?, position = ? WHERE id = ?''',
                       (department_number, department_name, position, main.tree.set(main.tree.selection()[0], '#1')))
        db.commit()
        positions_view()
        set_position_window.destroy()

    btn_confirm = tk.Button(set_position_window, text = 'Підтвердити', bd = 3)
    btn_confirm.place(x = 70, y = 300)
    btn_confirm.bind('<Button-1>', lambda event: update_data(entry_department_number.get(), entry_department_name.get(), entry_position.get()))

    btn_cancel = tk.Button(set_position_window, text = 'Скасувати', bd = 3)
    btn_cancel.place(x = 180, y = 300)
    btn_cancel.bind('<Button-1>', lambda event: set_position_window.destroy())

    set_position_window.grab_set()
    set_position_window.focus_set()

### Додати запис в БД(через дочірнє вікно)
def add_record():
    add_window = tk.Toplevel()
    add_window.title('Додати запис')
    add_window['bg'] = 'light grey'
    add_window.geometry('800x350')
    add_window.resizable(height = False, width = False)

    ### Додавання даних в БД для "Співробітники"
    label_for_staff = tk.Label(add_window, text = 'Співробітник', bg = 'light grey')
    label_for_staff.place(x = 130, y = 5)

    label_entry_name = tk.Label(add_window, text = 'ПІБ', bg = 'light grey')
    label_entry_name.place(x = 10, y = 40)
    entry_name = ttk.Entry(add_window)
    entry_name.place(x = 200, y = 40)

    label_entry_birthday = tk.Label(add_window, text = 'Дата народження(YYYY-MM-DD)', bg = 'light grey')
    label_entry_birthday.place(x = 10, y = 80)
    entry_birthday = ttk.Entry(add_window)
    entry_birthday.place(x = 200, y = 80)

    label_entry_sex = tk.Label(add_window, text = 'Стать', bg = 'light grey')
    label_entry_sex.place(x = 10, y = 120)
    entry_sex = ttk.Entry(add_window)
    entry_sex.place(x = 200, y = 120)

    label_entry_family_status = tk.Label(add_window, text = 'Сімейний статус', bg = 'light grey')
    label_entry_family_status.place(x = 10, y = 160)
    entry_family_status = ttk.Entry(add_window)
    entry_family_status.place(x = 200, y = 160)

    label_entry_education = tk.Label(add_window, text = 'Освіта', bg = 'light grey')
    label_entry_education.place(x = 10, y = 200)
    entry_education = ttk.Entry(add_window)
    entry_education.place(x = 200, y = 200)

    label_entry_salary = tk.Label(add_window, text = 'Зарплата', bg = 'light grey')
    label_entry_salary.place(x = 10, y = 240)
    entry_salary = ttk.Entry(add_window)
    entry_salary.place(x = 200, y = 240)

    ### Додавання даних в БД для "Архіву зарплат"
    label_for_archive = tk.Label(add_window, text = 'Архів зарплат', bg = 'light grey')
    label_for_archive.place(x = 550, y = 5)

    label_arch_1 = tk.Label(add_window, text = '2020/4', bg = 'light grey')
    label_arch_1.place(x = 400, y = 30)
    entry_arch_1 = ttk.Entry(add_window)
    entry_arch_1.place(x = 450, y = 30)

    label_arch_2 = tk.Label(add_window, text = '2020/3', bg = 'light grey')
    label_arch_2.place(x = 400, y = 60)
    entry_arch_2 = ttk.Entry(add_window)
    entry_arch_2.place(x = 450, y = 60)

    label_arch_3 = tk.Label(add_window, text = '2020/2', bg = 'light grey')
    label_arch_3.place(x = 400, y = 90)
    entry_arch_3 = ttk.Entry(add_window)
    entry_arch_3.place(x = 450, y = 90)

    label_arch_4 = tk.Label(add_window, text = '2020/1', bg = 'light grey')
    label_arch_4.place(x = 400, y = 120)
    entry_arch_4 = ttk.Entry(add_window)
    entry_arch_4.place(x = 450, y = 120)

    label_arch_5 = tk.Label(add_window, text = '2019/4', bg = 'light grey')
    label_arch_5.place(x = 400, y = 150)
    entry_arch_5 = ttk.Entry(add_window)
    entry_arch_5.place(x = 450, y = 150)

    label_arch_6 = tk.Label(add_window, text = '2019/3', bg = 'light grey')
    label_arch_6.place(x = 400, y = 180)
    entry_arch_6 = ttk.Entry(add_window)
    entry_arch_6.place(x = 450, y = 180)

    label_arch_7 = tk.Label(add_window, text = '2019/2', bg = 'light grey')
    label_arch_7.place(x = 400, y = 210)
    entry_arch_7 = ttk.Entry(add_window)
    entry_arch_7.place(x = 450, y = 210)

    label_arch_8 = tk.Label(add_window, text = '2019/1', bg = 'light grey')
    label_arch_8.place(x = 400, y = 240)
    entry_arch_8 = ttk.Entry(add_window)
    entry_arch_8.place(x = 450, y = 240)
    
    label_arch_9 = tk.Label(add_window, text = '2018/4', bg = 'light grey')
    label_arch_9.place(x = 400, y = 270)
    entry_arch_9 = ttk.Entry(add_window)
    entry_arch_9.place(x = 450, y = 270)

    label_arch_10 = tk.Label(add_window, text = '2018/3', bg = 'light grey')
    label_arch_10.place(x = 400, y = 300)
    entry_arch_10 = ttk.Entry(add_window)
    entry_arch_10.place(x = 450, y = 300)

    label_arch_11 = tk.Label(add_window, text = '2018/2', bg = 'light grey')
    label_arch_11.place(x = 600, y = 30)
    entry_arch_11 = ttk.Entry(add_window)
    entry_arch_11.place(x = 650, y = 30)

    label_arch_12 = tk.Label(add_window, text = '2018/1', bg = 'light grey')
    label_arch_12.place(x = 600, y = 60)
    entry_arch_12 = ttk.Entry(add_window)
    entry_arch_12.place(x = 650, y = 60)

    label_arch_13 = tk.Label(add_window, text = '2017/4', bg = 'light grey')
    label_arch_13.place(x = 600, y = 90)
    entry_arch_13 = ttk.Entry(add_window)
    entry_arch_13.place(x = 650, y = 90)

    label_arch_14 = tk.Label(add_window, text = '2017/3', bg = 'light grey')
    label_arch_14.place(x = 600, y = 120)
    entry_arch_14 = ttk.Entry(add_window)
    entry_arch_14.place(x = 650, y = 120)

    label_arch_15 = tk.Label(add_window, text = '2017/2', bg = 'light grey')
    label_arch_15.place(x = 600, y = 150)
    entry_arch_15 = ttk.Entry(add_window)
    entry_arch_15.place(x = 650, y = 150)

    label_arch_16 = tk.Label(add_window, text = '2017/1', bg = 'light grey')
    label_arch_16.place(x = 600, y = 180)
    entry_arch_16 = ttk.Entry(add_window)
    entry_arch_16.place(x = 650, y = 180)

    label_arch_17 = tk.Label(add_window, text = '2016/4', bg = 'light grey')
    label_arch_17.place(x = 600, y = 210)
    entry_arch_17 = ttk.Entry(add_window)
    entry_arch_17.place(x = 650, y = 210)

    label_arch_18 = tk.Label(add_window, text = '2016/3', bg = 'light grey')
    label_arch_18.place(x = 600, y = 240)
    entry_arch_18 = ttk.Entry(add_window)
    entry_arch_18.place(x = 650, y = 240)
    
    label_arch_19 = tk.Label(add_window, text = '2016/2', bg = 'light grey')
    label_arch_19.place(x = 600, y = 270)
    entry_arch_19 = ttk.Entry(add_window)
    entry_arch_19.place(x = 650, y = 270)

    label_arch_20 = tk.Label(add_window, text = '2016/1', bg = 'light grey')
    label_arch_20.place(x = 600, y = 300)
    entry_arch_20 = ttk.Entry(add_window)
    entry_arch_20.place(x = 650, y = 300)

    ### Кнопки "Підтвердити" та "Скасувати"
    def insert_data(name, birtday, sex, fam_st, edu, sal, slr2016_1, slr2016_2, slr2016_3, slr2016_4, slr2017_1,
                    slr2017_2, slr2017_3,slr2017_4, slr2018_1, slr2018_2, slr2018_3, slr2018_4, slr2019_1,
                    slr2019_2, slr2019_3, slr2019_4,slr2020_1, slr2020_2, slr2020_3, slr2020_4, 
                    department_number, department_name, position):
        all_id = cursor.execute('''SELECT id FROM salary_archive''')
        for_id = 1
        for i in all_id:
            if for_id != i[0]: break
            for_id += 1

        salary_arr = [slr2016_1, slr2016_2, slr2016_3, slr2016_4, slr2017_1, slr2017_2, slr2017_3,slr2017_4, slr2018_1, slr2018_2,
                       slr2018_3, slr2018_4, slr2019_1, slr2019_2, slr2019_3, slr2019_4,slr2020_1, slr2020_2, slr2020_3, slr2020_4]
        for i in range(len(salary_arr)):
            if (salary_arr[i] == ''): salary_arr[i] = None

        cursor.execute('''INSERT INTO staff (id, name, birthday, sex, family_status, education, salary) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (for_id, name, birtday, sex, fam_st, edu, sal))
        cursor.execute('''INSERT INTO salary_archive (id, slr2016_1, slr2016_2, slr2016_3, slr2016_4, slr2017_1, slr2017_2, slr2017_3,
                  slr2017_4, slr2018_1, slr2018_2, slr2018_3, slr2018_4, slr2019_1, slr2019_2, slr2019_3, slr2019_4,slr2020_1,
                  slr2020_2, slr2020_3, slr2020_4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (for_id, salary_arr[0], salary_arr[1], salary_arr[2], salary_arr[3], salary_arr[4], salary_arr[5], salary_arr[6],
                   salary_arr[7], salary_arr[8], salary_arr[9], salary_arr[10], salary_arr[11], salary_arr[12], salary_arr[13],
                   salary_arr[14], salary_arr[15], salary_arr[16], salary_arr[17], salary_arr[18], salary_arr[19]))
        cursor.execute('''INSERT INTO positions (id, department_number, department_name, position) VALUES (?, ?, ?, ?)''',
                       (for_id, department_number, department_name, position))
        db.commit()
        staff_view()
        add_window.destroy()

    btn_confirm = tk.Button(add_window, text = 'Підтвердити', bd = 3)
    btn_confirm.place(x = 70, y = 300)
    btn_confirm.bind('<Button-1>', lambda event: insert_data(entry_name.get(), entry_birthday.get(), entry_sex.get(),
                     entry_family_status.get(), entry_education.get(), entry_salary.get(), entry_arch_1.get(), entry_arch_2.get(),
                     entry_arch_3.get(), entry_arch_4.get(), entry_arch_5.get(), entry_arch_6.get(), entry_arch_7.get(),
                     entry_arch_8.get(), entry_arch_9.get(), entry_arch_10.get(), entry_arch_11.get(), entry_arch_12.get(),
                     entry_arch_13.get(), entry_arch_14.get(), entry_arch_15.get(), entry_arch_16.get(), entry_arch_17.get(),
                     entry_arch_18.get(), entry_arch_19.get(), entry_arch_20.get(), '', '', ''))

    btn_cancel = tk.Button(add_window, text = 'Скасувати', bd = 3)
    btn_cancel.place(x = 180, y = 300)
    btn_cancel.bind('<Button-1>', lambda event: add_window.destroy())

    add_window.grab_set()
    add_window.focus_set()

### Оновити запис в БД(через дочірнє вікно)
def update_record():
    add_window = tk.Toplevel()
    add_window.title('Змінити запис')
    add_window['bg'] = 'light grey'
    add_window.geometry('800x350')
    add_window.resizable(height = False, width = False)

    ### Додавання даних в БД для "Співробітники"
    label_for_staff = tk.Label(add_window, text = 'Співробітник', bg = 'light grey')
    label_for_staff.place(x = 130, y = 5)

    label_entry_name = tk.Label(add_window, text = 'ПІБ', bg = 'light grey')
    label_entry_name.place(x = 10, y = 40)
    entry_name = ttk.Entry(add_window)
    entry_name.place(x = 200, y = 40)

    label_entry_birthday = tk.Label(add_window, text = 'Дата народження(YYYY-MM-DD)', bg = 'light grey')
    label_entry_birthday.place(x = 10, y = 80)
    entry_birthday = ttk.Entry(add_window)
    entry_birthday.place(x = 200, y = 80)

    label_entry_sex = tk.Label(add_window, text = 'Стать', bg = 'light grey')
    label_entry_sex.place(x = 10, y = 120)
    entry_sex = ttk.Entry(add_window)
    entry_sex.place(x = 200, y = 120)

    label_entry_family_status = tk.Label(add_window, text = 'Сімейний статус', bg = 'light grey')
    label_entry_family_status.place(x = 10, y = 160)
    entry_family_status = ttk.Entry(add_window)
    entry_family_status.place(x = 200, y = 160)

    label_entry_education = tk.Label(add_window, text = 'Освіта', bg = 'light grey')
    label_entry_education.place(x = 10, y = 200)
    entry_education = ttk.Entry(add_window)
    entry_education.place(x = 200, y = 200)

    label_entry_salary = tk.Label(add_window, text = 'Зарплата', bg = 'light grey')
    label_entry_salary.place(x = 10, y = 240)
    entry_salary = ttk.Entry(add_window)
    entry_salary.place(x = 200, y = 240)

    ### Додавання даних в БД для "Архіву зарплат"
    label_for_archive = tk.Label(add_window, text = 'Архів зарплат', bg = 'light grey')
    label_for_archive.place(x = 550, y = 5)

    label_arch_1 = tk.Label(add_window, text = '2020/4', bg = 'light grey')
    label_arch_1.place(x = 400, y = 30)
    entry_arch_1 = ttk.Entry(add_window)
    entry_arch_1.place(x = 450, y = 30)

    label_arch_2 = tk.Label(add_window, text = '2020/3', bg = 'light grey')
    label_arch_2.place(x = 400, y = 60)
    entry_arch_2 = ttk.Entry(add_window)
    entry_arch_2.place(x = 450, y = 60)

    label_arch_3 = tk.Label(add_window, text = '2020/2', bg = 'light grey')
    label_arch_3.place(x = 400, y = 90)
    entry_arch_3 = ttk.Entry(add_window)
    entry_arch_3.place(x = 450, y = 90)

    label_arch_4 = tk.Label(add_window, text = '2020/1', bg = 'light grey')
    label_arch_4.place(x = 400, y = 120)
    entry_arch_4 = ttk.Entry(add_window)
    entry_arch_4.place(x = 450, y = 120)

    label_arch_5 = tk.Label(add_window, text = '2019/4', bg = 'light grey')
    label_arch_5.place(x = 400, y = 150)
    entry_arch_5 = ttk.Entry(add_window)
    entry_arch_5.place(x = 450, y = 150)

    label_arch_6 = tk.Label(add_window, text = '2019/3', bg = 'light grey')
    label_arch_6.place(x = 400, y = 180)
    entry_arch_6 = ttk.Entry(add_window)
    entry_arch_6.place(x = 450, y = 180)

    label_arch_7 = tk.Label(add_window, text = '2019/2', bg = 'light grey')
    label_arch_7.place(x = 400, y = 210)
    entry_arch_7 = ttk.Entry(add_window)
    entry_arch_7.place(x = 450, y = 210)

    label_arch_8 = tk.Label(add_window, text = '2019/1', bg = 'light grey')
    label_arch_8.place(x = 400, y = 240)
    entry_arch_8 = ttk.Entry(add_window)
    entry_arch_8.place(x = 450, y = 240)
    
    label_arch_9 = tk.Label(add_window, text = '2018/4', bg = 'light grey')
    label_arch_9.place(x = 400, y = 270)
    entry_arch_9 = ttk.Entry(add_window)
    entry_arch_9.place(x = 450, y = 270)

    label_arch_10 = tk.Label(add_window, text = '2018/3', bg = 'light grey')
    label_arch_10.place(x = 400, y = 300)
    entry_arch_10 = ttk.Entry(add_window)
    entry_arch_10.place(x = 450, y = 300)

    label_arch_11 = tk.Label(add_window, text = '2018/2', bg = 'light grey')
    label_arch_11.place(x = 600, y = 30)
    entry_arch_11 = ttk.Entry(add_window)
    entry_arch_11.place(x = 650, y = 30)

    label_arch_12 = tk.Label(add_window, text = '2018/1', bg = 'light grey')
    label_arch_12.place(x = 600, y = 60)
    entry_arch_12 = ttk.Entry(add_window)
    entry_arch_12.place(x = 650, y = 60)

    label_arch_13 = tk.Label(add_window, text = '2017/4', bg = 'light grey')
    label_arch_13.place(x = 600, y = 90)
    entry_arch_13 = ttk.Entry(add_window)
    entry_arch_13.place(x = 650, y = 90)

    label_arch_14 = tk.Label(add_window, text = '2017/3', bg = 'light grey')
    label_arch_14.place(x = 600, y = 120)
    entry_arch_14 = ttk.Entry(add_window)
    entry_arch_14.place(x = 650, y = 120)

    label_arch_15 = tk.Label(add_window, text = '2017/2', bg = 'light grey')
    label_arch_15.place(x = 600, y = 150)
    entry_arch_15 = ttk.Entry(add_window)
    entry_arch_15.place(x = 650, y = 150)

    label_arch_16 = tk.Label(add_window, text = '2017/1', bg = 'light grey')
    label_arch_16.place(x = 600, y = 180)
    entry_arch_16 = ttk.Entry(add_window)
    entry_arch_16.place(x = 650, y = 180)

    label_arch_17 = tk.Label(add_window, text = '2016/4', bg = 'light grey')
    label_arch_17.place(x = 600, y = 210)
    entry_arch_17 = ttk.Entry(add_window)
    entry_arch_17.place(x = 650, y = 210)

    label_arch_18 = tk.Label(add_window, text = '2016/3', bg = 'light grey')
    label_arch_18.place(x = 600, y = 240)
    entry_arch_18 = ttk.Entry(add_window)
    entry_arch_18.place(x = 650, y = 240)
    
    label_arch_19 = tk.Label(add_window, text = '2016/2', bg = 'light grey')
    label_arch_19.place(x = 600, y = 270)
    entry_arch_19 = ttk.Entry(add_window)
    entry_arch_19.place(x = 650, y = 270)

    label_arch_20 = tk.Label(add_window, text = '2016/1', bg = 'light grey')
    label_arch_20.place(x = 600, y = 300)
    entry_arch_20 = ttk.Entry(add_window)
    entry_arch_20.place(x = 650, y = 300)

    ### Кнопки "Підтвердити" та "Скасувати"
    def insert_data(name, birtday, sex, fam_st, edu, sal, slr2016_1, slr2016_2, slr2016_3, slr2016_4, slr2017_1,
                    slr2017_2, slr2017_3,slr2017_4, slr2018_1, slr2018_2, slr2018_3, slr2018_4, slr2019_1,
                    slr2019_2, slr2019_3, slr2019_4,slr2020_1, slr2020_2, slr2020_3, slr2020_4):

        salary_arr = [slr2016_1, slr2016_2, slr2016_3, slr2016_4, slr2017_1, slr2017_2, slr2017_3,slr2017_4, slr2018_1, slr2018_2,
                       slr2018_3, slr2018_4, slr2019_1, slr2019_2, slr2019_3, slr2019_4,slr2020_1, slr2020_2, slr2020_3, slr2020_4]
        for i in range(len(salary_arr)):
            if (salary_arr[i] == ''): salary_arr[i] = None

        cursor.execute('''UPDATE staff SET name = ?, birthday = ?, sex = ?, family_status = ?, education = ?, salary = ? WHERE id = ?''',
                       (name, birtday, sex, fam_st, edu, sal, main.tree.set(main.tree.selection()[0], '#1')))
        cursor.execute('''UPDATE salary_archive SET slr2016_1 = ?, slr2016_2 = ?, slr2016_3 = ?, slr2016_4 = ?, slr2017_1 = ?,
                  slr2017_2 = ?, slr2017_3 = ?, slr2017_4 = ?, slr2018_1 = ?, slr2018_2 = ?, slr2018_3 = ?, slr2018_4 = ?, slr2019_1 = ?,
                  slr2019_2 = ?, slr2019_3 = ?, slr2019_4 = ?, slr2020_1 = ?, slr2020_2 = ?, slr2020_3 = ?, slr2020_4 = ? WHERE id = ?''',
                  (salary_arr[0], salary_arr[1], salary_arr[2], salary_arr[3], salary_arr[4], salary_arr[5], salary_arr[6],
                   salary_arr[7], salary_arr[8], salary_arr[9], salary_arr[10], salary_arr[11], salary_arr[12], salary_arr[13],
                   salary_arr[14], salary_arr[15], salary_arr[16], salary_arr[17], salary_arr[18], salary_arr[19],
                   main.tree.set(main.tree.selection()[0], '#1')))

        db.commit()
        staff_view()
        add_window.destroy()

    btn_confirm = tk.Button(add_window, text = 'Підтвердити', bd = 3)
    btn_confirm.place(x = 70, y = 300)
    btn_confirm.bind('<Button-1>', lambda event: insert_data(entry_name.get(), entry_birthday.get(), entry_sex.get(),
                     entry_family_status.get(), entry_education.get(), entry_salary.get(), entry_arch_1.get(), entry_arch_2.get(),
                     entry_arch_3.get(), entry_arch_4.get(), entry_arch_5.get(), entry_arch_6.get(), entry_arch_7.get(),
                     entry_arch_8.get(), entry_arch_9.get(), entry_arch_10.get(), entry_arch_11.get(), entry_arch_12.get(),
                     entry_arch_13.get(), entry_arch_14.get(), entry_arch_15.get(), entry_arch_16.get(), entry_arch_17.get(),
                     entry_arch_18.get(), entry_arch_19.get(), entry_arch_20.get()))

    btn_cancel = tk.Button(add_window, text = 'Скасувати', bd = 3)
    btn_cancel.place(x = 180, y = 300)
    btn_cancel.bind('<Button-1>', lambda event: add_window.destroy())

    add_window.grab_set()
    add_window.focus_set()

### Видалення запису в БД
def delete_record():
    for i in main.tree.selection():
        cursor.execute('''DELETE FROM staff WHERE id = ?''', (main.tree.set(i, '#1'),))
        cursor.execute('''DELETE FROM salary_archive WHERE id = ?''', (main.tree.set(i, '#1'),))
        cursor.execute('''DELETE FROM positions WHERE id = ?''', (main.tree.set(i, '#1'),))
        db.commit()
    staff_view()

### Аналіз інформації з БД
def statistic():
    main.tree.destroy() # Очищення фрейма

    canvas_statistic = tk.Canvas(main, width = 1200, height = 700, bg = 'white')
    canvas_statistic.place(x = 0, y = 0)

    ### Дочіпнє вікно для виводу графіків
    def show_diagrams_window(switch):
        diagrams_window = tk.Toplevel()
        diagrams_window.title('Діаграми')
        diagrams_window.geometry('1000x630')
        diagrams_window.resizable(height = False, width = False)

        toolbar_diagrams = tk.Frame(diagrams_window)
        toolbar_diagrams.pack(fill = tk.X)

        canvas = tk.Canvas(diagrams_window, width = 1000, height = 600, bg = 'light blue')
        canvas.pack(side = tk.BOTTOM)

        ### Визначення кроку для осі Y в графіках для загальної та середньої зарплат 
        def y_minmax(switch):
            # bool = 0 - для загальної зарплати, bool = 1 - для середнбої зарплати
            cursor.execute('''SELECT * FROM salary_archive''')
            data = cursor.fetchall()
            salary_by_period = [0] * 20

            for i in range(20):
                sum = 0
                counter = 0
                for j in range(len(data)):
                    if (data[j][i + 1] != None): 
                        sum += data[j][i + 1]
                        counter += 1
                if switch: salary_by_period[i] = sum / counter
                else: salary_by_period[i] = sum
            
            min_value = round(min(salary_by_period))
            max_value = round(max(salary_by_period))

            min_value = math.floor(min_value / int('1' + '0' * (len(str(min_value)) - 2))) * int('1' + '0' * (len(str(min_value)) - 2))
            max_value = math.ceil(max_value / int('1' + '0' * (len(str(max_value)) - 2))) * int('1' + '0' * (len(str(max_value)) - 2))
            return (min_value, max_value)

        ### Осі координат для побудови графіків та сітка
        def coordinate_axis(switch):
            # Вісь X
            canvas.create_line(10, 550, 990, 550, arrow = tk.LAST, fill = 'black')
            for_year = 2016
            for i in range(20):
                canvas.create_line(99 + i * 45, 555, 99 + i * 45, 545, width = 1, fill = 'black')
                canvas.create_text(99 + i * 45, 570, text = ('%s' % for_year + '\n%s кв.' % (i % 4 + 1)), justify = tk.CENTER, font = 'Times 8')
                if i % 4 == 3: for_year += 1
        
            ### Вісь Y
            canvas.create_line(50, 590, 50, 10, arrow = tk.LAST, fill = 'black')
            for_y = y_minmax(switch)
            step = (for_y[1] - for_y[0]) / 10
            for i in range(11):
                canvas.create_line(45, 500 - i * 45, 55, 500 - i * 45, fill = 'black')
                canvas.create_text(25, 500 - i * 45, text = int(for_y[0] + step * i), justify = tk.CENTER, font = 'Times 8')
            
            # Сітка
            for i in range(20):
                    canvas.create_line(99 + i * 45, 0, 99 + i * 45, 546, fill = 'grey')
            for i in range(11):
                    canvas.create_line(55, 500 - i * 45, 1000, 500 - i * 45, fill = 'grey')

        ### Побудова графіка
        def build_diagram(switch):
            cursor.execute('''SELECT * FROM salary_archive''')
            data = cursor.fetchall()

            for_y = y_minmax(switch)
            pixel_step = (for_y[1] - for_y[0]) / 450.0

            X = []
            Y = []
            sum_arr = []
            for i in range(20):
                sum = 0
                count = 0
                for j in range(len(data)):
                    if (data[j][i + 1] != None):
                        sum += data[j][i + 1]
                        count += 1
                if switch: sum /= count
                X.append(99 + i * 45)
                Y.append(500 - (sum - for_y[0]) / pixel_step)
                sum_arr.append(sum)

            for i in range(20):
                if i % 2: canvas.create_rectangle(X[i] - 22, Y[i], X[i] + 22, 550, fill = 'purple')
                else: canvas.create_rectangle(X[i] - 22, Y[i], X[i] + 22, 550, fill = 'dark blue')
                if sum_arr[i] < (for_y[0] + (for_y[1] - for_y[0]) / 2.0):
                    canvas.create_text(X[i], Y[i] - 50, text = round(sum_arr[i] * 10) / 10, angle = 90, font = 'Times 15')
                else: canvas.create_text(X[i], Y[i] + 100, text = round(sum_arr[i] * 10) / 10, angle = 90, font = 'Times 15')
                
        ### Побудова кругової діаграми за статтю
        def pie_chart_by_sex(switch):
            cursor.execute('''SELECT sex, salary FROM staff''')
            data = cursor.fetchall()
            sum_m = 0
            sum_w = 0
            counter = 0
            for i in range(len(data)):
                if data[i][0] == 'ч':
                    sum_m += data[i][1]
                    counter += 1
                elif data[i][0] == 'ж':
                    sum_w += data[i][1]

            if switch == 6:   
                sum_m = counter
                sum_w = len(data) - counter
            elif switch - 2:
                sum_m /= counter
                sum_w /= len(data) - counter

            labels = 'Чоловіки', 'Жінки'
            sizes = [sum_m, sum_w]

            figure, ax = plt.subplots()
            ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 90)
            ax.axis('equal')
            plt.savefig('pie_chart.png')
            plt.close()

            load_img = Image.open('pie_chart.png')
            ready_img = ImageTk.PhotoImage(load_img)

            if switch == 6: str0 = 'Діаграма кадрового складу організації по статі'
            elif switch - 2: str0 = 'Діаграма частки зарплат(середня) по статі'
            else: str0 = 'Діаграма частки зарплат(загальна) по статі'
            diagram_title = tk.Label(canvas, text = '%s' % str0, bg = 'light blue', font = 'Times 20')
            diagram_title.place(x = 250, y = 20)

            diagram_explain_title = tk.Label(canvas, text = 'Дані з діаграми', bg = 'light blue', font = 'Times 17')
            diagram_explain_title.place(x = 750, y = 200)
            diagram_explain = tk.Label(canvas, text = 'Чоловіки:\n\n\nЖінки:', bg = 'light blue', font = 'Times 15')
            diagram_explain.place(x = 700, y = 250)
            str1 = str(round(sum_m * 100) / 100) + ' (' + str(round(sum_m / (sum_m + sum_w) * 1000) / 10) + '%)'
            str2 = str(round(sum_w * 100) / 100) + ' (' + str(round(sum_w / (sum_m + sum_w) * 1000) / 10) + '%)'
            diagram_explain_data = tk.Label(canvas, text = (str1 + '\n\n\n' + str2), bg = 'light blue', font = 'Times 15')
            diagram_explain_data.place(x = 800, y = 250)

            if switch != 6:
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)' % counter, bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 275)
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)'% (len(data) - counter), bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 340)

            img = tk.Label(canvas, image = ready_img)
            img.image = ready_img
            img.place(x = 20, y = 60)
        
        ### Побудова кругової діаграми за освітою
        def pie_chart_by_edu(switch):
            cursor.execute('''SELECT education, salary FROM staff''')
            data = cursor.fetchall()

            sum_hm = 0
            sum_hb = 0
            sum_p = 0
            sum_m = 0
            counter_hm = 0
            counter_hb = 0
            counter_p = 0
            counter_m = 0
            for i in range(len(data)):
                if data[i][0] == 'Вища(Магістр)':
                    sum_hm += data[i][1]
                    counter_hm += 1
                elif data[i][0] == 'Вища(Бакалавр)':
                    sum_hb += data[i][1]
                    counter_hb += 1
                elif data[i][0] == 'Професійна':
                    sum_p += data[i][1]
                    counter_p += 1
                elif data[i][0] == 'Середня':
                    sum_m += data[i][1]
                    counter_m += 1

            if switch == 7:   
                sum_hm = counter_hm
                sum_hb = counter_hb
                sum_p = counter_p
                sum_m = counter_m
            elif switch - 4:
                sum_hm /= counter_hm
                sum_hb /= counter_hb
                sum_p /= counter_p
                sum_m /= counter_m

            labels = 'Вища(Магістр)', 'Вища(Бакалавр)', 'Професійна', 'Середня'
            sizes = [sum_hm, sum_hb, sum_p, sum_m]

            figure, ax = plt.subplots()
            ax.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 90)
            ax.axis('equal')
            plt.savefig('pie_chart.png')
            plt.close()

            if switch == 7: str0 = 'Діаграма кадрового складу організації по статі'
            elif switch - 4: str0 = 'Діаграма частки зарплат(середня) по освіті'
            else: str0 = 'Діаграма частки зарплат(загальна) по освіті'
            diagram_title = tk.Label(canvas, text = '%s' % str0, bg = 'light blue', font = 'Times 20')
            diagram_title.place(x = 250, y = 20)

            diagram_explain_title = tk.Label(canvas, text = 'Дані з діаграми', bg = 'light blue', font = 'Times 17')
            diagram_explain_title.place(x = 700, y = 200)
            diagram_explain = tk.Label(canvas, text = 'Вища(Магістр):\n\n\nВища(Бакалавр):\n\n\nПрофесійна:\n\n\nСередня:', bg = 'light blue', anchor = tk.W, font = 'Times 15')
            diagram_explain.place(x = 700, y = 250)
            sum_total = sum_hm + sum_hb + sum_p + sum_m
            str1 = str(round(sum_hm * 100) / 100) + ' (' + str(round(sum_hm / sum_total * 1000) / 10) + '%)'
            str2 = str(round(sum_hb * 100) / 100) + ' (' + str(round(sum_hb / sum_total * 1000) / 10) + '%)'
            str3 = str(round(sum_p * 100) / 100) + ' (' + str(round(sum_p / sum_total * 1000) / 10) + '%)'
            str4 = str(round(sum_m * 100) / 100) + ' (' + str(round(sum_m / sum_total * 1000) / 10) + '%)'
            diagram_explain_data = tk.Label(canvas, text = (str1 + '\n\n\n' + str2 + '\n\n\n' + str3 + '\n\n\n' + str4), bg = 'light blue', font = 'Times 15')
            diagram_explain_data.place(x = 850, y = 250)

            if switch != 7:
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)' % counter_hm, bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 275)
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)'% counter_hb, bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 340)
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)'% counter_p, bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 405)
                diagram_explain_addition = tk.Label(canvas, text = '(%s співробітників)'% counter_m, bg = 'light blue', anchor = tk.W, font = 'Times 15')
                diagram_explain_addition.place(x = 750, y = 470)

            load_img = Image.open('pie_chart.png')
            ready_img = ImageTk.PhotoImage(load_img)

            img = tk.Label(canvas, image = ready_img)
            img.image = ready_img
            img.place(x = 20, y = 60)

        ### Побудова графіку кількості співробітників
        def build_staff_diagram(switch):
            cursor.execute('''SELECT * FROM salary_archive''')
            data = cursor.fetchall()

            staff_by_period = []
            
            for i in range(20):
                sum = 0
                for j in range(len(data)):
                    if (data[j][i + 1] != None): sum += 1
                staff_by_period.append(sum)

            min_value = min(staff_by_period)
            max_value = max(staff_by_period)

            step = (max_value - min_value) / 10.0
            pixel_step = (max_value - min_value) / 450.0

            # Вісь X
            canvas.create_line(10, 550, 990, 550, arrow = tk.LAST, fill = 'black')
            for_year = 2016
            for i in range(20):
                canvas.create_line(99 + i * 45, 555, 99 + i * 45, 545, width = 1, fill = 'black')
                canvas.create_text(99 + i * 45, 570, text = ('%s' % for_year + '\n%s кв.' % (i % 4 + 1)), justify = tk.CENTER, font = 'Times 8')
                if i % 4 == 3: for_year += 1
        
            ### Вісь Y
            canvas.create_line(50, 590, 50, 10, arrow = tk.LAST, fill = 'black')
            for i in range(11):
                canvas.create_line(45, 500 - i * 45, 55, 500 - i * 45, fill = 'black')
                canvas.create_text(25, 500 - i * 45, text = int(min_value + step * i), justify = tk.CENTER, font = 'Times 8')
            
            # Сітка
            for i in range(20):
                    canvas.create_line(99 + i * 45, 0, 99 + i * 45, 546, fill = 'grey')
            for i in range(11):
                    canvas.create_line(55, 500 - i * 45, 1000, 500 - i * 45, fill = 'grey')

            X = []
            Y = []
            for i in range(20):
                X.append(99 + i * 45)
                Y.append(500 - (staff_by_period[i] - min_value) / pixel_step)

            for i in range(20):
                if i % 2: canvas.create_rectangle(X[i] - 22, Y[i], X[i] + 22, 550, fill = 'purple')
                else: canvas.create_rectangle(X[i] - 22, Y[i], X[i] + 22, 550, fill = 'dark blue')
                if staff_by_period[i] < (min_value + (max_value - min_value) / 2.0):
                    canvas.create_text(X[i], Y[i] - 25, text = staff_by_period[i], angle = 90, font = 'Times 15')
                else: canvas.create_text(X[i], Y[i] + 50, text = staff_by_period[i], angle = 90, font = 'Times 15')

        ### Основна частина вікна
        if switch == 0 or switch == 1: 
            coordinate_axis(switch)
            build_diagram(switch)
        elif switch == 2 or switch == 3 or switch == 6:
            pie_chart_by_sex(switch)
        elif switch == 4 or switch == 5 or switch == 7:
            pie_chart_by_edu(switch)
        elif switch == 8:
            build_staff_diagram(switch)
        
        ### Кнопки
        btn_exit = tk.Button(toolbar_diagrams, text = 'Вийти', bd = 3)
        btn_exit.pack(side = tk.RIGHT)
        btn_exit.bind('<Button-1>', lambda event: diagrams_window.destroy())

        diagrams_window.grab_set()
        diagrams_window.focus_set()
   
    ### Кнопка виклику дочірнього вікна(в залежності від запиту)
    canvas_analitics = tk.Canvas()
    label_title_analitycs1 = tk.Label(canvas_statistic, text = 'Стовпчикові діаграми', bg = 'white', font = 12)
    label_title_analitycs1.place(x = 70, y = 50)

    label_title_analitycs2 = tk.Label(canvas_statistic, text = 'Кругові діаграми', bg = 'white', font = 12)
    label_title_analitycs2.place(x = 700, y = 50)

    label_show_diagram = tk.Label(canvas_statistic, text = 'Діаграма загальної зарплати в організації', bg = 'white')
    label_show_diagram.place(x = 10, y = 103)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 250, y = 100)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(0))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Діаграма середньої зарплати в організації', bg = 'white')
    label_show_diagram.place(x = 10, y = 153)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 250, y = 150)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(1))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Діаграма к-ті співробітників в організації', bg = 'white')
    label_show_diagram.place(x = 10, y = 203)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 250, y = 200)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(8))
    
    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по статі(загальна зарплата)', bg = 'white')
    label_show_diagram.place(x = 410, y = 103)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 670, y = 100)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(2))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по статі(середня зарплата)', bg = 'white')
    label_show_diagram.place(x = 410, y = 153)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 670, y = 150)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(3))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по освіті(загальна зарплата)', bg = 'white')
    label_show_diagram.place(x = 410, y = 203)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 670, y = 200)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(4))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по освіті(середня зарплата)', bg = 'white')
    label_show_diagram.place(x = 410, y = 253)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 670, y = 250)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(5))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по статі(кількісний склад)', bg = 'white')
    label_show_diagram.place(x = 830, y = 103)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 1100, y = 100)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(6))

    label_show_diagram = tk.Label(canvas_statistic, text = 'Кругова діаграма по освіті(кількісний склад)', bg = 'white')
    label_show_diagram.place(x = 830, y = 153)
    btn_show_diagram = tk.Button(canvas_statistic, text = 'Вивести', bd = 3)
    btn_show_diagram.place(x = 1100, y = 150)
    btn_show_diagram.bind('<Button-1>', lambda event: show_diagrams_window(7))

    def to_start():
        btn_to_start_window.destroy()
        canvas_statistic.destroy()
        start_window()
    btn_to_start_window = tk.Button(toolbar, text = 'Перейти на початковий екран', bd = 3)
    btn_to_start_window.pack(side = tk.RIGHT)
    btn_to_start_window.bind('<Button-1>', lambda event: to_start())

### Пошук записів в БД
def search_db():
    main.tree.destroy()

    main.tree = ttk.Treeview(main, columns = ('id', 'name', 'birthday', 'sex', 'family status', 'education', 'salary'), height = 17, show = 'headings')
    main.tree.place(x = 0, y = 295)

    main.tree.column('id', width = 75, anchor = tk.CENTER)
    main.tree.column('name', width = 300, anchor = tk.CENTER)
    main.tree.column('birthday', width = 150, anchor = tk.CENTER)
    main.tree.column('sex', width = 75, anchor = tk.CENTER)
    main.tree.column('family status', width = 200, anchor = tk.CENTER)
    main.tree.column('education', width = 200, anchor = tk.CENTER)
    main.tree.column('salary', width = 200, anchor = tk.CENTER)

    main.tree.heading('id', text = 'ID')
    main.tree.heading('name', text = 'ПІБ')
    main.tree.heading('birthday', text = 'Дата народження')
    main.tree.heading('sex', text = 'Стать')
    main.tree.heading('family status', text = 'Сімейний статус')
    main.tree.heading('education', text = 'Освіта')
    main.tree.heading('salary', text = 'Зарплата')

    def search_records():
        id = ('%' + entry_search_id.get() + '%')
        name = ('%' + entry_search_name.get() + '%')

        if entry_search_birthday.get() == '': birthday = '%%'
        elif birth_choose.get() == 'Повністю': birthday = entry_search_birthday.get()
        elif birth_choose.get() == 'Рік': birthday = entry_search_birthday.get() + '%'
        elif birth_choose.get() == 'Місяць': birthday = '%-' + entry_search_birthday.get() + '-%'
        elif birth_choose.get() == 'День': birthday = '%-' + entry_search_birthday.get()
        else: birthday = '%%'

        if entry_search_sex.get() == 'Чоловік': sex = 'ч'
        elif entry_search_sex.get() == 'Жінка': sex = 'ж'
        else: sex = '%%'

        if entry_search_family_status.get() == '': family_status = '%%'
        else: family_status = entry_search_family_status.get()

        if entry_search_education.get() == '': education = '%%'
        else: education = entry_search_education.get()
        
        salary_true_id = []
        cursor.execute('''SELECT id, salary FROM staff''')
        pre_data = cursor.fetchall()
        data = []
        for i in range(len(pre_data)):
            if pre_data[i][1] == '': data.append((pre_data[i][0], 0))
            else: data.append(pre_data[i])
        if entry_search_salary1.get() != '':
            if for_salary.get() == 'Рівно':
                for i in range(len(data)):
                    if float(entry_search_salary1.get()) == data[i][1]: salary_true_id.append(data[i][0])
            elif for_salary.get() == 'Більше':
                for i in range(len(data)):
                    if float(entry_search_salary1.get()) < data[i][1] or float(entry_search_salary1.get()) == data[i][1]: salary_true_id.append(data[i][0])
            elif for_salary.get() == 'Менше':
                for i in range(len(data)):
                    if float(entry_search_salary1.get()) > data[i][1] or float(entry_search_salary1.get()) == data[i][1]: salary_true_id.append(data[i][0])
            elif for_salary.get() == 'В межах':
                if float(entry_search_salary1.get()) > float(entry_search_salary2.get()):
                    max = float(entry_search_salary1.get())
                    min = float(entry_search_salary2.get())
                else:
                    max = float(entry_search_salary2.get())
                    min = float(entry_search_salary1.get())
                for i in range(len(data)):
                    if max > data[i][1] or max == data[i][1]:
                        if min < data[i][1] or min == data[i][1]: salary_true_id.append(data[i][0])

        cursor.execute('''SELECT * FROM staff WHERE id LIKE ? AND name LIKE ? AND birthday LIKE ? AND sex LIKE ? AND family_status LIKE ? AND education LIKE ?''',
                       (id, name, birthday, sex, family_status, education))
        data = cursor.fetchall()
        result = []
        if entry_search_salary1.get() != '':
            for i in range(len(data)):
                for j in range(len(salary_true_id)):
                    if data[i][0] == salary_true_id[j]: result.append(data[i])
        else: result = data

        [main.tree.delete(i) for i in main.tree.get_children()]
        for i in result:
            main.tree.insert('', 'end', values = i)

    label_search1 = tk.Label(main, text = 'Введіть запит для id:', bg = 'white')
    label_search1.place(x = 75, y = 55)
    label_search2 = tk.Label(main, text = 'Введіть запит для ПІБ:', bg = 'white')
    label_search2.place(x = 70, y = 150)
    label_search3 = tk.Label(main, text = 'Введіть запит для ДН\nформат: РРРР-ММ-ДД:', bg = 'white')
    label_search3.place(x = 350, y = 40)
    label_search4 = tk.Label(main, text = 'Введіть запит для статі:', bg = 'white')
    label_search4.place(x = 350, y = 150)
    label_search5 = tk.Label(main, text = 'Введіть запит для Сім. Ст.:', bg = 'white')
    label_search5.place(x = 627, y = 55)
    label_search6 = tk.Label(main, text = 'Введіть запит для освіти:', bg = 'white')
    label_search6.place(x = 632, y = 150)
    label_search7 = tk.Label(main, text = 'Введіть запит для зарплати\n(для функції "В межах" потрібно ввести 2 значення\nВ інших - лише перше):', bg = 'white')
    label_search7.place(x = 850, y = 80)

    entry_search_id = ttk.Entry(main)
    entry_search_id.place(x = 70, y = 80)
    entry_search_name = tk.Entry(main)
    entry_search_name.place(x = 70, y = 175)
    entry_search_birthday = tk.Entry(main)
    entry_search_birthday.place(x = 354, y = 75)
    birth_choose = ttk.Combobox(main)
    birth_choose['values'] = ('День', 'Місяць', 'Рік', 'Повністю')
    birth_choose.current(2)
    birth_choose.place(x = 345, y = 105)
    entry_search_sex = ttk.Combobox(main)
    entry_search_sex['values'] = ('', 'Чоловік', 'Жінка')
    birth_choose.current(0)
    entry_search_sex.place(x = 345, y = 175)
    entry_search_family_status = ttk.Combobox(main)
    entry_search_family_status['values'] = ('', 'Одружений(-а)', 'Неодружений(-а)')
    entry_search_family_status.current(0)
    entry_search_family_status.place(x = 630, y = 80)
    entry_search_education = ttk.Combobox(main)
    entry_search_education['values'] = ('', 'Вища(Магістр)', 'Вища(Бакалавр)', 'Професійна', 'Середня')
    entry_search_education.place(x = 630, y = 175)
    for_salary = ttk.Combobox(main)
    for_salary['values'] = ('Рівно', 'Більше', 'Менше', 'В межах')
    for_salary.place(x = 920, y = 150)
    entry_search_salary1 = ttk.Entry(main)
    entry_search_salary1.place(x = 930, y = 185)
    entry_search_salary2 = ttk.Entry(main)
    entry_search_salary2.place(x = 930, y = 210)

    btn_search = tk.Button(main, text = 'Пошук', command = search_records, bd = 3)
    btn_search.place(x = 550, y = 250)

    def to_start():
        label_search1.destroy()
        label_search2.destroy()
        label_search3.destroy()
        label_search4.destroy()
        label_search5.destroy()
        label_search6.destroy()
        label_search7.destroy()
        entry_search_id.destroy()
        entry_search_name.destroy()
        entry_search_birthday.destroy()
        birth_choose.destroy()
        entry_search_sex.destroy()
        entry_search_family_status.destroy()
        entry_search_education.destroy()
        for_salary.destroy()
        entry_search_salary1.destroy()
        entry_search_salary2.destroy()
        btn_search.destroy()
        btn_to_start_window.destroy()
        start_window()
    btn_to_start_window = tk.Button(toolbar, text = 'Перейти на початковий екран', bd = 3)
    btn_to_start_window.pack(side = tk.RIGHT)
    btn_to_start_window.bind('<Button-1>', lambda event: to_start())

### Перегляд бази данних
def view_db():
    canvas_view_db = tk.Canvas(toolbar, width = 1020, height = 25, bg = 'light grey')
    canvas_view_db.place(x = 0, y = 0)
    staff_view()

    btn_show_staff = tk.Button(canvas_view_db, command = staff_view, text = 'Співробітники', bd = 3)
    btn_show_staff.pack(side = tk.LEFT)

    btn_show_archive = tk.Button(canvas_view_db, command = salary_archive_view, text = 'Архів зарплат', bd = 3)
    btn_show_archive.pack(side = tk.LEFT)

    btn_show_archive = tk.Button(canvas_view_db, command = positions_view, text = 'Посади', bd = 3)
    btn_show_archive.pack(side = tk.LEFT)

    btn_delete = tk.Button(canvas_view_db, command = add_record, text = 'Додати запис', bd = 3)
    btn_delete.pack(side = tk.LEFT)

    btn_update = tk.Button(canvas_view_db, command = update_record, text = 'Змінити запис', bd = 3)
    btn_update.pack(side = tk.LEFT)

    btn_delete = tk.Button(canvas_view_db, command = delete_record, text = 'Видалити запис', bd = 3)
    btn_delete.pack(side = tk.LEFT)

    btn_set_position = tk.Button(canvas_view_db, command = set_position, text = 'Ввести посаду', bd = 3)
    btn_set_position.pack(side = tk.LEFT)

    def to_start():
        btn_to_start_window.destroy()
        canvas_view_db.destroy()
        start_window()
    btn_to_start_window = tk.Button(toolbar, text = 'Перейти на початковий екран', bd = 3)
    btn_to_start_window.pack(side = tk.RIGHT)
    btn_to_start_window.bind('<Button-1>', lambda event: to_start())

### Розширений перегляд бази даних
def expanded_view_db(id, name, birthday, sex, family_status, education, salary, department, position):
    main.tree.destroy()

    result = []
    head = []
    if id:
        cursor.execute('''SELECT id FROM staff''')
        data = cursor.fetchall()
        head.append(['id', 'ID'])
        result.append(data)
    if name:
        cursor.execute('''SELECT name FROM staff''')
        data = cursor.fetchall()
        head.append(['name', 'ПІБ'])
        result.append(data)
    if birthday:
        cursor.execute('''SELECT birthday FROM staff''')
        data = cursor.fetchall()
        head.append(['birthday', 'Дата народження'])
        result.append(data)
    if sex:
        cursor.execute('''SELECT sex FROM staff''')
        data = cursor.fetchall()
        head.append(['sex', 'Стать'])
        result.append(data)
    if family_status:
        cursor.execute('''SELECT family_status FROM staff''')
        data = cursor.fetchall()
        head.append(['family_status', 'Сімейний статус'])
        result.append(data)
    if education:
        cursor.execute('''SELECT education FROM staff''')
        data = cursor.fetchall()
        head.append(['education', 'Освіта'])
        result.append(data)
    if salary:
        cursor.execute('''SELECT salary FROM staff''')
        data = cursor.fetchall()
        head.append(['salary', 'Зарплата'])
        result.append(data)
    if department:
        cursor.execute('''SELECT department_name FROM positions''')
        data = cursor.fetchall()
        head.append(['department', 'Відділ'])
        result.append(data)
    if position:
        cursor.execute('''SELECT position FROM positions''')
        data = cursor.fetchall()
        head.append(['position', 'Посада'])
        result.append(data)

    main.tree = ttk.Treeview(main, height = 32, show = 'headings')
    main.tree['columns'] = [head[i][0] for i in range(len(head))]

    for i in range(len(head)):
        main.tree.column(head[i][0], width = round(1200 / len(head)), anchor = tk.CENTER)
        main.tree.heading(head[i][0], text = head[i][1])

    result_t = [*zip(*result)]

    for i in result_t:
        main.tree.insert('', 'end', values = i)

    main.tree.pack()

    ### Недопустити зміну ширини стовпців
    def handle_click(event):
        if main.tree.identify_region(event.x, event.y) == "separator":
            return 'break'
    main.tree.bind('<Button-1>', handle_click)

    def to_start():
        btn_to_start_window.destroy()
        start_window()
    btn_to_start_window = tk.Button(toolbar, text = 'Перейти на початковий екран', bd = 3)
    btn_to_start_window.pack(side = tk.RIGHT)
    btn_to_start_window.bind('<Button-1>', lambda event: to_start())

### Початкове вікно
def start_window():
    canvas_start = tk.Canvas(root, width = 1200, height = 700, bg = 'light grey')
    canvas_start.place(x = 0, y = 0)

    def next(switch):
        canvas_start.destroy()
        if switch == 0: view_db()
        elif switch == 1:
            if ch_id.get() or ch_name.get() or ch_birthday.get() or ch_sex.get() or ch_family_status.get() or ch_education.get() or ch_salary.get() or ch_department.get() or ch_position.get():
                expanded_view_db(ch_id.get(), ch_name.get(), ch_birthday.get(), ch_sex.get(), ch_family_status.get(), ch_education.get(), ch_salary.get(), ch_department.get(), ch_position.get())
            else:
                start_window()
        elif switch == 2: statistic()
        elif switch == 3: search_db()

    pixel_image = tk.PhotoImage(width = 1, height = 1)

    checkbutton_label = tk.Label(canvas_start, text = 'Обрати атрибути для виведення в таблиці:', bg = 'light grey')
    checkbutton_label.place(x = 760, y = 190)
    ch_id = tk.BooleanVar()
    ch_name = tk.BooleanVar()
    ch_birthday = tk.BooleanVar()
    ch_sex = tk.BooleanVar()
    ch_family_status = tk.BooleanVar()
    ch_education = tk.BooleanVar()
    ch_salary = tk.BooleanVar()
    ch_department = tk.BooleanVar()
    ch_position = tk.BooleanVar()
    checkbutton_id = tk.Checkbutton(canvas_start, text = 'ID', variable = ch_id, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_name = tk.Checkbutton(canvas_start, text = 'ПІБ', variable = ch_name, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_birthday = tk.Checkbutton(canvas_start, text = 'Дата народження', variable = ch_birthday, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_sex = tk.Checkbutton(canvas_start, text = 'Стать', variable = ch_sex, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_family_status = tk.Checkbutton(canvas_start, text = 'Сімейний статус', variable = ch_family_status, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_education = tk.Checkbutton(canvas_start, text = 'Освіта', variable = ch_education, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_salary = tk.Checkbutton(canvas_start, text = 'Зарплата', variable = ch_salary, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_department = tk.Checkbutton(canvas_start, text = 'Відділ', variable = ch_department, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_position = tk.Checkbutton(canvas_start, text = 'Посада', variable = ch_position, onvalue = 1, offvalue = 0, bg = 'light grey')
    checkbutton_id.place(x = 800, y = 250)
    checkbutton_name.place(x = 800, y = 275)
    checkbutton_birthday.place(x = 800, y = 300)
    checkbutton_sex.place(x = 800, y = 325)
    checkbutton_family_status.place(x = 800, y = 350)
    checkbutton_education.place(x = 800, y = 375)
    checkbutton_salary.place(x = 800, y = 400)
    checkbutton_department.place(x = 800, y = 425)
    checkbutton_position.place(x = 800, y = 450)

    btn_view_db = tk.Button(canvas_start, text = 'Переглянути/редагувати базу даних', image = pixel_image, width = 300, height = 50, compound = 'c')
    btn_view_db.place(x = 100, y = 100)
    btn_view_db.bind('<Button-1>', lambda event: next(0))

    btn_view_db_expanded = tk.Button(canvas_start, text = 'Переглянути базу даних за запитом', image = pixel_image, width = 300, height = 50, compound = 'c')
    btn_view_db_expanded.place(x = 700, y = 500)
    btn_view_db_expanded.bind('<Button-1>', lambda event: next(1))

    btn_stat = tk.Button(canvas_start, text = 'Переглянути статистику бази даних', image = pixel_image, width = 300, height = 50, compound = 'c')
    btn_stat.place(x = 100, y = 300)
    btn_stat.bind('<Button-1>', lambda event: next(2))

    btn_search_bd = tk.Button(canvas_start, text = 'Пошук в базі даних', image = pixel_image, width = 300, height = 50, compound = 'c')
    btn_search_bd.place(x = 100, y = 500)
    btn_search_bd.bind('<Button-1>', lambda event: next(3))

### Підключення БД, попереднє створення таблиці tree та виведення сутності "Співробітники"
db = sqlite3.connect('OrgStaff.db')
cursor = db.cursor()
main.tree = ttk.Treeview(main, height = 32)
main.tree.column('#0', width = 1300)
main.tree.pack()

start_window()

root.mainloop()