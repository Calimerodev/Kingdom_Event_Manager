import sqlite3

class Depend_Resources():
    def __init__(self):
        self.connection = sqlite3.Connection("DATA BASE.db")
        self.cursor = self.connection.cursor()
    

    def create(self):
        sql = """
            CREATE TABLE Depend_Resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_resource1 INTEGER,
                id_resource2 INTEGER
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def insert(self, id_resource1, id_resource2):
            sql = f"""
                INSERT INTO Depend_Resources(
                    id,
                    id_resource1,
                    id_resource2
                ) VALUES (
                    NULL,
                    {id_resource1},
                    {id_resource2}
                )
            """
            self.cursor.execute(sql)
            self.connection.commit()


    def getall(self):
        sql = """
            SELECT * FROM Depend_Resources
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_element(self,
                    id_depend = None,
                    id_resource1 = None,
                    id_resource2 = None
                ):
        
        all_depend = self.getall()
        
        for depend in all_depend:
            
            if id_depend == None:
                if depend[1] == id_resource1 and depend[2] == id_resource2:
                    return depend

            else:            
                if depend[0] == id_depend:
                    return depend
    
        return None


    def delete_id(self,id_depend):
        sql = """
            DELETE FROM Depend_Resources WHERE id = ?
        """
        self.cursor.execute(sql , (f"{id_depend}",))
        self.connection.commit()


    def update(
            self,
            new_id_resource1 = None,
            new_id_resource2 = None,
            id_depend = None
        ):
        
        change_id_resource1 = "" if new_id_resource1 == None else f"id_resource1 = {new_id_resource1}"
        change_id_resource2 = "" if new_id_resource2 == None else f",id_resource2 = {new_id_resource2}"

        sql = f"""
            UPDATE Depend_Resources SET
                {change_id_resource1}
                {change_id_resource2}
            WHERE id = ?
        """

        self.cursor.execute(sql, (id_depend,))
        self.connection.commit()


class Incompatibles_Resources():
    def __init__(self):
        self.connection = sqlite3.Connection("DATA BASE.db")
        self.cursor = self.connection.cursor()


    def create(self):
        sql = """
            CREATE TABLE Incompatibles_Resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_resource1 INTEGER,
                id_resource2 INTEGER
            )
        """

        self.cursor.execute(sql)
        self.connection.commit()


    def insert(self, id_resource1, id_resource2):
            sql = f"""
                INSERT INTO Incompatibles_Resources(
                    id,
                    id_resource1,
                    id_resource2
                ) VALUES (
                    NULL,
                    {id_resource1},
                    {id_resource2}
                )
            """
            self.cursor.execute(sql)
            self.connection.commit()


    def getall(self):
        sql = """
            SELECT * FROM Incompatibles_Resources
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_element(self,
                    id_incompatible = None,
                    id_resource1 = None,
                    id_resource2 = None
                ):
        
        all_incompatible = self.getall()
        
        for incompatible in all_incompatible:
            
            if id_incompatible == None:
                if incompatible[1] == id_resource1 and incompatible[2] == id_resource2:
                    return incompatible

            else:            
                if incompatible[0] == id_incompatible:
                    return incompatible
    
        return None


    def delete_id(self,id_incompatible):
        sql = """
            DELETE FROM Incompatibles_Resources WHERE id = ?
        """
        self.cursor.execute(sql , (f"{id_incompatible}",))
        self.connection.commit()
    

    def update(
            self,
            new_id_resource1 = None,
            new_id_resource2 = None,
            id_incompatible = None
        ):
        
        change_id_resource1 = "" if new_id_resource1 == None else f"id_resource1 = {new_id_resource1}"
        change_id_resource2 = "" if new_id_resource2 == None else f",id_resource2 = {new_id_resource2}"

        sql = f"""
            UPDATE Incompatibles_Resources SET
                {change_id_resource1}
                {change_id_resource2}
            WHERE id = ?
        """

        self.cursor.execute(sql, (id_incompatible,))
        self.connection.commit()


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
    

    def get_element(
                    self,
                    id_relation = None,
                    id_event=None,
                    id_resource = None
                ):
        all_reations = self.getall()
        
        for  relation in all_reations:
            if id_relation == None:
                if relation[1] == id_event and relation[2] == id_resource:
                    return relation
            
            else:
                if relation[0] == id_relation:
                    return relation
            
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
                execution INTEGER, 
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


    def get_element(
            self,
            id_event = None,
            name_event = None,
            place_event = None,
            resources_event = None,
            execution_event = None,
            start_event = None,
            end_event = None
            ):
        
        all_events = self.getall()
        
        for event in all_events:
            print(event)

            if id_event:
                if event[0] == id_event:
                    return event
            
            else:
                if name_event == event[1] and place_event == event[2] and resources_event == event[3] and execution_event == event[4] and start_event == event[5] and end_event == event[6]:
                    return event

        return (-1,-1,-1,-1,-1,-1,-1)


    def insert(
            self,
            name_event,
            place_event,
            resources_event,
            execution_event,
            start_event,
            end_event
        ):
        
        sql = f"""
            INSERT INTO Events(id,name,place,resources,execution,start,end) VALUES (
                NULL,
                '{name_event}',
                '{place_event}',
                {resources_event},
                {execution_event},
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
        return True


    def update(
            self,
            new_name_event = '*',
            new_place_event='*',
            new_resource_event='*',
            update_execution = '*',
            new_start_event='*',
            new_end_event='*',
            id_event = '*'
        ):
        print("Updating Event...") 
        change_name = "" if new_name_event == '*' else f"name = '{new_name_event}'"
        change_place = "" if new_place_event == '*' else f",place = '{new_place_event}'"
        change_resource = "" if new_resource_event == '*' else f",resources = {new_resource_event}"
        change_execution = "" if update_execution == '*' else f",execution = {update_execution}"
        change_start = "" if new_start_event == '*' else f",start = '{new_start_event}'"
        change_end = "" if new_end_event == '*' else f",end = '{new_end_event}'"
        
        sql = f"""
            UPDATE Events SET 
                {change_name}
                {change_place}
                {change_resource}
                {change_execution}
                {change_start}
                {change_end}
            WHERE id = ?
        """
        self.cursor.execute(sql , (id_event,))
        self.connection.commit()
