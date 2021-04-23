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


class TrpoLectures(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='trpo/lectures')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ТРПО Лекция"
		verbose_name_plural = 'ТРПО Лекции'


class PP0201Lectures(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='pp0201/lectures')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПП.02.01. Лекция"
		verbose_name_plural = 'ПП.02.01. Лекции'


class PP0102Lectures(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='pp0102/lectures')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПП.01.02. Лекция"
		verbose_name_plural = 'ПП.01.02. Лекции'


class TrpoPractices(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='trpo/practices')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ТРПО Практика"
		verbose_name_plural = 'ТРПО Практики'


class PP0201Practices(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='pp0201/practices')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПП.02.01. Практика"
		verbose_name_plural = 'ПП.02.01. Практики'


class PP0102Practices(models.Model):
	"""Лекции"""
	file = models.FileField("Файл", upload_to='pp0102/practices')
	name = models.CharField("Имя лекции", max_length=100)
	items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
	date = models.DateField('Дата')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПП.01.02. Практика"
		verbose_name_plural = 'ПП.01.02. Практики'


class Groups(models.Model):
	"""Группы"""
	code = models.IntegerField("Код группы", default=None)

	def __str__(self):
		return str(self.code)

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
		verbose_name = "Оценка"
		verbose_name_plural = 'Оценки'
