## Data Analysis and Visualisations in Django | Pandas | Matplotlib | base64

### Installations
pip django install pillow django-crispy-forms matplotlib pandas seaborn xhtml2pdf

pip install crispy-bootstrap4

inside settings.py in the main app add 
INSTALLED_APPS = [ 
    ... 
    'crispy_forms', 
    'crispy_bootstrap4', 
    ... 
] 

CRISPY_TEMPLATE_PACK = 'bootstrap4' 

inside your_html.html file add 
{% load crispy_forms_tags %} 
