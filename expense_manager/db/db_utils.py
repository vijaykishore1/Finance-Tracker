import sqlite3

class DbUtils:
    def __init__(
        self,
    ):
        self.con = None
        self.connect_connection()

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

    def insert_into_table(
        self,
        table_name,
        values,
    ):
        query = f"insert into {table_name} values ({values})"
        self.run_query(input_str=query)
        print("Record inserted successfully")

    def update_in_table_interactive(
        self,
        table_name,
    ):
        no_of_updates = int(input("how many values do you want to update"))
        list_column = []
        list_value = []
        for i in range(no_of_updates):
            list_column.append(input("Enter column to update:"))
            list_value.append(input("Enter new value to update:"))
        check_column = input("Enter column for condition check:")
        check_value = input("Enter value for condition check:")
        for i in range(no_of_updates):
            query = f"update {table_name} set {list_column[i]} = '{list_value[i]}' where {check_column} = {check_value}"
            self.run_query(input_str=query)
        print("Table updated successfully")
        # print("Record inserted successfully")

    def update_in_table(self, table_name, column_name, value, where_clause):
        query = f"update {table_name} set {column_name} = '{value}' where {where_clause}"
        self.run_query(input_str=query)
        print("Table updated successfully")

    def select_from_table(
        self,
        column_name,
        table_name,
        where_clause=""
    ):
        query = f"select {column_name} from {table_name}"
        if where_clause:
            query += f" where {where_clause}"
        res = self.run_query(input_str=query)
        return res.fetchall()

    def delete_from_table(self,table_name,where_clause):
        query = f"delete from {table_name} where {where_clause}"
        self.run_query(input_str=query)
        print("Record deleted successfully")
    def close_connection(
        self,
    ):
        self.con.close()


if __name__ == "__main__":
    conn_obj = DbUtils()
    # conn_obj.insert_into_table(table_name="user",values="1, 'Shrinath' ,'982766638'")
    # conn_obj.update_in_table(table_name="user",column_name="name",value="VijayKishore",where_clause="id = 1")
    # conn_obj.delete_from_table(table_name="user",where_clause="id = 2")
    # conn_obj.insert_into_table(table_name="user",values="1, 'Shrinath' ,'982766638'")
    # conn_obj.insert_into_table(table_name="user", values="2, 'Vijay' ,'9827666982'")
    conn_obj.insert_into_table(table_name="login", values="'vijaykishore','Vijay@123'")
    # conn_obj.insert_into_table(table_name="user",values=["1, '"])
    print(
        conn_obj.select_from_table(
            column_name="*",
            table_name="login",
            # where_clause="name = 'Vijay Kishore'",
        )
    )
    conn_obj.close_connection()