import sqlite3
from PIL import Image
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PostForm, AnswerForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Answer

#главная страница
def main_view(request):
    sort_by = request.GET.get('sort_by', '-created_at')  # По умолчанию сортируем по дате создания (новые вопросы сверху)
    search_query = request.GET.get('search', '')  # Получаем поисковый запрос из параметра 'search' или пустую строку, если параметр не указан
    questions = Post.objects.filter(title__icontains=search_query).order_by(sort_by)
    context = {'questions': questions, 'sort_by': sort_by, 'search_query': search_query}
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context['page'] = page
    return render(request, 'main.html', context)

#меню
def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

#вопросы
def questions_view(request):
    return render(request, 'questions.html')

def question_detail(request, post_id):
    question = get_object_or_404(Post, pk=post_id)
    return render(request, 'question_detail.html', {'question': question})

def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if answer.is_deleted:
        answer.delete()
    else:
        answer.is_deleted = True
        answer.save()
    return redirect(reverse('question_detail', kwargs={'post_id': answer.post_id}))

def edit(request, question_id, answer_id):
    try:
        answer = Answer.objects.get(id=answer_id)
        if request.method == 'POST':
            answer.content = request.POST.get("content")
            answer.save()
            return redirect(reverse('question_detail', kwargs={'post_id': answer.post_id}))
        else:
            return render(request, 'edit.html', {'answer': answer})
    except Answer.DoesNotExist:
        return HttpResponseNotFound("<h2>Answer not found</h2>")

def answer_view(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect(reverse('question_detail', kwargs={'post_id': post_id}))
    else:
        form = AnswerForm()

    return render(request, 'answer.html', {'form': form, 'post': post})

#добавить вопрос
def post_view(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.save()
            return redirect('main')
        else:
            print(form.errors)  # Вывод ошибок формы в консоль
            messages.error(request, 'Ошибка при создании поста.')  # Отображение сообщения об ошибке пользователю
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form, 'posts': posts})