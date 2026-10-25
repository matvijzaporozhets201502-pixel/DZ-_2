
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 2000
        self.energy = 100
        self.knowledge = 50
        self.day = 1

    def work(self):
        if self.energy >= 30:
            salary = random.randint(200, 500)
            self.money += salary
            self.energy -= 30
            print(f"{self.name} працює і заробляє {salary} грн.")
        else:
            print(f"{self.name} занадто втомився для роботи.")

    def rest(self):
        cost = 100
        self.money -= cost
        self.energy = min(100, self.energy + 40)
        print(f"{self.name} відпочиває. Витрачено {cost} грн.")

    def study(self):
        if self.energy >= 20:
            self.knowledge += random.randint(5, 15)
            self.energy -= 20
            print(f"{self.name} навчається.")
        else:
            print(f"{self.name} занадто втомився для навчання.")

    def live_day(self):
        print(f"\n--- День {self.day} ---")

        expenses = random.randint(50, 150)
        self.money -= expenses
        print(f"Щоденні витрати: {expenses} грн.")

        if self.money < 300:
            print("Грошей мало! Потрібно знайти роботу.")
            self.work()
        elif self.knowledge < 30:
            self.study()
        else:
            action = random.choice(["work", "rest", "study"])

            if action == "work":
                self.work()
            elif action == "rest":
                self.rest()
            else:
                self.study()

        event = random.randint(1, 10)

        if event == 1:
            bonus = 300
            self.money += bonus
            print(f"Студент отримав бонус {bonus} грн.")
        elif event == 2:
            loss = min(max(self.money, 0), 200)
            self.money -= loss
            print(f"Несподівані витрати: {loss} грн.")

        self.energy = max(0, min(100, self.energy))
        self.knowledge = max(0, min(100, self.knowledge))
        self.day += 1

    def show_status(self):
        print("\n===== РЕЗУЛЬТАТИ РОКУ =====")
        print(f"Ім'я студента: {self.name}")
        print(f"Гроші: {self.money} грн.")
        print(f"Енергія: {self.energy}/100")
        print(f"Знання: {self.knowledge}/100")

        if self.money < 0:
            print("Студент має борги!")
        elif self.knowledge >= 80:
            print("Студент добре навчався!")
        elif self.money >= 5000:
            print("Студент добре заробив!")
        else:
            print("Студент прожив звичайний рік.")


student = Student("Андрій")

print("Починається рік життя студента!")

for _ in range(365):
    student.live_day()

student.show_status()
