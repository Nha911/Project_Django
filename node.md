py -m venv nha
.\nha\Scripts\activate  
pip install django
django-admin startproject demo_project .
cd demo_project  
python manage.py runserver

===================================
python manage.py startapp my_web_demo
we are change port :
python manage.py runserver 5000
python manage.py runserver 172.20.10.7:8000

===================================
npm install tailwindcss @tailwindcss/cli
@import "tailwindcss";
npx @tailwindcss/cli -i ./src/style/input.css -o ./src/style/output.css --watch

===================================
pip install python-dotenv
urls.py : path('', include('my_web_app.urls')),
Create Admin
python manage.py migrate
python my_project/manage.py migrate
python manage.py createsuperuser
input name
input email
input passwd
done
python my_project/manage.py runserver run one more

panha
1

===================================
python manage.py makemigrations my_web_app
python manage.py migrate

===================================
|default:'https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=

===================================
git add .
git commit -m "Update project files"
git push -u origin main
===================================
git pull origin main --allow-unrelated-histories
git commit -am "Merge branch 'main' of https://github.com/Nha911/Project_Django"
git push -u origin main
=======================================
git add my_project/static/image/*
git commit -m "Add static image assets to version control"
git push -u origin main

git add my_project/*
git add my_project/.gitignore
git add my_project/media/product_images/*
git add my_project/static/*
git add my_project/templates/*
git add my_project/management/commands/*
git status
===================================

            {% if product.image %}
                <div class="mb-2">
                    <img class="card-img-top p-2" style="height:250px;object-fit:contain;" src="{{ product.image.url }}" alt="product image" />
                </div>
            {% else %}
                {% with product.images.all|first as img %}
                    {% if img %}
                        <div class="mb-2">
                            <img class="card-img-top p-2" style="height:250px;object-fit:contain;" src="{{ img.image_url }}" alt="product image" />
                        </div>
                    {% else %}
                        <div class="mb-2">
                            <img class="card-img-top p-10" style="height:180px;object-fit:contain;" src="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=" alt="product image" />
                        </div>
                    {% endif %}
                {% endwith %}
            {% endif %}
===================================
<!-- <script>
function showPasswordPrompt() {
  setTimeout(function() {
    var password = window.prompt("Enter admin password to add product:");
    if (password === "2005") {
      window.location.href = "{% url 'add_product' %}";
    } else if (password !== null) {
      window.alert("Access denied! Only admin can add products.");
    }
  }, 100);
}
</script> -->
===================================
<script>
// MD5 hash of "2005" = 310dcbbf4cce62f762a2aaa148d556bd
const ADMIN_PASSWORD_HASH = "310dcbbf4cce62f762a2aaa148d556bd";

function showPasswordPrompt(url, action) {
    event.preventDefault();
    
    const actionText = {
        'add': 'add product',
        'edit': 'edit product', 
        'delete': 'delete product'
    }[action] || 'perform this action';
    
    const password = window.prompt(`Enter admin password to ${actionText}:`);
    
    if (password !== null) {
        // Compare MD5 hashes instead of plain text
        if (md5(password) === ADMIN_PASSWORD_HASH) {
            window.location.href = url;
        } else {
            window.alert("Access denied! Only admin can " + actionText + ".");
        }
    }
}
</script>

===================================

ORM IS 


python manage.py shell