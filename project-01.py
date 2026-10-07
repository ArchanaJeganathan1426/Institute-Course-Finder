import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def connect_db():
    return mysql.connector.connect(host="localhost",user="root",password="pass123",database="institute_course_finder")

root = tk.Tk()
root.title("Institute & Course Finder")
root.geometry("1150x720")
root.resizable(False, False)

BG = "#EAF2F8"
WHITE = "#FFFFFF"
NAVY = "#1F4E78"
BLUE = "#2E75B6"
DARK = "#1F2937"
LIGHT = "#F8FAFC"
BORDER = "#B8CCE4"
SELECT = "#D6EAF8"
GREEN = "#287A4B"
RED = "#B42318"

root.configure(bg=BG)


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def title_label(text):
    return tk.Label(root,text=text,font=("Segoe UI", 24, "bold"),bg=BG,fg=NAVY)
def styled_button(parent, text, command, color=BLUE):
    return tk.Button( parent, text=text,command=command,font=("Segoe UI", 11, "bold"),bg=color,fg="white",activebackground=color,activeforeground="white",relief="flat",
cursor="hand2",padx=18,pady=8)

def home_page():

    clear_window()

    frame = tk.Frame(root, bg=BG)
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text="INSTITUTE & COURSE FINDER",
        font=("Segoe UI", 28, "bold"),
        bg=BG,
        fg=NAVY
    ).pack(pady=(100, 10))

    tk.Label(
        frame,
        text="Find and compare courses across institutes",
        font=("Segoe UI", 14),
        bg=BG,
        fg=DARK
    ).pack(pady=5)

    button_frame = tk.Frame(frame, bg=BG)
    button_frame.pack(pady=60)

    styled_button(
        button_frame,
        "User Search",
        user_page
    ).grid(row=0, column=0, padx=20)

    styled_button(
        button_frame,
        "Admin Login",
        admin_login,
        NAVY
    ).grid(row=0, column=1, padx=20)

    tk.Label(
        frame,
        text="Python • Tkinter • MySQL",
        font=("Segoe UI", 10),
        bg=BG,
        fg="#64748B"
    ).pack(side="bottom", pady=30)


def user_page():

    clear_window()

    title_label("Course Search").pack(pady=25)

    form = tk.Frame(root, bg=WHITE, bd=1, relief="solid")
    form.pack(padx=100, pady=10, fill="x")

    labels = [
        "Name",
        "Age",
        "Experience Status",
        "Interested Course",
        "Preferred Location"
    ]

    for i, text in enumerate(labels):
        tk.Label(
            form,
            text=text,
            font=("Segoe UI", 11, "bold"),
            bg=WHITE,
            fg=DARK
        ).grid(row=i, column=0, padx=25, pady=12, sticky="w")

    name_entry = ttk.Entry(form, width=40)
    name_entry.grid(row=0, column=1, padx=25, pady=12)

    age_entry = ttk.Entry(form, width=40)
    age_entry.grid(row=1, column=1, padx=25, pady=12)

    status_combo = ttk.Combobox(
        form,
        values=["Fresher", "Experienced"],
        state="readonly",
        width=37
    )
    status_combo.set("Fresher")
    status_combo.grid(row=2, column=1, padx=25, pady=12)

    course_combo = ttk.Combobox(
        form,
        values=[
            "All",
            "Data Analytics",
            "Data Science",
            "Python",
            "Python Full Stack",
            "Java Full Stack",
            "SQL",
            "Software Testing"
        ],
        state="readonly",
        width=37
    )
    course_combo.set("All")
    course_combo.grid(row=3, column=1, padx=25, pady=12)

    location_combo = ttk.Combobox(
        form,
        values=["Chennai"],
        state="readonly",
        width=37
    )
    location_combo.set("Chennai")
    location_combo.grid(row=4, column=1, padx=25, pady=12)

    def save_and_search():

        name = name_entry.get().strip()
        age = age_entry.get().strip()
        status = status_combo.get()
        course = course_combo.get()
        location = location_combo.get()

        if not name or not age:
            messagebox.showwarning(
                "Missing Information",
                "Please enter your name and age."
            )
            return

        try:
            age = int(age)

            if age <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Age",
                "Please enter a valid age."
            )
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO users
                (name, age, experience_status, interested_course, preferred_location)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (name, age, status, course, location)
            )

            conn.commit()
            cursor.close()
            conn.close()

            results_page(course, location)

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    button_frame = tk.Frame(root, bg=BG)
    button_frame.pack(pady=25)

    styled_button(
        button_frame,
        "Search Courses",
        save_and_search
    ).grid(row=0, column=0, padx=10)

    styled_button(
        button_frame,
        "Back",
        home_page,
        NAVY
    ).grid(row=0, column=1, padx=10)


