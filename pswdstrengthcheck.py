import sys
commonpswd= {
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",
    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",
    "ashley", "nicole", "password123", "matthew", "access", "yankees", "987654321", "dallas",
    "austin", "thunder", "taylor", "matrix", "welcome", "phoenix", "camaro", "silver",
    "internet", "orange", "cookie", "maverick", "mercedes", "falcon", "hello123", "hello@123", "password@123"
}

def main():
    password=input("Enter your password: ").strip()
    score=10
    if len(password)<8:
        sys.exit("Too short")
    if password.lower() in commonpswd:
        sys.exit("Too common")
    if len(password)>12:
        score+=2
    if not uppercheck(password):
        score-=2
        print("Need at least one uppercase letter")
    if not lowercheck(password):
        score-=2
        print("Need at least one lowercase letter")
    if not numcheck(password):
        score-=2
        print("Need at least one digit")
    if not spclcharcheck(password):
        score-=2
        print("Need at least one special character")
    print("\nPassword complexity:")
    scoreprint(score)

def uppercheck(pswd):
    for c in pswd:
        if c.isupper():
            return True
    return False

def lowercheck(pswd):
    for c in pswd:
        if c.islower():
            return True
    return False

def numcheck(pswd):
    for c in pswd:
        if c.isdigit():
            return True
    return False

def spclcharcheck(pswd):
    spcl={"!",",","@","#","$","%","^","&","*","(",")","_","+","[","]","{","}","|",";",":",".","<",">","?","/","\\","'",'"'}
    for c in pswd:
        if c in spcl:
            return True
    return False

def scoreprint(score):
    if score<5:
        print("Password strength is TOO WEAK")
    elif score<8:
        print("Password strength is WEAK")
    elif score<10:
        print("Password strength is MEDIUM")
    elif score>=10:
        print("Password strength is STRONG")

main()
