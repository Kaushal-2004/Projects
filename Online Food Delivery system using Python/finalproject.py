class Display:
    def display_account(self):

        print("|================================================================|")
        print("|------------Welcome to Online Food Delivery System--------------|")
        print("|    [1]. Create Account                                         |")
        print("|    [2]. Sign in                                                |")
        print("|    [3]. Exit                                                   |")
        print("|================================================================|")
        choice=int(input("Enter your choice: "))

        if(choice==1):
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            new_user=user_account(username,password)
            new_user.create_user()
            

        elif(choice==2):
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            user_exits=user_account(username,password)
            user_exits.sign_in()

        elif(choice==3):
            print("|================================================================|")
            print("|    Exiting...                                                  |")
            print("|================================================================|")
            exit()

        else:
            print("|================================================================|")
            print("|    Invalid choice...                                           |")
            print("|================================================================|")
            self.display_account()

class user_account:

    user_list={}
    address={}
    object=Display()
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_user(self):
        if self.username in self.user_list:
            print("|----------------------------------------------------------------|")
            print("|    User already exists...                                      |")
            print("|----------------------------------------------------------------|")
            self.object.display_account()
            
        else:
            user_account.user_list[self.username]=self.password
            print("|----------------------------------------------------------------|")
            print(f"|   New user {self.username} created...                           |")
            print("|----------------------------------------------------------------|")
            self.object.display_account()
    
    def sign_in(self):
        if self.username in self.user_list:
            if self.password==self.user_list[self.username]:
                print("|----------------------------------------------------------------|")
                print("|    User signed in successfully...                              |")
                print(f"|    welcome {self.username}...                                        |")
                print("|----------------------------------------------------------------|")
                self.delivery_address()
                
            else:
                print("|----------------------------------------------------------------|")
                print("|    Username or Password are incorrect...                       |")
                print("|----------------------------------------------------------------|")
                self.object.display_account()
        else:
            print("|----------------------------------------------------------------|")
            print("|    User does not exist...                                      |")
            print("|----------------------------------------------------------------|")
            self.object.display_account()

    def add_new_address(self):
        x=str(input("if you want to add/update a new location (yes or no): "))
        if x.lower() == "yes":
            self.delivery_address()
        
        elif x.lower() == "no":
            return False

        else:
            print("|----------------------------------------------------------------|")
            print("|    Enter a valid option...                                     |")
            print("|----------------------------------------------------------------|")
            self.add_new_address()
        
    def delivery_address(self):
        print("|----------------------------------------------------------------|")
        print("|------------------Adding Delivering location--------------------|")
        add_type=input("Enter your Delivery Location Type(Home/Office/Other) : ")
        location=input("Enter your Delivery Final Location : ")

        if add_type.lower()=="home":
            self.address["Home"]=location
            print("|----------------------------------------------------------------|")
            print("|    Delivery location successfully added...                     |")
            print("|----------------------------------------------------------------|")
            self.add_new_address()

        elif add_type.lower()=="office":
            self.address["Office"]=location
            print("|----------------------------------------------------------------|")
            print("|    Delivery location successfully added...                     |")
            print("|----------------------------------------------------------------|")
            self.add_new_address()

        elif add_type.lower()=="other":
            self.address["Other"]=location
            print("|----------------------------------------------------------------|")
            print("|    Delivery location successfully added...                     |")
            print("|----------------------------------------------------------------|")
            self.add_new_address()

        else:
            print("|----------------------------------------------------------------|")
            print("|    Enter a invalid option...                                   |")
            print("|----------------------------------------------------------------|")
            self.delivery_address()
        