def results_page(selected_course="All", location="Chennai"):

    clear_window()

    title_label("Available Courses").pack(pady=15)

    filter_frame = tk.Frame(root, bg=WHITE, bd=1, relief="solid")
    filter_frame.pack(fill="x", padx=30, pady=5)
    
    tk.Label(filter_frame,text="Course:",bg=WHITE,fg=DARK,font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)

    course_filter = ttk.Combobox( filter_frame,values=["All","Data Analytics","Data Science","Python","Python Full Stack","Java Full Stack""SQL","Software Testing"],state="readonly",width=20)
    course_filter.set(selected_course)
    course_filter.grid(row=0, column=1, padx=5)

    tk.Label(filter_frame,text="Institute:",bg=WHITE,fg=DARK,font=("Segoe UI", 10, "bold")).grid(row=0, column=2, padx=10)
    institute_entry = ttk.Entry(filter_frame,width=22)
    institute_entry.grid(row=0, column=3, padx=5)

    tk.Label(filter_frame,text="Min Fee:",bg=WHITE,fg=DARK,font=("Segoe UI", 10, "bold")).grid(row=0, column=4, padx=10)
    min_fee = ttk.Entry(filter_frame,width=10)
    min_fee.grid(row=0, column=5)

    tk.Label(filter_frame,text="Max Fee:",bg=WHITE,fg=DARK,font=("Segoe UI", 10, "bold")).grid(row=0, column=6, padx=10)

    max_fee = ttk.Entry(filter_frame,width=10)
    max_fee.grid(row=0, column=7)

    tk.Label(filter_frame,text="Sort:",bg=WHITE,fg=DARK,font=("Segoe UI", 10, "bold")).grid(row=1, column=0, padx=10, pady=10)
    sort_combo = ttk.Combobox( filter_frame,values=["Default","Fees: Low to High","Fees: High to Low","Duration"],state="readonly",width=20)
    sort_combo.set("Default")
    sort_combo.grid(row=1, column=1)


    table_frame = tk.Frame(root, bg=BG)
    table_frame.pack(fill="both", expand=True, padx=30, pady=15)

    columns = (
        "ID",
        "Institute",
        "Course",
        "Duration",
        "Fees",
        "Mode",
        "Location"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=15
    )

    widths = {
        "ID": 50,
        "Institute": 180,
        "Course": 170,
        "Duration": 100,
        "Fees": 100,
        "Mode": 90,
        "Location": 100
    }

    for col in columns:
        tree.heading(col, text=col)
        tree.column(
            col,
            width=widths[col],
            anchor="center"
        )

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    def load_data():

        for item in tree.get_children():
            tree.delete(item)

        course = course_filter.get()
        institute = institute_entry.get().strip()
        minimum = min_fee.get().strip()
        maximum = max_fee.get().strip()
        sort_value = sort_combo.get()

        query = """
            SELECT
                c.course_id,
                i.institute_name,
                c.course_name,
                c.duration,
                c.fees,
                c.mode,
                i.location
            FROM courses c
            JOIN institutes i
            ON c.institute_id = i.institute_id
            WHERE i.location = %s
        """

        params = [location]

        if course != "All":
            query += " AND c.course_name = %s"
            params.append(course)

        if institute:
            query += " AND i.institute_name LIKE %s"
            params.append("%" + institute + "%")

        if minimum:
            try:
                float(minimum)
            except ValueError:
                messagebox.showerror(
                    "Invalid Fee",
                    "Minimum fee must be a number."
                )
                return

            query += " AND c.fees >= %s"
            params.append(float(minimum))

        if maximum:
            try:
                float(maximum)
            except ValueError:
                messagebox.showerror(
                    "Invalid Fee",
                    "Maximum fee must be a number."
                )
                return

            query += " AND c.fees <= %s"
            params.append(float(maximum))

        if sort_value == "Fees: Low to High":
            query += " ORDER BY c.fees ASC"

        elif sort_value == "Fees: High to Low":
            query += " ORDER BY c.fees DESC"

        elif sort_value == "Duration":
            query += """
                ORDER BY CAST(
                    SUBSTRING_INDEX(c.duration, ' ', 1)
                    AS UNSIGNED
                ) ASC
            """

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(query, tuple(params))

            rows = cursor.fetchall()

            cursor.close()
            conn.close()

            for row in rows:
                tree.insert(
                    "",
                    "end",
                    values=row
                )

            if not rows:
                messagebox.showinfo(
                    "No Results",
                    "No matching courses found."
                )

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    styled_button(
        filter_frame,
        "Apply Filters",
        load_data,
        BLUE
    ).grid(row=1, column=3, padx=10)


    def show_details():

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                "Select Course",
                "Please select a course."
            )
            return

        values = tree.item(
            selected[0],
            "values"
        )

        institute_name = values[1]

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    institute_name,
                    location,
                    address,
                    phone,
                    website,
                    description
                FROM institutes
                WHERE institute_name = %s
                """,
                (institute_name,)
            )

            data = cursor.fetchone()

            cursor.close()
            conn.close()

            if data:

                details = (
                    f"Institute: {data[0]}\n\n"
                    f"Location: {data[1]}\n"
                    f"Address: {data[2]}\n"
                    f"Phone: {data[3]}\n"
                    f"Website: {data[4]}\n\n"
                    f"Description:\n{data[5]}"
                )

                messagebox.showinfo(
                    "Institute Details",
                    details
                )

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def recommend_course():

        course = course_filter.get()

        try:
            conn = connect_db()
            cursor = conn.cursor()

            if course == "All":

                cursor.execute(
                    """
                    SELECT
                        i.institute_name,
                        c.course_name,
                        c.duration,
                        c.fees
                    FROM courses c
                    JOIN institutes i
                    ON c.institute_id = i.institute_id
                    WHERE i.location = %s
                    ORDER BY c.fees ASC
                    LIMIT 3
                    """,
                    (location,)
                )

            else:

                cursor.execute(
                    """
                    SELECT
                        i.institute_name,
                        c.course_name,
                        c.duration,
                        c.fees
                    FROM courses c
                    JOIN institutes i
                    ON c.institute_id = i.institute_id
                    WHERE i.location = %s
                    AND c.course_name = %s
                    ORDER BY c.fees ASC
                    LIMIT 3
                    """,
                    (location, course)
                )

            rows = cursor.fetchall()

            cursor.close()
            conn.close()

            if not rows:
                messagebox.showinfo(
                    "Recommendation",
                    "No recommendation available."
                )
                return

            text = "Recommended Courses\n\n"

            for index, row in enumerate(rows, start=1):

                text += (
                    f"{index}. {row[0]}\n"
                    f"   Course: {row[1]}\n"
                    f"   Duration: {row[2]}\n"
                    f"   Fees: ₹{row[3]:,.0f}\n\n"
                )

            messagebox.showinfo(
                "Course Recommendation",
                text
            )

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    button_frame = tk.Frame(root, bg=BG)
    button_frame.pack(pady=10)

    styled_button(
        button_frame,
        "Institute Details",
        show_details
    ).grid(row=0, column=0, padx=8)

    styled_button(
        button_frame,
        "Recommend Course",
        recommend_course,
        GREEN
    ).grid(row=0, column=1, padx=8)

    styled_button(
        button_frame,
        "Back",
        user_page,
        NAVY
    ).grid(row=0, column=2, padx=8)

    load_data()


def admin_login():

    clear_window()

    title_label("Admin Login").pack(pady=50)

    login_frame = tk.Frame(
        root,
        bg=WHITE,
        bd=1,
        relief="solid"
    )

    login_frame.pack(
        padx=350,
        pady=10,
        fill="x"
    )

    tk.Label(
        login_frame,
        text="Username",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )

    username = ttk.Entry(
        login_frame,
        width=30
    )

    username.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
    )

    tk.Label(
        login_frame,
        text="Password",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=DARK
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=20
    )

    password = ttk.Entry(
        login_frame,
        width=30,
        show="*"
    )

    password.grid(
        row=1,
        column=1,
        padx=20,
        pady=20
    )

    def login():

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT admin_id
                FROM admins
                WHERE username = %s
                AND password = %s
                """,
                (
                    username.get(),
                    password.get()
                )
            )

            result = cursor.fetchone()

            cursor.close()
            conn.close()

            if result:
                admin_dashboard()
            else:
                messagebox.showerror(
                    "Login Failed",
                    "Invalid username or password."
                )

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    button_frame = tk.Frame(root, bg=BG)
    button_frame.pack(pady=30)

    styled_button(
        button_frame,
        "Login",
        login
    ).grid(row=0, column=0, padx=10)

    styled_button(
        button_frame,
        "Back",
        home_page,
        NAVY
    ).grid(row=0, column=1, padx=10)


