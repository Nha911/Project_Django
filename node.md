py -m venv nha
.\nha\Scripts\activate  
pip install django
pip install plilow
django-admin startproject demo_project .
cd demo_project  
python manage.py runserver

===================================
python manage.py startapp my_web_demo
we are change port :
python manage.py runserver 5000
python manage.py runserver 172.20.10.7:8000
python manage.py runserver 192.168.100.193:8000

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


admin
admin

pkay
1

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
git add my_project/static/image/\*
git commit -m "Add static image assets to version control"
git push -u origin main

git add my_project/_
git add my_project/.gitignore
git add my_project/media/product_images/_
git add my_project/static/_
git add my_project/templates/_
git add my_project/management/commands/\*
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

<style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #fff;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 24px 0 0 0;
        }

        .tabs {
            display: flex;
            border-bottom: 1px solid #ccc;
            margin-bottom: 24px;
        }

        .tab {
            flex: 1;
            text-align: left;
            padding: 12px 16px 8px 0;
            font-size: 22px;
            font-weight: bold;
            color: #222;
            cursor: pointer;
            border: none;
            background: none;
            outline: none;
        }

        .tab.active {
            border-bottom: 3px solid #000;
        }

        .close-btn {
            position: absolute;
            right: 24px;
            top: 24px;
            font-size: 28px;
            cursor: pointer;
            color: #000000;
        }

        .form-group {
            margin-bottom: 18px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            color: #444;
            font-size: 16px;
        }

        input[type="text"],
        input[type="password"],
        input[type="email"] {
            width: 100%;
            padding: 12px;
            border: 1px solid #222;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }

        .password-wrapper {
            position: relative;
        }

        .toggle-password {
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
        }

        .btn {
            width: 100%;
            padding: 14px 0;
            background: #000;
            color: #fff;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-bottom: 18px;
        }

        .or {
            text-align: center;
            color: #444;
            margin: 18px 0 12px 0;
            font-size: 18px;
        }

        .facebook-btn {
            width: 100%;
            padding: 12px 0;
            border: 1px solid #222;
            border-radius: 4px;
            background: #fff;
            color: #222;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            cursor: pointer;
        }

        .facebook-btn .fb-icon {
            background: #4267B2;
            color: #fff;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }

        .link {
            color: #222;
            text-decoration: underline;
            cursor: pointer;
            font-size: 16px;
        }

        .center-text {
            text-align: center;
            margin: 18px 0 0 0;
            font-size: 18px;
        }

        .gender-group {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 18px;
        }

        .row {
            display: flex;
            gap: 12px;
        }

        .row .form-group {
            flex: 1;
        }

        select {
            width: 100%;
            padding: 12px;
            border: 1px solid #222;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
            background: #fff;
        }

        @media (max-width: 500px) {
            .container {
                max-width: 100vw;
                padding: 12px 0 0 0;
            }
        }

        .close-btn {
            margin-top: 35px;
            margin-right: 24px;
            color: #000;
            font-size: 32px;
            position: absolute;
            z-index: 1000;
            transition: color 0.3s;

            &:hover {
                color: #f00;
            }
        }
</style>
