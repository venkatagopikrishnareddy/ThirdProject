from django.shortcuts import render
import datetime;
def wishes(request):
    date1=datetime.datetime.now()
    msg1='Hello User...Good';
    hr=int(date1.strftime('%H'));
    imgs='s1.jpeg';
    if hr<12:
        msg1+='Morning.!!'
        imgs='s1.jpeg';
    elif hr<16:
        msg1+='AfterNoon..!!';
        imgs='g1.jpeg';
    elif hr<20:
        msg1+='Evening..!!'
        imgs='bg1.jpg';
    else :
        msg1+='Good Night..!!';
        imgs='s3.jpeg';
    dict={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes.html',context=dict);
# Create your views here.

from django.shortcuts import render
import datetime
def imagesgallery(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imgsgallery.html', context=dict1);



from django.shortcuts import render
import datetime
def hyperlinks(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Hyperlinks***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/hyperlinks.html', context=dict1);


from django.shortcuts import render
import datetime
def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery(Product)***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imggallery2.html', context=dict1);

