mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
	@echo 'Migrates were done successfully'

su:
	python3 manage.py createsuperuser

