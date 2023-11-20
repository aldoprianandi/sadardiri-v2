from js import window
Quest = [
    "I like to receive notes of affirmation from you. (A) | I like it when you hug me. (E)",
    "I like to spend one-on-one time with you. (B) | I feel loved when you give me practical help. (D)",
    "I like it when you give me gifts. (C) | I like taking long walks with you. (B)",
    "I feel loved when you do things to help me. (D) | I feel loved when you hug or touch me. (E)",
    "I feel loved when you hold me in your arms. (E) | I feel loved when I receive a gift from you. (C)",
    "I like to go places with you. (B) | I like to hold hands with you. (E)",
    "I feel loved when you acknowledge me. (A) | Visible symbols of love (gifts) are very important to me. (C)",
    "I like to sit close to you. (E) | I like it when you tell me that I am attractive. (A)",
    "I like to spend time with you. (B) | I like to receive little gifts from you. (C)",
    "I know you love me when you help me. (D) | Your words of acceptance are important to me. (A)",
    "I like to be together when we do things. (B) | I like the kind words you say to me. (A)",
    "I feel whole when we hug. (E) | What you do affects me more than what you say. (D)",
    "I value your praise and try to avoid your criticism. (A) | Several inexpensive gifts mean more to me than one large expensive gift. (C)",
    "I feel closer to you when you touch me. (E) | I feel close when we are talking or doing something together. (B)",
    "I like you to compliment my achievements. (A) | I know you love me when you do things for me that you don’t enjoy doing. (D)",
    "I like for you to touch me when you walk by. (E) | I like when you listen to me sympathetically. (B)",
    "I really enjoy receiving gifts from you. (C) | I feel loved when you help me with my home projects. (D)",
    "I like when you compliment my appearance. (A) | I feel loved when you take the time to understand my feelings. (B)",
    "I feel secure when you are touching me. (E) | Your acts of service make me feel loved. (D)",
    "I appreciate the many things you do for me. (D) | I like receiving gifts that you make. (C)",
    "I really enjoy the feeling I get when you give me your undivided attention. (B) | I really enjoy the feeling I get when you do some act of service for me. (D)",
    "I feel loved when you celebrate my birthday with a gift. (C) | I feel loved when you celebrate my birthday with meaningful words (written or spoken). (A)",
    "I feel loved when you help me out with my chores. (D) | I know you are thinking of me when you give me a gift. (C)",
    "I appreciate it when you remember special days with a gift. (C) | I appreciate it when you listen patiently and don’t interrupt me. (B)",
    "I enjoy extended trips with you. (B) | I like to know that you are concerned enough to help me with my daily task. (D)",
    "Kissing me unexpectedly makes me feel loved. (E) | Giving me a gift for no occasion makes me feel loved. (C)",
    "I like to be told that you appreciate me. (A) | I like for you to look at me when we are talking. (B)",
    "Your gifts are always special to me. (C) | I feel loved when you kiss me. (E)",
    "I feel loved when you tell me how much you appreciate me. (A) | I feel loved when you enthusiastically do a task I have requested. (D)",
    "I need to be hugged by you every day. (E) | I need your words of affirmation daily. (A)",
]

Element("question").write(Quest[0])
i = 0

answers = []



def answer():
    global i
    #answer = input("Your choice (A, B, C, D, E): ").strip().upper()
    #answer = x.strip().upper()
    answer = Element('ans').element.value
    
    if answer in ('A', 'B', 'C', 'D', 'E'):
        answers.append(answer)
        

    else:
        Element("answer").write("Invalid choice. Please enter A, B, C, D, or E.")
        return

    
    
        
    if i == len(Quest) - 1:
        scores = calculate_love_languages_score(answers)  
        
        maximum = max(scores, key=scores.get)
        move(maximum)
        return
    i += 1
    Element("question").write(Quest[i])
    Element("answer").write("")
    #Element("answer").write(answers)
    

def calculate_love_languages_score(answers):
    scores = {
        'A': 0,  # Words of Affirmation
        'B': 0,  # Quality Time
        'C': 0,  # Receiving Gifts
        'D': 0,  # Acts of Service
        'E': 0   # Physical Touch
    }
    
    for answer in answers:
        scores[answer] += 1
    return scores

def move(x):
    if x == "A":
        window.location.href = "Result Love\A.html"
    if x == "B":
        window.location.href = "Result Love\B.html"
    if x == "C":
        window.location.href = "Result Love\C.html"
    if x == "D":
        window.location.href = "Result Love\D.html"
    if x == "E":
        window.location.href = "Result Love\E.html"