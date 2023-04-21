#1) დაწერეთ შემდეგი პროგრამა:
# კონსოლიდან შეიყვანეთ იუზერის სახელი და პაროლი. თუ დაემთხვა თქვენს მიერ შექმნილ
# იუზერს და პაროლს, კონსოლზე დაიბეჭდოს წარმატება. 5 ცდის შემდეგ კი დააბრუნოს
# შეცდომის შეტყობინება.
def guess_user():
    """Guess the user's name and password."""
    # pre-defined username and password
    username = 'admin'
    password = 'admin'

    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:

        user_input_username = input("Enter your username: ")
        user_input_password = input("Enter your password: ")

        if user_input_username == username and user_input_password == password:
            print("Success! Your username is:", username, "and your password is:", password)
            break
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    if attempts == max_attempts:
        print("Maximum number of attempts reached. Please try again later.")

#2) დაწერეთ პროგრამა, რომელიც კონსოლიდან შეყვანილ რიცხვს გადაიყვანს ორობით
# ფორმატში.
# შედეგი დაბეჭდეთ კონსოლზე.
def to_binary():
    """Convert a decimal number to binary."""
    decimal = int(input("Enter a decimal number: "))
    binary = ''

    while decimal > 0:
        remainder = decimal % 2
        print(remainder)
        binary = str(remainder) + binary
        decimal = decimal // 2

    print("The binary representation is:", binary)


#3) 3) შექმენით ორი გადატვირთული მეთოდი.
# პირველი მეთოდი უნდა ითვლიდეს ფართობს (სიგრძე * სიგანეზე), მეორე მეთოდი
# მოცულობას (სიგრძე * სიგანე * სიმაღლე). გადაეცით მეთოდებს შესაბამისი რაოდენობის
# პარამეტრები.
class Calculator:
    def calculate_area(self, length, width):
        return length * width

    def calculate_volume(self, length, width, height):
        return length * width * height

calc = Calculator()
print(calc.calculate_area(5, 10))
print(calc.calculate_volume(5, 10, 15))


