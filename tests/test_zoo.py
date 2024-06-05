import unittest
from unittest import TestCase
from src.Zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):
   
    def test_add_animal_dimension(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=800.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        
        result :int=len(fence_1.animals)
        message :str =f"Error: the function add_animal should not add animal_1 into fence_1, it's too big." 
        self.assertEqual(result, 0, message)

    def test_add_animal_habitat(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=2.0,width=1.0,preferred_habitat="savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        
        result :int=len(fence_1.animals)
        message :str =f"Error: the function add_animal should not add animal_1 into fence_1, it has a different preferred habitat." 
        self.assertEqual(result, 0, message)

    def test_remove_animal_removing(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=2.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        zookeeper_1.remove_animal(animal_1, fence_1)
        
        result :int=len(fence_1.animals)
        message :str =f"Error: the function remove_animal should remove animal_1 from fence_1" 
        self.assertEqual(result, 0, message)


    def test_remove_animal_empty(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=2.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.remove_animal(animal_1, fence_1)
        
        result :int=len(fence_1.animals)
        message :str =f"Error: the function remove_animal shouldn't do anything because animal_1 is not in fence_1" 
        self.assertEqual(result, 0, message)


    def test_feed_cant_feed(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=100.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        zookeeper_1.feed(animal_1)

        result :int=animal_1.height
        message :str =f"Error: the function feed_animal shouldn't do anything because animal_1 is already as big as fence_1" 
        self.assertEqual(result, 100, message)
    

    def test_feed_can_feed(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=10.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        zookeeper_1.feed(animal_1)

        result :int=round(animal_1.height+(animal_1.height*0.02),3)
        message :str =f"Error: the function feed_animal should increase animal_1's height because there is still space in fence_1" 
        self.assertEqual(result, 10.2, message)

        result :int=round(animal_1.width+(animal_1.width*0.02),3)
        message :str =f"Error: the function feed_animal should increase animal_1's width because there is still space in fence_1" 
        self.assertEqual(result, 1.02, message)

        result :int=round(animal_1.health*0.01,3)
        message :str =f"Error: the function feed_animal should increase animal_1's health because there is still space in fence_1" 
        self.assertEqual(result, 20.2, message)

    def test_clean_empty_fence(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")

        result :float=zookeeper_1.clean(fence_1)
        message :str =f"Error: the function clean should return 0.0 because fence_1 is empty and there is nothing to clean." 
        self.assertEqual(result, 0.0, message)

    def test_clean_with_feed(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=20.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        
        result :float=zookeeper_1.clean(fence_1)
        message :str =f"Error: the function clean return is wrong" 
        self.assertEqual(result, 0.25, message)

        zookeeper_1.feed(animal_1)
        
        result :float=zookeeper_1.clean(fence_1)
        message :str =f"Error: the function clean is wrong after you feed the animal." 
        self.assertEqual(result, 0.263, message)


    def test_clean_full_fence(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        animal_1=Animal(name="Pluto",species="Canide", age=5,height=100.0,width=1.0,preferred_habitat="Savanna")
        zookeeper_1.add_animal(animal_1, fence_1)
        
        result :float=zookeeper_1.clean(fence_1)
        message :str =f"Error: the function clean should return a value equivalent to fence_1's area, because it's full." 
        self.assertEqual(result, 100, message)
    
    def test_None(self):
        #Luca Cavalleri
        zookeeper_1=ZooKeeper(name="Gianni",surname="Rossi",id=1)
        fence_1=Fence(area=100,temperature=25.0,habitat="Savanna")
        
        message="Error: the function is not checking the types and using None values"
        try:
            zookeeper_1.add_animal(None, None)
        except(Exception):
            self.assertEqual(True, False, message)

        try:
            zookeeper_1.add_animal(None, fence_1)
        except(Exception):
            self.assertEqual(True, False, message)
        self.assertEqual(len(fence_1.animals), 0, "Error: your add_animal function saves in fence_1 a None value as an animal.")
        
        try:
            zookeeper_1.clean(None)
        except(Exception):
            self.assertEqual(True, False, message)

        try:
            zookeeper_1.feed(None)
        except(Exception):
            self.assertEqual(True, False, message)

        try:
            zookeeper_1.remove_animal(None, fence_1)
        except(Exception):
            self.assertEqual(True, False, \
                             "Error: the function is not checking the types and using None values or it's trying to remove an element the is not present in the fence")
        

    
if __name__ == "__main__":
    unittest.main()