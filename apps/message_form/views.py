
from django.shortcuts import render
from apps.message_form.models import Message

def message_form(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message_text", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text

        message.save()

        return render(request,"message_form.html",{"message":message})

    if request.method == "GET":
        var_dict = {}
        all_message = Message.objects.all()
        if all_message: #判断all_message是否存在 暨数据库中是否有数据
            message = all_message[0] #【0】列表中第一个数据
            var_dict = {
                "message":message #前一个message是key 对应html离 后一个message是value
            }

        return render(request,"message_form.html", var_dict)
