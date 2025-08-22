# FastAPI CRUD Ansible bilan o'rnatish

## Ta'rif
Loyiha FastAPI CRUD endpointlarini yaratadi, PostgreSQL DB ni Alembic migratsiyalari bilan ishlatadi va local va remote serverlar orasida replikatsiyani Ansible orqali o'rnatadi.

## Struktura
```
fastapi_crud_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   ├── ansible.cfg
│   └── group_vars/
│       └── all/
│           └── vault.yml (shifrlangan)
├── alembic.ini
├── requirements.txt
└── README.md
```

## O'rnatish
1. Ansible va bog'liqliklarni o'rnating.
2. `group_vars/all/vault.yml` ni yarating, sirlarni (db_pass, ssh_pass, repl_pass) kiriting va `ansible-vault` bilan shifrlang.
3. inventory.ini da remote IP ni yangilang.
4. Ishga tushiring: `ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --vault-id @prompt --ask-become-pass`.

## Foydalanish
- Local FastAPI: app_dir dan `uvicorn app.main:app --reload` ni ishga tushiring.
- CRUD endpointlarini `/items/` da sinab ko'ring.

## Eslatmalar
- PostgreSQL porti: 5433.
- Replikatsiya: Localdan remote ga streaming.
- Sirlarni vault bilan himoyalang.

## Bosqichma-bosqich ketma-ketlik (foydalanuvchilar uchun):
1. GitHubdan repository ni clone qiling: `git clone https://github.com/usmanovabdulaziz/ansible_fastapi_crud.git`.
2. Project papkasiga o'ting: `cd ansible_fastapi_crud`.
3. Virtual muhit yarating va faollashtiring: `python3 -m venv venv && source venv/bin/activate`.
4. Bog'liqliklarni o'rnating: `pip install -r requirements.txt`.
5. Ansible vault faylini yarating va sirlarni kiriting: `ansible-vault create ansible/group_vars/all/vault.yml` (db_pass, ssh_pass, repl_pass qo'shing).
6. inventory.ini da remote server IP va foydalanuvchini yangilang.
7. Playbook ni ishga tushiring: `ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --vault-id @prompt --ask-become-pass`.
8. Localda app ni ishga tushiring: `cd /opt/fastapi_crud && venv/bin/uvicorn app.main:app --reload`.
9. Remote da shunday tekshiring.
