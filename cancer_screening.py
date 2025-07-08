from datetime import datetime, timedelta

def calculate_risk(age, family_history, smoker, alcohol_use):
    score = 0
    if age >= 50:
        score += 2
    elif age >= 40:
        score += 1
    if family_history:
        score += 2
    if smoker:
        score += 1
    if alcohol_use:
        score += 1

    if score >= 4:
        return "High"
    elif score >= 2:
        return "Medium"
    else:
        return "Low"

def next_screening_date(risk):
    today = datetime.today()
    if risk == "High":
        interval = 1
    elif risk == "Medium":
        interval = 2
    else:
        interval = 3
    return (today + timedelta(days=interval * 365)).strftime('%Y-%m-%d')

def main():
    print("📋 Cancer Screening Risk Calculator\n")

    name = input("Enter patient name: ")
    gender = input("Enter gender (male/female): ").lower()
    age = int(input("Enter age: "))
    family_history = input("Family history of cancer? (yes/no): ").strip().lower() == "yes"
    smoker = input("Smoker? (yes/no): ").strip().lower() == "yes"
    alcohol_use = input("Alcohol use? (yes/no): ").strip().lower() == "yes"

    risk = calculate_risk(age, family_history, smoker, alcohol_use)
    breast_date = next_screening_date(risk)
    cervical_date = next_screening_date(risk)
    colorectal_date = next_screening_date(risk)

    print("\n✅ Patient Summary:")
    print(f"Name: {name}")
    print(f"Gender: {gender.capitalize()}")
    print(f"Age: {age}")
    print(f"Risk Level: {risk}")
    print("\n📅 Next Screening Dates:")

    print(f"  Breast Cancer:     {breast_date}")
    if gender == "female":
        print(f"  Cervical Cancer:   {cervical_date}")
    else:
        print(f"  Cervical Cancer:   Not applicable")
    print(f"  Colorectal Cancer: {colorectal_date}")

if __name__ == "__main__":
    main()


