from django.db import models


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
	file = models.FileField("Лекции")
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Лекция"
		verbose_name_plural = 'Лекции'


class Practices(models.Model):
	"""Практики"""
	file = models.FileField("Практики")
	name = models.CharField("Имя практики", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Практика"
		verbose_name_plural = 'Практики'


class Users(models.Model):
	"""Пользователи"""
	name = models.CharField("Имя пользователя", max_length=30, default=None)
	surname = models.CharField("Фамилия пользователя", max_length=30)
	group = models.IntegerField('Группа')
	login = models.CharField("Логин пользователя", max_length=30)
	password = models.CharField("Пароль пользователя", max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = 'Пользователи'


class Calendar(models.Model):
	"""Календарь"""
	date = models.DateField('Дата')
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	mark = models.IntegerField('Оценка')
	users_code = models.ForeignKey(Users, verbose_name="Код пользователя", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.date)

	class Meta:
		verbose_name = "Календарь"
		verbose_name_plural = 'Календарь'
