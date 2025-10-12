import sqlite3

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


class Resources():
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


    def insert(self , name_resource , resource_cuantity , resource_aviable, assigned_to):
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


class Events():
    def __init__(self):
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


    def get_element(self , id_event):
        
        all_events = self.getall()
        
        for event in all_events:
            if event[0] == id_event:
                return event
            
        return None


    def insert(self , name_event , type_event , resources_event , start_event , end_event):
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


data = Events()
data2 = Resources()

data.create()
data2.create()

#data.create()

print(data.getall())

