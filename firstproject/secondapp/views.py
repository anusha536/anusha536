from django.shortcuts import render,redirect
from secondapp.models import Author,Book
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'registration.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('book_aut')
        else:
            return HttpResponse('Invalid credentials')
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')


def insertauthor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Author.objects.create(auth_name=name)
        return HttpResponse('Author Added Successfully')

    return render(request, 'author.html')



def insertbook(request):
    if request.method == 'POST':
        name = request.POST.get('book_name')
        author_name = request.POST.get('author')
        price = request.POST.get('book_price')

        authors = Author.objects.create(auth_name=author_name)

        Book.objects.create(book_name=name, author=authors, book_price=price)

        return HttpResponse('Book Added Successfully')

    return render(request, 'book.html')

def author(request):
    bk = Book.objects.all()
    au = Author.objects.all()
    di = {'bk': bk, 'au': au}
    return render(request,'author2.html',di)

def edit_data(request,id):
    da = Author.objects.get(id = id)
    di={'da':da}
    if request.method=='POST':
        da.auth_name=request.POST.get('auth_name')
        da.save()
        return redirect('book_aut')
    return render(request,'edit_data.html',di)
def delete_data(request,id):
    da=Author.objects.get(id=id)
    da.delete()
    return redirect(author)

def book(request):
    bk=Book.objects.all()
    au=Author.objects.all()
    di={'bk':bk,'au':au}

    return render(request,'author2.html',di)

def edit(request,id):
    au = Author.objects.all()
    da=Book.objects.get(id = id)
    di={'da':da}
    if request.method=='POST':
        book.book_name=request.POST.get('book_name')
        auth_name=request.POST.get('author')
        authors=Author.objects.get(auth_name=auth_name)
        da.author=authors
        da.book_price=request.POST.get('book_price')
        da.save()
        return redirect(book)
    return render(request,'book_edit.html',di)

def delete(request,id):
    da=Book.objects.get(id=id)
    da.delete()
    return redirect(book)