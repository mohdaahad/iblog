from django.shortcuts import render, get_object_or_404

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})    


 <a href=""><i class="material-icons">&#xe7f4;</i></a>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <div class="row"> <span class=""> <img src="{% static 'app/img/tint1.jpg' %}" class="rounded-circle " style="width: 40px;" alt="">
              </a><ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                {% for cat in cats %}
              <a class="dropdown-item" href="/category/{{cat.url}}">{{cat.title}}</a>
              {% endfor %}
               
              </ul>
          </li>



<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0" allowfullscreen></iframe>
</div>