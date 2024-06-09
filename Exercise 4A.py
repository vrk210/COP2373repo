import time

def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val
    return wrapper

@make_timer
def calculate_spam_score(message):
    spam_keywords = [
        "free", "cash", "0% down", "cash back", "act now",
        "no interest", "risk-free", "no money down", "you're a winner!", "timeshare",
        "special promotion", "buy one get one free", "limited time deal", "invest now", "luxury",
        "special", "save money", "lowest price", "incredible deal", "earn money",
        "learn to make money", "on sale", "extremely affordable", "investment opportunity", "cash up front",
        "no cost", "no fees", "buy now", "apply now", "100% free"
    ]

    # Convert message to lowercase to match list
    lower_message = message.lower()

    # Calculate spam score
    spam_score = 0
    words_spam = []

    for keyword in spam_keywords:
        if keyword in lower_message:
            spam_score += 1
            words_spam.append(keyword)

    # Determines likelihood that the message is spam
    if spam_score <= 5:
        spam_likelihood = "Low"
    elif spam_score <= 15:
        spam_likelihood = "Medium"
    else:
        spam_likelihood = "High"

    return spam_score, spam_likelihood, words_spam

def main():
    print("Welcome to the Email Spam Detector App!")
    print("Enter an email to determine its spam score.")

    # Gets email from user
    message = input("Enter the email: ")

    # Calculates the spam score
    spam_score, spam_likelihood, words_spam = calculate_spam_score(message)

    # Displays the results
    print("\nSpam Score:", spam_score)
    print("Likelihood that this message is spam:", spam_likelihood)
    print("Words/Phrases that caused this message to be considered spam:", words_spam)

if __name__ == "__main__":
    main()

    # link to repo: https://github.com/vrk210/COP2373repo
