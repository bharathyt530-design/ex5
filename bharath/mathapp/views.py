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