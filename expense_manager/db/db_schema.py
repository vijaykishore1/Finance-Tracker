import sqlite3

class DatabaseConnection:
    def __init__(
        self,
    ):
        self.con = None
        self.connect_connection()
        self.create_table_user()
        self.create_table_login()
        self.create_table_bank_account()
        self.create_table_category()
        self.create_table_income()
        self.create_table_expenses()
        self.create_table_investments()
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
            "id INT primary key not null,"
            "name TEXT not null,"
            "phone_number TEXT not null"
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
            "username TEXT primary key not null,"
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
            "bank_id INT primary key not null,"
            "id INT not null,"
            "bank_name TEXT not null,"
            "amount INT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_category(
            self,
            # table_name,
    ):
        query = (
            f"Create table category ("
            "category_id INT primary key not null,"
            "id INT not null,"
            "category TEXT not null,"
            "sub_category TEXT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_income(
            self,
            # table_name,
    ):
        query = (
            f"Create table income ("
            "income_id INT primary key not null,"
            "bank_id INT not null,"
            "id INT not null,"
            "source TEXT not null,"
            "amount INT not null,"
            "date datetime,"
            "description TEXT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

    def create_table_expenses(
            self,
            # table_name,
    ):
        query = (
            f"Create table expenses ("
            "expense_id INT primary key not null,"
            "bank_id INT not null,"
            "id INT not null,"
            "category_id INT not null,"
            "amount INT not null,"
            "date datetime,"
            "description TEXT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")


    def create_table_investments(
            self,
            # table_name,
    ):
        query = (
            f"Create table investments ("
            "investment_id INT primary key not null,"
            "id INT not null,"
            "type TEXT not null,"
            "amount INT not null,"
            "date datetime,"
            "description TEXT not null"
            ");"
        )
        self.run_query(input_str=query)
        print("Table created successfully")

if __name__ == "__main__":
    conn_obj = DatabaseConnection()