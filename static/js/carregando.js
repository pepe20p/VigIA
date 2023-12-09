function redirecionar() {
    window.location.href = "{% load static %}";
  }
  window.onload = setTimeout(redirecionar, 20000);