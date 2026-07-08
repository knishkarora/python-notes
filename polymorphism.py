class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# The polymorphic calls - same function, different outputs
start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)


#  inheritance-based polymorphism.

class Animal:
   def speak(self):
       return 'Some generic sound'

class Cat(Animal):
   def speak(self):
       return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'
  
print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak()) # Some generic sound

# You can also take things further and do the calling in a list, then loop through the list to display what the speak() method returns for each:

animals = [Cat(), Dog(), Monkey()]

for animal in animals:
   print(animal.speak())

# Output:
# A cat meow
# A dog barks woof woof
# A monkey ooh ooh aah aah ooh ooh aah aah