class FoodMenu:
    def __init__(self):

        self.pizza={"Marghrita":100, "Onion":85, "Tomato":80, "Golden Corn":90, "Maharaja Panner":140, "7-cheese":250, "Bahubali Pizza":1000, "Classic Pizza":200}
        self.burger={"Veg Aloo Tikki":70, "Veg Panner":100, "PeriPeri":120, "Tanduri":125, "Cheese":130, "Maharaja":160}
        self.sandwich={"Veg":70, "Aloo Mattar":80, "Panner Masala":110, "Veg Grill":100, "Cheese":140, "Bahubali":200}
        self.thali={"Gujarati":100, "Panjabi":130, "South Indian":120, "Farali":90}
        self.chinese={"Manchurian":100, "Panner Chilli":120, "Fried Rice":110, "Veg Noodles":90, "Hot & Sour Soup":85}
        self.drinks={"Pepsi":50, "CocaCola":50, "ThumsUp":50, "Limca":40, "Fanta":45, "Frooti":50, "Mazza":55, "Slice Mango Drink":60}
        self.snacks={"Khaman Dhokla":30, "Samosa":25, "Bhajiya":40, "Sev Khamani":45, "Kachori":40, "Gathiya":50, "Fafda and Jalebi":65, "Dabeli":25, "Vadapav":25, "Puff":20, "PavBhaji":50}
        self.icecream={"Chocolate":100, "Vanila":70, "Mango":80, "Rose":80, "Oreo Browne":120, "Rajbhog":100, "Kesar Pista":90, "American DryFruits":125}
        self.dessert={"Chocolate Cake":150, "Cheese Cake":150, "Chocolate Browne":100, "Cookies":100, "Gulab Jamun":90, "Rasagulla":90, "Lava Cakes with flavor":160}
        self.selected_items={}
        self.qty = {}
        self.final_payment_amt=0

    def pizza_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|---------------------------Pizza Menu---------------------------|")
        for key, value in self.pizza.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
        i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite pizza no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.pizza_menu()
        else:
            quantity = int(input("Enter the quantity of item : "))
            for key, value in self.pizza.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value * quantity
                        self.qty[key] += quantity
                        print("|----------------------------------------------------------------|")
                        print(f"|    {quantity} {key} Pizza(s) successfully added to cart...   |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value * quantity
                        self.qty[key] = quantity
                        print("|----------------------------------------------------------------|")
                        print(f"|    {quantity} {key} Pizza(s) successfully added to cart...   |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.pizza_menu()

    def burger_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|--------------------------Burger Menu---------------------------|")
        for key, value in self.burger.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite burger no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.burger_menu()
        
        else:
            for key, value in self.burger.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Burger successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Burger successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.burger_menu()

    def sandwich_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|-------------------------Sandwich Menu--------------------------|")
        for key, value in self.sandwich.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite sandwich no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.sandwich_menu()
        
        else:
            for key, value in self.sandwich.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Sandwich successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Sandwich successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.sandwich_menu()
    
    def thali_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|---------------------------Thali Menu---------------------------|")
        for key, value in self.thali.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite thali no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.thali_menu()
        
        else:
            for key, value in self.thali.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Thali successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Thali successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.thali_menu()

    def chinese_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|--------------------------Chinese Menu--------------------------|")
        for key, value in self.chinese.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite chinese no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.chinese_menu()
        
        else:
            for key, value in self.chinese.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.chinese_menu()

    def drinks_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|--------------------------Drinks Menu---------------------------|")
        for key, value in self.drinks.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite drinks no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.drinks_menu()
        
        else:
            for key, value in self.drinks.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Drink successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Drink successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.drinks_menu()

    def snacks_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|--------------------------snacks Menu---------------------------|")
        for key, value in self.snacks.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite snacks no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.snacks_menu()
        
        else:
            for key, value in self.snacks.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} snacks successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} snacks successfully added to cart...                  |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.snacks_menu()

    def icecream_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|-------------------------Ice-Cream Menu-------------------------|")
        for key, value in self.icecream.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total  Bill...                                |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite ice-cream no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.snacks_menu()
        
        else:
            for key, value in self.icecream.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Ice-cream successfully added to cart...               |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} Ice-cream successfully added to cart...               |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.icecream_menu()

    def dessert_menu(self):
        i=1
        j=1
        print("|================================================================|")
        print("|--------------------------Dessert Menu--------------------------|")
        for key, value in self.dessert.items():
            print(f"|   [{i}] {key:33}: Rs. {value}                |")
            i += 1
        print("|----------------------------------------------------------------|")
        print("|   [100]. Display Total Bill...                                 |")
        print("|   [200]. go back...                                            |")
        print("|================================================================|")
        c = int(input("Enter your favorite dessert no : "))

        if c == 100:
            self.total_bill()

        elif c == 200:
            self.display_menu()

        elif (c!=100 and c!=200 and c>=i):
            print("|----------------------------------------------------------------|")
            print("|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.dessert_menu()
        
        else:
            for key, value in self.dessert.items():
                if j == c:
                    if key in self.selected_items:
                        self.selected_items[key] += value
                        self.qty[key] += 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} successfully added to cart...                         |")
                        print("|----------------------------------------------------------------|")
                    else:
                        self.selected_items[key] = value
                        self.qty[key] = 1
                        print("|----------------------------------------------------------------|")
                        print(f"|    {key} successfully added to cart...                         |")
                        print("|----------------------------------------------------------------|")
                j+=1
            self.dessert_menu()

    def final_stage(self):
        print("|----------------------------------------------------------------|")
        print("|-------------------------Congratulations------------------------|")
        print("|    your order will deliver soon at your selected location...   |")
        print("|----------------------------------------------------------------|")
        print("|    Thank you for shopping with us...                           |")
        print("|----------------------------------------------------------------|")
        exit()
    
    def payment(self):

        print("|----------------------------------------------------------------|")
        print("|-------------------------Payment Method-------------------------|")
        print("|    [1]. Cash/UPI on Delivery                                   |")
        print("|    [2]. UPI(Google Pay/Phone Pay/PayTM)                        |")
        print("|    [3]. Credit/Debit/ATM Card                                  |")
        print("|----------------------------------------------------------------|")
        pay=int(input("Enter your choice: "))
        if(pay==1):
            print("|----------------------------------------------------------------|")
            print("You have selected Cash on Delivery. You will pay when the product is delivered.")
            print("|----------------------------------------------------------------|")
            self.final_stage()
        
        elif(pay==2):
            upi_id = str(input("Enter your UPI ID : "))
            amount = float(input("Enter the payment amount: "))
            try:
                if amount<self.final_payment_amt or amount>self.final_payment_amt:
                    print("|----------------------------------------------------------------|")
                    print(f"|    Invalid payment amount...                                   |")
                    print("|----------------------------------------------------------------|")
                    self.payment()
            except Exception as e:
                print("|----------------------------------------------------------------|")
                print(f"   Invalid payment amount: {e} ")
                print("|----------------------------------------------------------------|")
                self.payment()
                
            confirm=str(input(f"Please confirm your payment is paid to {upi_id} UPI ID (Yes/No): "))

            if(confirm.lower()=="yes"):
                print("|----------------------------------------------------------------|")
                print(f"|    Payment of {amount} is received by {upi_id} successfully...      |")
                print("|----------------------------------------------------------------|")
                self.final_stage()
            
            elif(confirm.lower() =="no"):
                print("|----------------------------------------------------------------|")
                print(f"|    Payment of {self.final_payment_amt} is not received by {upi_id}...!      |")
                print("|    Try Again...                                                |")
                print("|----------------------------------------------------------------|")
                self.payment()
            
            else:
                print("|----------------------------------------------------------------|")
                print(f"|    Invalid choice...                                           |")
                print("|----------------------------------------------------------------|")
                self.payment()

        elif(pay==3):
            card_number = str(input("Enter your card number: "))
            if len(card_number)!=16:
                print("|----------------------------------------------------------------|")
                print(f"|    Invalid card number...                                      |")
                print("|----------------------------------------------------------------|")
                self.payment()
            expiry_date = str(input("Enter card expiry date (MM/YY): "))
            if len(expiry_date)!=5:
                print("|----------------------------------------------------------------|")
                print(f"|    Invalid expiry date...                                      |")
                print("|----------------------------------------------------------------|")
                self.payment()
            else:
                expiry_parts = expiry_date.split('/')
                if len(expiry_parts) == 2:
                    month, year = expiry_parts
                    if month.isdigit() and year.isdigit():
                        month = int(month)
                        year = int(year)
                        if month<1 or month>12:
                            print("|----------------------------------------------------------------|")
                            print("|    Invalid format for expiry date. Please use MM/YY format.    |")
                            print("|----------------------------------------------------------------|")
                            self.payment()
                        if year<1:
                            print("|----------------------------------------------------------------|")
                            print("|    Invalid format for expiry date. Please use MM/YY format.    |")
                            print("|----------------------------------------------------------------|")
                            self.payment()

            cvv = input("Enter CVV: ")
            if len(cvv)!=3:
                print("|----------------------------------------------------------------|")
                print(f"|    Invalid CVV...                                              |")
                print("|----------------------------------------------------------------|")
                self.payment()
            try:
                amount = float(input("Enter the payment amount: "))
                if amount<self.final_payment_amt or amount>self.final_payment_amt:
                    print("|----------------------------------------------------------------|")
                    print(f"|    Invalid payment amount...                                   |")
                    print("|----------------------------------------------------------------|")
                    self.payment()
            except Exception as e:
                print("|----------------------------------------------------------------|")
                print(f"   Invalid payment amount: {e} ")
                print("|----------------------------------------------------------------|")
                self.payment()
            print("|----------------------------------------------------------------|")
            print(f"Payment of Rs. {amount} is successfully received by card no. XXXX XXXX XXXX {card_number[-4:]} ")
            print("|----------------------------------------------------------------|")
            self.final_stage()

        else:
            print("|----------------------------------------------------------------|")
            print(f"|    Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.payment()
    

    def total_bill(self):
        total_sum = 0.0
        for key, value in self.selected_items.items():
            total_sum += value
        gst = total_sum * 0.18
        gst=round(gst,2)
        final_amt = total_sum + gst
        self.final_payment_amt = final_amt
        
        with open("TotalBill.txt", "w+") as f:
            f.write("|================================================================|\n")
            f.write("|---------------------------Final Bill---------------------------|\n")
            f.write("|      Product                           Qty        Price        |\n")
            f.write("|                                                                |\n")

            for key, value in self.selected_items.items():
                f.write(f"|     {key:21}      {self.qty[key]:10}       Rs. {float(value)}      |\n")
            
            f.write("|----------------------------------------------------------------|\n")
            f.write(f"|    Total Amount :                               Rs. {total_sum}      |\n")
            f.write("|----------------------------------------------------------------|\n")
            f.write(f"|    GST (18%) :                                  Rs. {gst}      |\n")
            f.write("|----------------------------------------------------------------|\n")
            f.write(f"|    Final Payable Amount :                       Rs. {final_amt}      |\n")
            f.write("|================================================================|\n")
            f.write("|---------------------------Thank You----------------------------|\n")
            f.write("|================================================================|\n")
        print("|----------------------------------------------------------------|")
        print("|    Bill generated and saved in TotalBill.txt successfully...   |")
        print("|----------------------------------------------------------------|")
        self.final_address()
        

    def final_address(self):
        un=""
        pw=""
        z=str(input(" Select Your Final Delivery Location (Home/Office/Other) : "))
        obj_address=user_account(un,pw)
        if(z.lower()=="home"):
            home_address = obj_address.address.get("Home")
            if home_address:
                print("|----------------------------------------------------------------|")
                print(f"|   Home : {home_address:54} |")
                print("|----------------------------------------------------------------|")
                self.payment()
            else:
                print("|----------------------------------------------------------------|")
                print("|   Home address not found.                                      |")
                print("|----------------------------------------------------------------|")
                self.final_address()
                
        elif(z.lower() == "office"):
            office_address = obj_address.address.get("Office")
            if office_address:
                print("|----------------------------------------------------------------|")
                print(f"|   Office : {office_address:53}|")
                print("|----------------------------------------------------------------|")
                self.payment()
            else:
                print("|----------------------------------------------------------------|")
                print("|   Office address not found.                                    |")
                print("|----------------------------------------------------------------|")
                self.final_address()

        elif(z.lower() == "other"):
            other_address = obj_address.address.get("Other")
            if other_address:
                print("|----------------------------------------------------------------|")
                print(f"|   Other : {other_address:54}|")
                print("|----------------------------------------------------------------|")
                self.payment()
            else:
                print("|----------------------------------------------------------------|")
                print("|   Other address not found.                                     |")
                print("|----------------------------------------------------------------|")
                self.final_address()
        else:
            print("|----------------------------------------------------------------|")
            print(f"|   Invalid choice...                                           |")
            print("|----------------------------------------------------------------|")
            self.final_address()

    def display_menu(self):
        print("|================================================================|")
        print("|--------------------------Food Menu-----------------------------|")
        print("|    [1]. Pizza                                                  |")
        print("|    [2]. Burger                                                 |")
        print("|    [3]. Sandwich                                               |")
        print("|    [4]. Thali                                                  |")
        print("|    [5]. Chinese                                                |")
        print("|    [6]. Drinks                                                 |")
        print("|    [7]. snacks                                                 |")
        print("|    [8]. Ice-Cream                                              |")
        print("|    [9]. Dessert                                                |")
        print("|    [10]. Display Total Bill                                    |")
        print("|    [11]. Exit                                                  |")
        print("|================================================================|")
        choose=int(input("Enter your choice: ")) 

        if(choose==1):
            self.pizza_menu()
        
        elif(choose==2):
            self.burger_menu()
        
        elif(choose==3):
            self.sandwich_menu()
        
        elif(choose==4):
            self.thali_menu()
        
        elif(choose==5):
            self.chinese_menu()
        
        elif(choose==6):
            self.drinks_menu()
        
        elif(choose==7):
            self.snacks_menu()
        
        elif(choose==8):
            self.icecream_menu()
        
        elif(choose==9):
            self.dessert_menu()
        
        elif(choose==10):
            self.total_bill()

        elif(choose==11):
            print("|================================================================|")
            print("|    Thank You...                                                |")
            print("|================================================================|")
            exit()

        else:
            print("|================================================================|")
            print("|    Invalid choice...                                           |")
            print("|================================================================|")
            self.display_menu()

start=Display()
start.display_account()
obj=FoodMenu()
obj.display_menu()