def admin_dashboard():

    clear_window()

    title_label("Admin Dashboard").pack(pady=15)

    notebook = ttk.Notebook(root)
    notebook.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=10
    )

    institute_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    course_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    user_tab = tk.Frame(
        notebook,
        bg=WHITE
    )

    notebook.add(
        institute_tab,
        text="Institutes"
    )

    notebook.add(
        course_tab,
        text="Courses"
    )

    notebook.add(
        user_tab,
        text="Users"
    )


    institute_tree = ttk.Treeview(
        institute_tab,
        columns=(
            "ID",
            "Name",
            "Location",
            "Address",
            "Phone"
        ),
        show="headings",
        height=14
    )

    for col, width in [
        ("ID", 50),
        ("Name", 180),
        ("Location", 100),
        ("Address", 250),
        ("Phone", 130)
    ]:
        institute_tree.heading(
            col,
            text=col
        )
        institute_tree.column(
            col,
            width=width,
            anchor="center"
        )

    institute_tree.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    def load_institutes():

        for item in institute_tree.get_children():
            institute_tree.delete(item)

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    institute_id,
                    institute_name,
                    location,
                    address,
                    phone
                FROM institutes
                ORDER BY institute_id
                """
            )

            for row in cursor.fetchall():
                institute_tree.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def add_institute():

        popup = tk.Toplevel(root)
        popup.title("Add Institute")
        popup.geometry("450x400")
        popup.resizable(False, False)
        popup.configure(bg=BG)

        fields = [
            "Institute Name",
            "Location",
            "Address",
            "Phone",
            "Website",
            "Description"
        ]

        entries = {}

        for i, field in enumerate(fields):

            tk.Label(
                popup,
                text=field,
                bg=BG,
                fg=DARK,
                font=("Segoe UI", 10, "bold")
            ).grid(
                row=i,
                column=0,
                padx=15,
                pady=10,
                sticky="w"
            )

            entry = ttk.Entry(
                popup,
                width=35
            )

            entry.grid(
                row=i,
                column=1,
                padx=15,
                pady=10
            )

            entries[field] = entry

        def save():

            values = [
                entries[field].get().strip()
                for field in fields
            ]

            if not values[0] or not values[1]:
                messagebox.showwarning(
                    "Required",
                    "Institute name and location are required."
                )
                return

            try:
                conn = connect_db()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO institutes
                    (
                        institute_name,
                        location,
                        address,
                        phone,
                        website,
                        description
                    )
                    VALUES (%s,%s,%s,%s,%s,%s)
                    """,
                    tuple(values)
                )

                conn.commit()

                cursor.close()
                conn.close()

                popup.destroy()
                load_institutes()

                messagebox.showinfo(
                    "Success",
                    "Institute added successfully."
                )

            except mysql.connector.Error as e:
                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

        styled_button(
            popup,
            "Save Institute",
            save,
            GREEN
        ).grid(
            row=len(fields),
            column=0,
            columnspan=2,
            pady=20
        )

    def delete_institute():

        selected = institute_tree.selection()

        if not selected:
            messagebox.showwarning(
                "Select Institute",
                "Please select an institute."
            )
            return

        values = institute_tree.item(
            selected[0],
            "values"
        )

        institute_id = values[0]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete this institute and its courses?"
        )

        if not confirm:
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM institutes WHERE institute_id = %s",
                (institute_id,)
            )

            conn.commit()

            cursor.close()
            conn.close()

            load_institutes()

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    institute_buttons = tk.Frame(
        institute_tab,
        bg=WHITE
    )

    institute_buttons.pack(pady=10)

    styled_button(
        institute_buttons,
        "Add Institute",
        add_institute,
        GREEN
    ).grid(row=0, column=0, padx=10)

    styled_button(
        institute_buttons,
        "Delete Institute",
        delete_institute,
        RED
    ).grid(row=0, column=1, padx=10)

    load_institutes()


    course_tree = ttk.Treeview(
        course_tab,
        columns=(
            "ID",
            "Institute",
            "Course",
            "Duration",
            "Fees",
            "Mode"
        ),
        show="headings",
        height=14
    )

    for col, width in [
        ("ID", 50),
        ("Institute", 180),
        ("Course", 180),
        ("Duration", 100),
        ("Fees", 100),
        ("Mode", 100)
    ]:
        course_tree.heading(
            col,
            text=col
        )
        course_tree.column(
            col,
            width=width,
            anchor="center"
        )

    course_tree.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    def load_courses():

        for item in course_tree.get_children():
            course_tree.delete(item)

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    c.course_id,
                    i.institute_name,
                    c.course_name,
                    c.duration,
                    c.fees,
                    c.mode
                FROM courses c
                JOIN institutes i
                ON c.institute_id = i.institute_id
                ORDER BY c.course_id
                """
            )

            for row in cursor.fetchall():
                course_tree.insert(
                    "",
                    "end",
                    values=row
                )

            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def add_course():

        popup = tk.Toplevel(root)
        popup.title("Add Course")
        popup.geometry("450x420")
        popup.resizable(False, False)
        popup.configure(bg=BG)

        tk.Label(
            popup,
            text="Institute",
            bg=BG,
            fg=DARK,
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=12
        )

        institute_combo = ttk.Combobox(
            popup,
            state="readonly",
            width=32
        )

        institute_combo.grid(
            row=0,
            column=1,
            padx=15,
            pady=12
        )

        institute_ids = {}

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT institute_id, institute_name
                FROM institutes
                ORDER BY institute_name
                """
            )

            institute_rows = cursor.fetchall()

            for row in institute_rows:
                institute_ids[row[1]] = row[0]

            institute_combo["values"] = [
                row[1]
                for row in institute_rows
            ]

            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

        fields = [
            "Course Name",
            "Duration",
            "Fees",
            "Mode",
            "Description"
        ]

        entries = {}

        for i, field in enumerate(fields, start=1):

            tk.Label(popup,
                text=field,
                bg=BG,
                fg=DARK,
                font=("Segoe UI", 10, "bold")
            ).grid(
                row=i,
                column=0,
                padx=15,
                pady=10,
                sticky="w"
            )

            entry = ttk.Entry(
                popup,
                width=35
            )

            entry.grid(
                row=i,
                column=1,
                padx=15,
                pady=10
            )

            entries[field] = entry

        def save():

            institute_name = institute_combo.get()

            values = {
                field: entries[field].get().strip()
                for field in fields
            }

            if not institute_name:
                messagebox.showwarning(
                    "Required",
                    "Please select an institute."
                )
                return

            if not values["Course Name"]:
                messagebox.showwarning(
                    "Required",
                    "Course name is required."
                )
                return

            try:
                fees = float(values["Fees"])
            except ValueError:
                messagebox.showerror(
                    "Invalid Fees",
                    "Please enter a valid fee amount."
                )
                return

            try:
                conn = connect_db()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO courses
                    (
                        institute_id,
                        course_name,
                        duration,
                        fees,
                        mode,
                        description
                    )
                    VALUES (%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        institute_ids[institute_name],
                        values["Course Name"],
                        values["Duration"],
                        fees,
                        values["Mode"],
                        values["Description"]
                    )
                )

                conn.commit()

                cursor.close()
                conn.close()

                popup.destroy()
                load_courses()

                messagebox.showinfo(
                    "Success",
                    "Course added successfully."
                )

            except mysql.connector.Error as e:
                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

        styled_button(
            popup,
            "Save Course",
            save,
            GREEN
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20
        )

    def delete_course():

        selected = course_tree.selection()

        if not selected:
            messagebox.showwarning( "Select Course", "Please select a course." )
            return

        values = course_tree.item(selected[0], "values" )

        course_id = values[0]

        if not messagebox.askyesno("Confirm Delete","Delete this course?"):
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM courses WHERE course_id = %s",(course_id,))
            conn.commit()
            cursor.close()
            conn.close()
            load_courses()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error",str(e))

    course_buttons = tk.Frame(course_tab, bg=WHITE)

    course_buttons.pack(pady=10)

    styled_button(course_buttons,"Add Course", add_course,GREEN ).grid(row=0, column=0, padx=10)

    styled_button(course_buttons,"Delete Course",delete_course,RED).grid(row=0, column=1, padx=10)load_courses()


    user_tree = ttk.Treeview(user_tab,columns=("ID","Name","Age","Status","Course","Location"),show="headings", height=14 )

    for col, width in [("ID", 50),("Name", 160),("Age", 70),("Status", 120),("Course", 180),("Location", 120)]:
        user_tree.heading(col,text=col)
        user_tree.column(col,width=width,anchor="center")

    user_tree.pack( fill="both",expand=True,padx=15,pady=15)

    def load_users():

        for item in user_tree.get_children():
            user_tree.delete(item)

        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute( """ SELECT user_id,name,age,experience_status,interested_course, preferred_location FROM users ORDER BY user_id DESC """)
        for row in cursor.fetchall():
          user_tree.insert( "","end",values=row)
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
           messagebox.showerror("Database Error",str(e))

    def delete_user():

        selected = user_tree.selection()

        if not selected:
            messagebox.showwarning("Select User","Please select a user.")
            return
       values = user_tree.item(selected[0],"values")
       user_id = values[0]
       if not messagebox.askyesno("Confirm Delete","Delete this user record?"):
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = %s",(user_id,))
            conn.commit()
            cursor.close()
            conn.close()
            load_users()
except mysql.connector.Error as e:messagebox.showerror("Database Error", str(e))
user_buttons = tk.Frame(user_tab, bg=WHITE)
user_buttons.pack(pady=10)
styled_button(user_buttons,"Delete User",delete_user,RED).grid(row=0, column=0, padx=10)load_users()styled_button(root,"Logout", home_page,NAVY).pack(pady=8)
home_page()
root.mainloop()
