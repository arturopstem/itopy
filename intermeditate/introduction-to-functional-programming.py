def shout(text):
  return text.upper()
yell = shout
print(yell("Hello"))


def welcome(name):
  return "Welcome, " + name


def process_user(name, func):
  return func(name)


print(process_user("Alice",welcome))

def order(dish):
  return "Your order: " + dish


def process_order(dish, func):
  print(func(dish))


process_order("Spaghetti", order)


def book_title(title):
  return "Book title: " + title


def info(title, func):
  return func(title)


print(info("The Great Gatsby", book_title))