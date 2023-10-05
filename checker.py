import re

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
        
    if re.search("[a-z]", password):
        score += 1
        
    if re.search("[A-Z]", password):
        score += 1
        
    if re.search("[0-9]", password):
        score += 1
        
    if re.search("[@#$%^&+=]", password):
        score += 1

    return score

def crack_time_estimate(score):
    if score == 1:
        return "few seconds to minutes."
    elif score == 2:
        return "several minutes."
    elif score == 3:
        return "several hours."
    elif score == 4:
        return "several days."
    elif score == 5:
        return "many weeks to years."
    else:
        return "instantly."

password = input("Enter a password to test: ")
strength_score = password_strength(password)
crack_time = crack_time_estimate(strength_score)

print(f"Strength Score: {strength_score} out of 5")
print(f"Estimated Crack Time: {crack_time}")
