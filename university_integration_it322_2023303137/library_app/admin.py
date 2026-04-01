from django.contrib import admin
from .models import Book, BorrowRecord, LibraryRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    list_filter = ("published_date",)
    search_fields = ("title", "author")

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ("book", "student_id", "borrowed_on", "returned_on")
    list_filter = ("borrowed_on", "returned_on")
    search_fields = ("student_id", "book__title", "book__author")

@admin.register(LibraryRecord)
class LibraryRecordAdmin(admin.ModelAdmin):
    list_display = ("student_id", "has_fines", "amount_due")
    list_filter = ("has_fines",)
    search_fields = ("student_id",)
