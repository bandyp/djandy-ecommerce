{"filter":false,"title":"views.py","tooltip":"/accounts/views.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":4,"column":63},"end":{"row":4,"column":97},"action":"remove","lines":[" ProfileUpdateForm, UserUpdateForm"],"id":33},{"start":{"row":4,"column":62},"end":{"row":4,"column":63},"action":"remove","lines":[","]}],[{"start":{"row":65,"column":0},"end":{"row":81,"column":80},"action":"remove","lines":["@login_required","def profile(request):","    if request.method == 'POST':","        u_form = UserUpdateForm(request.POST, instance=request.user)","        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)","        if u_form.is_valid() and p_form.is_valid():","            u_form.username = request.user","            p_form.name = request.user","            u_form.save()","            p_form.save()","        messages.success(request, f\"Your account has been updated\")","        return redirect('profile')","    else:","        u_form = UserUpdateForm(instance=request.user)","        p_form = ProfileUpdateForm(instance=request.user)","        ","    return render(request, 'profile.html', {'p_form': p_form, 'u_form': u_form})"],"id":34}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":65,"column":0},"end":{"row":65,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1582828627141,"hash":"8eb7c8c988160e2d239ec07db8db034c1d3916dd"}