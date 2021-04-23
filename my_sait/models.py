from django.db import models
from datetime import datetime


class Items(models.Model):
	"""Предметы"""
	name = models.CharField("Название предмета", max_length=150)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Предмет"
		verbose_name_plural = 'Предметы'


class Lectures(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='lectures')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Лекция"
		verbose_name_plural = 'Лекции'


class Practices(models.Model):
	"""Практики"""
	file = models.FileField("Файл", upload_to='practices')
	name = models.CharField("Имя практики", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Практика"
		verbose_name_plural = 'Практики'


class Groups(models.Model):
	"""Группы"""
	code = models.IntegerField("Код группы", default=None)

	def __str__(self):
		return self.code

	class Meta:
		verbose_name = "Группа"
		verbose_name_plural = 'Группы'


class Users(models.Model):
	"""Пользователи"""
	name = models.CharField("Имя пользователя", max_length=30, default=None)
	surname = models.CharField("Фамилия пользователя", max_length=30)
	group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.PROTECT)
	login = models.CharField("Логин пользователя", max_length=30)
	password = models.CharField("Пароль пользователя", max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = 'Пользователи'


class Marks(models.Model):
	"""Календарь"""
	date = models.DateField('Дата')
	items_code = models.ForeignKey(Items, verbose_name="Предмет", on_delete=models.CASCADE)
	group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.PROTECT)
	users_code = models.ForeignKey(Users, verbose_name="Код пользователя", on_delete=models.CASCADE)
	mark = models.IntegerField('Оценка')

	def __str__(self):
		return str(self.date)

	class Meta:
		verbose_name = "Календарь"
		verbose_name_plural = 'Календарь'
