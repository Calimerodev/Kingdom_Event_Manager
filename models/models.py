import sqlite3

class Depend_Resources():
    pass


class Incompatibles_Resources():
    def __init__(self):
        self.connection = sqlite3.Connection("DATA BASE.db")
        self.cursor = self.connection.cursor()


    def create(self):
        sql = """
            CREATE TABLE Incmpatibles_Rsources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_resource1 INTEGER,
                id_resource2 INTEGER
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def insert():
        pass


class Events_Resources_Relation():
    def __init__(self):
        self.connection = sqlite3.Connection("DATA BASE.db")
        self.cursor = self.connection.cursor()


    def create(self):
        sql = """
            CREATE TABLE Events_Resources_Relation(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_event INTEGER,
                id_resource INTEGER
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def insert(self , id_event , id_resource):
        sql = f"""
            INSERT INTO Events_Resources_Relation(id, id_event, id_resource) VALUES (
                NULL,
                {id_event},
                {id_resource}
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def getall(self):
        sql = """
            SELECT * FROM Events_Resources_Relation
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    

    def get_element(self, id_relation):
        all_events = self.getall()
        
        for event in all_events:
            if event[0] == id_relation:
                return event
            
        return None
    

    def delete_id(self,id_relation):
        sql = """
            DELETE FROM Events_Resources_Relation WHERE id = ?
        """
        self.cursor.execute(sql , (f"{id_relation}",))
        self.connection.commit()
    

    def update(
            self,
            new_id_event=None,
            new_id_resource=None,
            id_relation = None
        ):
        
        change_id_event = "" if new_id_event == None else f"id_event = {new_id_event}"
        change_id_resource = "" if new_id_resource == None else f",id_resource = {new_id_resource}"

        sql = f"""
            UPDATE Events_Resources_Relation SET
                {change_id_event}
                {change_id_resource}
            WHERE id = ?
        """

        self.cursor.execute(sql, (id_relation,))
        self.connection.commit()


class Resources(Events_Resources_Relation):
    def __init__(self):
        self.connection = sqlite3.connect("DATA BASE.db")
        self.cursor = self.connection.cursor()


    def create(self):
        sql = """
            CREATE TABLE Resources (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT,
                resources_cuantity INTEGER,
                resources_aviable INTEGER,
                assigned_to TEXT
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def get_element(self, id_resource):
        all_events = self.getall()
        
        for event in all_events:
            if event[0] == id_resource:
                return event
            
        return None


    def getall(self):
        sql = """
            SELECT * FROM Resources
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def insert(self,
               name_resource,
               resource_cuantity,
               resource_aviable, 
               assigned_to
            ):
     
        sql = f"""
            INSERT INTO Resources(id,name,resources_cuantity,resources_aviable,assigned_to) VALUES (
                NULL,
                '{name_resource}',
                {resource_cuantity},
                {resource_aviable},
                '{assigned_to}'
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()
        return True
    

    def delete_id(self,id_resource):
        sql = """
            DELETE FROM Resources WHERE id = ?
        """
        self.cursor.execute(sql , (f"{id_resource}",))
        self.connection.commit()


    def update(
            self,
            new_name_resource = None,
            new_cuantity_resource=None,
            new_aviable_resource=None,
            new_assigned_to=None,
            id_resource = None
        ):

        change_name = "" if new_name_resource == None else f"name = '{new_name_resource}'"
        change_cuantity_resources = "" if new_cuantity_resource == None else f",resources_cuantity = {new_cuantity_resource}"
        change_aviable_resources = "" if new_aviable_resource == None else f",resources_aviable = {new_aviable_resource}"
        change_assigned_to = "" if new_assigned_to == None else f",assigned_to = '{new_assigned_to}'"
        
        sql = f"""
            UPDATE Resources SET
                {change_name}
                {change_cuantity_resources}
                {change_aviable_resources}
                {change_assigned_to}
            WHERE id = ?
        """

        self.cursor.execute(sql , (id_resource,))
        self.connection.commit()


class Events(Events_Resources_Relation):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.Connection("DATA BASE.db")
        self.cursor = self.connection.cursor()


    def create(self):
        sql = """
            CREATE TABLE Events (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT,
                place TEXT,
                resources INTEGER,
                start TEXT,
                end TEXT
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def getall(self):
        sql = """
            SELECT * FROM Events
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_element(self , id_event , id_resource):
        
        all_events = self.getall()
        
        for event in all_events:
            if event[1] == id_event and event[2] == id_resource:
                return event
            
        return None


    def insert(
            self,
            name_event,
            type_event,
            resources_event,
            start_event,
            end_event
            ):
        
        sql = f"""
            INSERT INTO Events(id,name,place,resources,start,end) VALUES (
                NULL,
                '{name_event}',
                '{type_event}',
                {resources_event},
                '{start_event}',
                '{end_event}'
            )
        """
        self.cursor.execute(sql)
        self.connection.commit()
        return True        


    def delete_id(self,id_event):
        sql = """
            DELETE FROM Events WHERE id = ?
        """
        self.cursor.execute(sql , (f"{id_event}",))
        self.connection.commit()


    def update(
            self,
            new_name_event = None,
            new_type_event=None,
            new_resource_event=None,
            new_start_event=None,
            new_end_event=None,
            id_event = None
        ):
        
        change_name = "" if new_name_event == None else f"name = '{new_name_event}'"
        change_type = "" if new_type_event == None else f",place = {new_type_event}"
        change_resource = "" if new_resource_event == None else f",resources = '{new_resource_event}'"
        change_start = "" if new_start_event == None else f",start = '{new_start_event}'"
        change_end = "" if new_end_event == None else f",end = '{new_end_event}'"
        
        sql = f"""
            UPDATE Events SET 
                {change_name}
                {change_type}
                {change_resource}
                {change_start}
                {change_end}
            WHERE id = ? 
        """
        self.cursor.execute(sql , (id_event,))
        self.connection.commit()


data = Incompatibles_Resources()