{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":8,"column":0},"end":{"row":19,"column":37},"action":"remove","lines":["def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))"],"id":2},{"start":{"row":8,"column":0},"end":{"row":19,"column":37},"action":"insert","lines":["def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ","","    request.session['cart'] = cart","    return redirect(reverse('index'))"]}],[{"start":{"row":26,"column":7},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":23},"action":"insert","lines":["print(request.POST)"],"id":4}]]},"ace":{"folds":[],"scrolltop":120,"scrollleft":0,"selection":{"start":{"row":26,"column":7},"end":{"row":26,"column":7},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":114,"mode":"ace/mode/python"}},"timestamp":1573503803694,"hash":"d3326822f6f632505cd9e2150b073d8e2e0e7df5"}