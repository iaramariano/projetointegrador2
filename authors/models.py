from django.db import models
class AuthorsMod(models.Model):
    # Metadados
    update_at = models.DateTimeField(auto_now=True, db_column='last_login')
