

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + ".")
    print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')


# positional arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet2(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# A dog named Willie.
describe_pet2('willie')
describe_pet2(pet_name='willie')

# A hamster named Harry.
describe_pet2('harry', 'hamster')
describe_pet2(pet_name='harry', animal_type='hamster')
describe_pet2(animal_type='hamster', pet_name='harry')

describe_pet2()
