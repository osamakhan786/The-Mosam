from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get("city", 'lucknow')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=32dc91f6865a372a8ed4750bc583369c'
    data = requests.get(url).json()
    
    payload ={
        'city': data['name'],
        'speed': data['wind']['speed'],
        'weather': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'temperature': int(data['main']['temp']-273),
        'feels_like': int(data['main']['feels_like']-273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'cloud': data['clouds']['all'],
    }
    context = {'data': payload}
    return render(request, 'index.html', context)