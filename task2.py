#3. Positive, Negative or Zero

'''num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")'''

#4. Library Fine Calculation (Using Class)

'''class Library:
    def input_days(self):
        self.days = int(input("Enter number of days late: "))

    def calculate_fine(self):
        if self.days <= 5:
            self.fine = self.days * 0.40
        elif self.days <= 10:
            self.fine = self.days * 0.65
        else:
            self.fine = self.days * 0.80

    def display(self):
        print("Fine amount: Rs", self.fine)'''

# Main
'''lib = Library()
lib.input_days()
lib.calculate_fine()
lib.display()'''

#5. Basic Calculator

'''weight = int(input("Enter parcel weight (kg): "))
booking = input("Enter booking type (O/E): ")

if weight <= 5:
    charge = weight * 30
else:
    charge = weight * 50

if booking == 'E' or booking == 'e':
    charge += 50

print("Total Charges: Rs", charge)'''

#8. Laptop Discount Calculation

'''price = float(input("Enter price of laptop: "))

if price >= 50000:
    discount = price * 0.20
elif price >= 30000:
    discount = price * 0.15
else:
    discount = price * 0.10

total_price = price - discount

print("Price of laptop :", price)
print("Discount :", discount)
print("Total Price :", total_price)'''








