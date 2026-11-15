from django import forms

COMUNA_CHOICES = [
    ('Cerrillos', 'Cerrillos'),
    ('Cerro Navia', 'Cerro Navia'),
    ('Conchalí', 'Conchalí'),
    ('El Bosque', 'El Bosque'),
    ('Estación Central', 'Estación Central'),
    ('Huechuraba', 'Huechuraba'),
    ('Independencia', 'Independencia'),
    ('La Cisterna', 'La Cisterna'),
    ('La Florida', 'La Florida'),
    ('La Granja', 'La Granja'),
    ('La Pintana', 'La Pintana'),
    ('La Reina', 'La Reina'),
    ('Las Condes', 'Las Condes'),
    ('Lo Barnechea', 'Lo Barnechea'),
    ('Lo Espejo', 'Lo Espejo'),
    ('Lo Prado', 'Lo Prado'),
    ('Macul', 'Macul'),
    ('Maipú', 'Maipú'),
    ('Ñuñoa', 'Ñuñoa'),
    ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'),
    ('Peñalolén', 'Peñalolén'),
    ('Providencia', 'Providencia'),
    ('Pudahuel', 'Pudahuel'),
    ('Quilicura', 'Quilicura'),
    ('Quinta Normal', 'Quinta Normal'),
    ('Recoleta', 'Recoleta'),
    ('Renca', 'Renca'),
    ('San Joaquín', 'San Joaquín'),
    ('San Miguel', 'San Miguel'),
    ('San Ramón', 'San Ramón'),
    ('Santiago', 'Santiago'),
    ('Vitacura', 'Vitacura'),
]

TIPO_CHOICES = [
    ('Universidad', 'Universidad'),
    ('Recreativo', 'Recreativo'),
    ('Comercio', 'Comercio'),
    ('Cultural', 'Cultural'),
    ('Miscelaneo', 'Miscelaneo'),
]

class InterestLocationForm(forms.Form):
    add_lugar_nombre = forms.CharField(max_length=50)
    add_lugar_tipo = forms.ChoiceField(choices=TIPO_CHOICES)
    add_lugar_comuna = forms.ChoiceField(choices=COMUNA_CHOICES)
    
    add_lugar_encontrar = forms.CharField(max_length=200)
    add_lugar_razon = forms.CharField(max_length=200)
    
    lat = forms.FloatField()
    lng = forms.FloatField()