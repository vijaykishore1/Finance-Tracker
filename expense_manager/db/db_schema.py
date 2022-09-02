import sqlite3


class DatabaseConnection:
    def __init__(
        self,
    ):
        self.con = None
        self.connect_connection()
        self.create_table_expenses_categories()
        self.create_table_investments_categories()
        self.create_table_income_categories()
        self.create_table_investments()
        self.create_table_expenses()
        self.create_table_income()
        self.create_table_user()
        self.create_table_login()
        self.create_table_bank_account()

    def connect_connection(
        self,
    ):
        self.con = sqlite3.connect(database="ExpenseManager.db")

    def run_query(
        self,
        input_str,
    ):
        print(
            "Executing input_str:",
            input_str,
        )
        cur = self.con.cursor()
        cur.execute(input_str)
        self.con.commit()
        return cur

    def create_table_user(
        self,
        # table_name,
    ):
        query = (
            f"Create table user ("
            "id integer primary key autoincrement,"
            "name TEXT not null,"
            "phone_number TEXT not null"
            # "primary key (id)"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_login(
        self,
        # table_name,
    ):
        query = (
            f"Create table login ("
            # "id INT primary key not null,"
            "login_id integer primary key autoincrement,"
            "username TEXT not null,"
            "password TEXT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_bank_account(
        self,
        # table_name,
    ):
        query = (
            f"Create table bank_account ("
            "bank_id integer primary key autoincrement,"
            "id INT not null,"
            "bank_name TEXT not null,"
            "amount INT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_expenses_categories(
        self,
        # table_name,
    ):
        query = (
            f"Create table expenses_categories ("
            "expenses_category_id integer primary key autoincrement,"
            "expenses_category TEXT not null,"
            "expenses_sub_category TEXT,"
            "count INT default 0"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_investments_categories(
        self,
        # table_name,
    ):
        query = (
            f"Create table investments_categories ("
            "investments_category_id integer primary key autoincrement,"
            "investments_category TEXT not null,"
            "investments_sub_category TEXT,"
            "count INT default 0"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_income_categories(
        self,
        # table_name,
    ):
        query = (
            f"Create table income_categories ("
            "income_category_id integer primary key autoincrement,"
            "income_category TEXT not null,"
            "income_sub_category TEXT,"
            "count INT default 0"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_income(self):
        query = (
            f"Create table income ("
            "income_id integer primary key autoincrement,"
            "bank_name TEXT not null,"
            "id INT not null,"
            "income_category_id INT not null,"
            "amount INT not null,"
            "date date not null,"
            "description TEXT"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_expenses(self):
        query = (
            f"Create table expenses ("
            "expenses_id integer primary key autoincrement,"
            "bank_name TEXT not null,"
            "id INT not null,"
            "expenses_category_id INT not null,"
            "amount INT not null,"
            "date date not null,"
            "description TEXT"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_investments(self):
        query = (
            f"Create table investments ("
            "investments_id integer primary key autoincrement,"
            "bank_name TEXT not null,"
            "id INT not null,"
            "investments_category_id INT not null,"
            "amount INT not null,"
            "date date not null,"
            "description TEXT"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")


if __name__ == "__main__":
    conn_obj = DatabaseConnection()
