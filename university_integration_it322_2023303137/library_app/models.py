from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10)
    borrowed_on = models.DateField(auto_now_add=True)
    returned_on = models.DateField(null=True, blank=True)

class LibraryRecord(models.Model):
    student_id = models.CharField(max_length=10)
    has_fines = models.BooleanField(default=False)
    amount_due = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
