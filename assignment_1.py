class Superhero:
    # Base class representing a superhero with core attributes and methods

    def __init__(self, name, secret_identity, power_level):
        # constructor to initialize a superhero's basic attribute
        self._name = name
        self._secret_identity = secret_identity
        self._power_level = power_level
        self._is_active = True

    def introduce(self):
        # Method for the hero to introduce themselves
        return f"I'm {self._name}, defender of justice!"
    
    def activate_mission(self):
        # Activate the hero's mission status.
        self._is_active = True
        return f"{self._name} is now active duty!"
    
    def deactivate_mission(self):
        # Deactivate the hero's mission status.
        self._is_active = False
        return f"{self._name} is taking a break."
    
    def get_power_level(self):
        # Retrieve the hero's current power level.
        return self._power_level
    
class ComicBookSuperHero(Superhero):
    # Specialized superhero class with comic book specific attributes.
    def __init__(self, name, secret_identity, power_level, comic_publisher, first_appearance):
        # Extended constructor for comic book superheroes
        super().__init__(name, secret_identity, power_level)
        self._comic_publisher = comic_publisher
        self._first_appearance = first_appearance
        self._team_affiliations = []

    def add_team_affiliation(self, team_name):
        # Add a new team affiliation for the hero.
        if team_name not in self._team_affiliations:
            self._team_affiliations.append(team_name)
            return f"{self._name} is now part of {team_name}!"
        return f"{self._name} is already a member of {team_name}."
    
    def get_comic_info(self):
        # Retrieve detailed comic book information about the hero.
        return {
            "Name": self._name,
            "Publisher": self._comic_publisher,
            "First Appearance": self._first_appearance,
            "Teams": self._team_affiliations
        }
    

class SuperheroTeam:
    # Represents the team of superheroes with management capabilities
    def __init__(self, team_name):
        # Initialize a superhero team
        self._team_name = team_name
        self._members = []

    def recruit_hero(self, hero):
        # Recruit a superhero to the team
        if hero not in self._members:
            self._members.append(hero)
            return f"{hero._name} has been recruited to {self._team_name}!"
        return f"{hero._name} is already a member of {self._team_name}."
    
    def team_power_level(self):
        # Calculates the total team power level
        return sum(hero.get_power_level() for hero in self._members)
    

# Demostration
def main():
    # Create superhero instances
    spider_man = ComicBookSuperHero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        power_level=85,
        comic_publisher="Marvel",
        first_appearance=1962
    )

    batman = ComicBookSuperHero(
        name="Batman",
        secret_identity="Bruce Wayne",
        power_level=75,
        comic_publisher="DC",
        first_appearance=1939
    )

    # Team creation and hero recruitment
    avengers = SuperheroTeam("The Avengers")
    avengers.recruit_hero(spider_man)

    # Demostrate methods
    print(spider_man.introduce())
    print(spider_man.add_team_affiliation("Avengers"))
    print(spider_man.get_comic_info())
    print(f"Team Power Level: {avengers.team_power_level()}")

if __name__ == "__main__":
    main()