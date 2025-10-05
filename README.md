# Ex.05 Design a Website for Server Side Processing
## Date:05.10.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Incandescent Bulb Power Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #f9f9f9; }
        input, button { padding: 10px; margin: 10px; font-size: 16px; }
        .result { margin-top: 20px; font-weight: bold; font-size: 20px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Incandescent Bulb Power Calculator</h1>
    <form method="post">
        {% csrf_token %}
        <label>Voltage (V): </label>
        <input type="text" name="voltage" value="{{ voltage }}"><br>
        <label>Current (I): </label>
        <input type="text" name="current" value="{{ current }}"><br>
        <label>Resistance (R): </label>
        <input type="text" name="resistance" value="{{ resistance }}"><br>
        <button type="submit">Calculate Power</button>
    </form>

    {% if power %}
        <div class="result">Power of the filament: {{ power|floatformat:2 }} W</div>
    {% elif error_message %}
        <div class="error">{{ error_message }}</div>
    {% endif %}
</body>
</html>

views.py

# mathapp/views.py
from django.shortcuts import render

def calculate_power(request):
    power = None
    error_message = None

    if request.method == "POST":
        voltage = request.POST.get('voltage')
        current = request.POST.get('current')
        resistance = request.POST.get('resistance')

        try:
            V = float(voltage) if voltage else None
            I = float(current) if current else None
            R = float(resistance) if resistance else None

            if I is not None and R is not None:
                power = I**2 * R
            elif V is not None and R is not None:
                power = V**2 / R
            elif V is not None and I is not None:
                power = V * I
            else:
                error_message = "Please provide at least two values."

        except ValueError:
            error_message = "Please enter valid numbers."

    context = {
        'power': power,
        'error_message': error_message,
        'voltage': request.POST.get('voltage', ''),
        'current': request.POST.get('current', ''),
        'resistance': request.POST.get('resistance', ''),
    }

    # Include the app name in the template path
    return render(request, 'mathapp/math.html', context)


urls.py

"""
URL configuration for abi project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', views.calculate_power, name='calculate_power'),
]


```

## SERVER SIDE PROCESSING:
![alt text](<bharath/mathapp/Screenshot 2025-10-05 104957.png>)

## HOMEPAGE:
![alt text](<bharath/mathapp/Screenshot (23).png>)

## RESULT:
The program for performing server side processing is completed successfully.
