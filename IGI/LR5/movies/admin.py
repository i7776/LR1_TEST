from django.contrib import admin
from .models import Genre, Actor, Movie, Hall, Screening, Employee, AboutCompany, FAQ, News, Review, Vacancy, PromoCode, PrivacyPolicy, ContactInfo, Ticket

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Screening)
admin.site.register(Ticket)
admin.site.register(Employee)

admin.site.register(AboutCompany)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(Review)
admin.site.register(Vacancy)
admin.site.register(PromoCode)
admin.site.register(ContactInfo)
admin.site.register(PrivacyPolicy)

