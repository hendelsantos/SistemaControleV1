# SistemaControleV1

Sistema web para **controle de demandas e pedidos** de materiais, desenvolvido com Django + Bootstrap.

## Funcionalidades

- Cadastro e gerenciamento de demandas de materiais.
- Tela de pedidos, com vinculação a demandas.
- Filtros inteligentes de busca por ID, solicitante, descrição, catálogo, quantidade, data e etapa.
- Dashboard resumido com status das demandas.
- Tela administrativa via Django Admin.
- Layout responsivo e elegante (Bootstrap 5).

## Tecnologias utilizadas

- Python 3.x
- Django 4.x
- Bootstrap 5
- SQLite3 (banco padrão, fácil de migrar)


## Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. **Crie o ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### Favicon

- O arquivo do favicon deve estar em `static/favicon.png` ou `static/favicon.ico`
- No arquivo `base.html`, já existe a linha:
  ```html
  <link rel="shortcut icon" href="{% static 'favicon.png' %}" type="image/png">
  ```
- Se quiser usar `.ico`, altere para:
  ```html
  <link rel="shortcut icon" href="{% static 'favicon.ico' %}" type="image/x-icon">
  ```