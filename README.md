## Como rodar o projeto?
1. Clone esse repositório. 
2. Crie um virtualenv com Python 3.
3. Ative o virtualenv.
3. Instale as dependências.
4. Rode as migrações.


* git clone https://github.com/Madusalves/Estoque.git
* cd Estoque
* python3 -m venv .venv
* source .venv/bin/activate
* pip install -r requirements.txt
* python contrib/env_gen.py
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
