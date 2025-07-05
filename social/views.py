from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario

def feed(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'social/feed.html', {'posts': posts})

def novo_post(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        mensagem = request.POST.get('mensagem')
        imagem = request.FILES.get('imagem')
        Post.objects.create(nome=nome, mensagem=mensagem, imagem=imagem)
        return redirect('social_feed')
    return render(request, 'social/novo_post.html')

def novo_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        comentario = request.POST.get('comentario')
        Comentario.objects.create(post=post, nome=nome, comentario=comentario)
        return redirect('social_feed')
    return render(request, 'social/novo_comentario.html', {'post': post})