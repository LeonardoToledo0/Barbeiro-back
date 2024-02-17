from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ClienteManager(BaseUserManager):
    def create_user(self, email, telefone, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O endereço de e-mail deve ser fornecido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, telefone=telefone, nome=nome, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, telefone, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, telefone, nome, senha, **extra_fields)

class Cliente(AbstractBaseUser):
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)  # Você pode ajustar o comprimento conforme necessário
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)
    ultimas_compras = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClienteManager()

    # USERNAME_FIELD é usado para fazer login (no lugar do username)
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS são os campos obrigatórios ao criar um superusuário pelo comando createsuperuser
    REQUIRED_FIELDS = ['telefone', 'nome']

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cliente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    horario = models.DateTimeField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva para {self.cliente.nome} em {self.horario.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['horario']

class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagem1 = models.ImageField(upload_to='galeria/', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='galeria/', null=True, blank=True)
    imagem3 = models.ImageField(upload_to='galeria/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    

class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.titulo
