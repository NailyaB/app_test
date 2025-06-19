import streamlit as st
import math

def find_root(a, b, c):
    # Решение квадратного уравнения ax^2 + bx + c = 0
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Корней нет"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Один корень: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Два корня: {root1} и {root2}"

st.title('Нахождение корня квадратного уравнения')
a = st.number_input('Введите коэффициент a', value=1.0)
b = st.number_input('Введите коэффициент b', value=0.0)
c = st.number_input('Введите коэффициент c', value=0.0)

result = find_root(a, b, c)
st.write(result)

