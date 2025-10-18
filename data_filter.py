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
        
        alldependencys = Depend_Resources().getall()
        for resource in resources:
            for dependency in alldependencys:
                if dependency[1] == resource:
                    resources.append(dependency[2])
        
        #allincompatibilitys = Incompatibles_Resources().getall()
        for i in range(len(resources)):
           for j in range(len(resources)):
                if i == j:
                    continue
                if(Incompatibles_Resources().get_element(resources[i],resources[j]) != None or Incompatibles_Resources().get_element(resources[j],resources[i]) != None):
                    return "Recursos Incompatibles"


        Events().insert(
            name_event=name_event,
            place_event=place_event,
            resources_event=resources_event,
            execution_event=execution_event, 
            start_event=start_event,
            end_event=end_event
        )


        actual_event = Events().get_element(
                                    name_event=name_event,
                                    place_event=place_event,
                                    resources_event=resources_event,
                                    execution_event=execution_event,
                                    start_event=start_event,
                                    end_event=end_event
                                )

        for resource in resources:
            #print(actual_event , resource)
            Events_Resources_Relation().insert(actual_event[0] , resource)

        Events().update(
            new_name_event=actual_event[1],
            new_place_event=actual_event[2],
            new_resource_event=0,
            new_start_event=actual_event[4],
            new_end_event=actual_event[5],
            id_event=actual_event[0]
        )


    def delete_event(self, id_event):
        
        all_relations = Events_Resources_Relation().getall()
        
        for relation in all_relations:
            if relation[1] == id_event:
                Events_Resources_Relation().delete_id(relation[0])
        
        Events.delete_id(id_event=id_event)
    
    
    def show_resouce_event(self, id_event):
        all_relations = Events_Resources_Relation().getall()
        resources_event = []
        
        for relation in all_relations:
            #print(relation)
            if relation[1] == id_event:
                resources_event.append(Resources().get_element(relation[2]))
        
        return resources_event


    def search_hole(self):
        pass