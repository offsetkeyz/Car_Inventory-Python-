class Car:
    # Final Variables
    new_car_income = 2.75
    used_21to24_income = 5.00
    used_24to27_income = 5.50
    video_income = 3.00

    # Constructor
    def __init__(self, stock_number, customer_name, car_make, car_model, car_year, num_pics, new_or_used):
        self.stock_number = stock_number
        self.customer_name = customer_name
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.num_pics = num_pics
        self.new_or_used = new_or_used

    def calculate_income(self):
        income = 0.0
        return income

    def get_stock_number(self):
        return self.stock_number

    # To String method
    def __str__(self) -> str:
        return f"Stock Number: {self.stock_number}"

    # Equals Method
    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)
