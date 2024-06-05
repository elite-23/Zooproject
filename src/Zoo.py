'''
Sistema di gestione dello zoo virtuale

CLASSI:

    1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

    2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, 
        health che è uguale a round(100 * (1 / age), 3).

    3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. 
        I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

    4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
        I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.


FUNZIONALITÀ:
    X1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
        L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
        ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

    X2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
        L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

    X3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
        Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) 
        vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

    X4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
        Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
        Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

    X5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) 
con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

GUARDIANS:

    ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

FENCES:

    Fence(area=100, temperature=25, habitat=Continent)

WITH ANIMALS:

    Animal(name=Scoiattolo, species=Blabla, age=25)

    Animal(name=Lupo, species=Lupus, age=14)

#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
'''

class Animal:
    def __init__(self, name :str, species :str, age :int, height :float, width :float , preferred_habitat :str) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=round(height,3)
        self.width=round(width,3)
        self.preferred_habitat=preferred_habitat
        self.health=round(100 * (1 / age), 3)
        self.fence=None

    def __str__(self) -> str:
        return "Animal(name="+self.name+", species="+self.species+", age="+str(self.age)+", height="+str(self.height)+", width="+str(self.width)+", preferred_habitat="+self.preferred_habitat+")\n"
    
    def __eq__(self, value :object) -> bool:
        return self.name==value.name and self.species==value.species # type: ignore
    
    def put_in_fence(self,fence :object):
        self.fence=fence

    def removed_from_fence(self):
        self.fence=None

    
    
class Fence:
    def __init__(self, area :float, temperature :float, habitat :str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.animals :list[Animal]=[]
        self.area_left=area
    
    def __str__(self) -> str:
        if len(self.animals)>0:
            f="Fence(area="+str(self.area)+", temperature="+str(self.temperature)+", habitat="+self.habitat+")\nwith animals:\n"
            for i in self.animals:
                f+=i.__str__()
            return f
        else:
            return "Fence(area="+str(self.area)+", temperature="+str(self.temperature)+", habitat="+self.habitat+")"


    def add_animal(self,animal :Animal) -> None:
        self.area_left= round(self.area_left - (animal.height*animal.width),3)
        self.animals.append(animal)

    def remove_animal(self, animal :Animal) -> None:
        for i in self.animals:
            if i==animal:
                self.animals.remove(animal)
                self.area_left= round(self.area_left + (animal.height*animal.width),3)
                break


class ZooKeeper:
    def __init__(self,name :str, surname :str, id :int) -> None:
        self.name=name
        self.surname=surname
        self.id=id

    def __str__(self) -> str:
        return "ZooKeeper(name="+self.name+", surname="+self.surname+", id="+str(self.id)+")\n"


    def add_animal(self, animal: Animal, fence: Fence) -> None:
        if animal and isinstance(animal, Animal) and fence and isinstance(fence, Fence) and animal.preferred_habitat==fence.habitat and animal.fence==None:

            if animal.height*animal.width <= fence.area_left:
                fence.add_animal(animal)
                animal.put_in_fence(fence)

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal and isinstance(animal, Animal) and fence and isinstance(fence, Fence) and animal in fence.animals:
            fence.remove_animal(animal)
            animal.removed_from_fence()
        

    def feed(self, animal: Animal):
        if animal and isinstance(animal,Animal):
            fence=animal.fence
            Nwidth=round(animal.width+(animal.width*0.02),3)
            Nheight=round(animal.height+(animal.height*0.02),3)
            
            if fence and fence.area_left>= Nheight*Nwidth:        
                fence.area_left-=round((Nwidth*Nheight) - (animal.width*animal.height),3)
                animal.height=Nheight
                animal.width=Nwidth
                animal.health+=round(animal.health*0.01,3)

    def clean(self, fence: Fence):
        if fence and isinstance(fence, Fence):
            if fence.area_left==0:
                return fence.area
            else:
                time :float=round((fence.area-fence.area_left)/fence.area_left,3)
                return time
        

class Zoo:

    def __init__(self,fences :list[Fence], zoo_keepers :list[ZooKeeper]) -> None:
        if fences and isinstance(fences, list) and isinstance(fences[0],Fence) and zoo_keepers and isinstance(zoo_keepers, list) and isinstance(zoo_keepers[0],ZooKeeper):
            self.fences=fences
            self.zoo_keepers=zoo_keepers
        else:
            self.fences=[]
            self.zoo_keepers=[]

    def describe_zoo(self):
        go=False
        z=""
        if len(self.zoo_keepers)>0:
            z="Guardians:\n"
            for i in self.zoo_keepers:
                z+=i.__str__()
            
        for i in self.fences:
            if len(i.animals)!=0:
                go=True
                break

        if go:
            z+="Fences:\n"
            for i in range(len(self.fences)):
                if len(self.fences[i].animals)!=0:
                    z+=""+self.fences[i].__str__()
                    if i+1<len(self.fences):
                        if len(self.fences[i+1].animals)!=0:
                            z+="##############################\n"
        
        print(z)