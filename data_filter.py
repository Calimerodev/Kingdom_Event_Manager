import sqlite3
from models.models import *

class Manager_Events():
    
    def insert_event(
            self,
            name_event,
            place_event,
            resources_event,
            execution_event,
            start_event,
            end_event,
            resources = [],
        ):
        
        print (Events().insert(
            name_event=name_event,
            place_event=place_event,
            resources_event=resources_event,
            execution_event=execution_event, 
            start_event=start_event,
            end_event=end_event
        ))

        actual_event = Events().get_element(
                                    name_event=name_event,
                                    place_event=place_event,
                                    resources_event=resources_event,
                                    execution_event=execution_event,
                                    start_event=start_event,
                                    end_event=end_event
                                )
        
        all_resources = []

        alldependencys = Depend_Resources().getall()
        for resource in resources:
            for dependency in alldependencys:
                if dependency[1] == resource:
                    resources.append(dependency[2])

        for resource in resources:
            Events_Resources_Relation().insert(actual_event[0] , resource[0])


    def delete_event(self):
        pass
    
    
    def show_resouce_event(self, id_event):
        all_relations = Events_Resources_Relation().getall()
        resources_event = []
        
        for relation in all_relations:
            if relation[1] == id_event:
                resources_event.append(Resources().get_element(id_event=relation[2]).copy())
        
        return resources_event

    def search_hole(self):
        pass