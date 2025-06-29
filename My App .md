food/
list.html (Food menu)
detail.html (Food item details)
add.html (Add new food)
cart/
view.html (View cart)
checkout.html (Checkout)
order/
history.html (Order history)
detail.html (Order details)
account/
login.html (User login)
register.html (User registration)
profile.html (User profile)

========================whene create model========================
   pip install python-dotenv
   
   python manage.py makemigrations
   python manage.py migrate
================ 
   "python -m pip install Pillow"

A Product model (with fields like name, description, price, image, etc.)
A view to fetch and pass product data to the template
A template that loops through products and displays them