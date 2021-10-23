from django import forms
from .models import ItemName

class NewItemForm(forms.ModelForm):
    contact_person1 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id':'person1',
        'class':'form-control',
        'placeholder':'Example*** Azam',        
    }))
    contact_number1 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Example*** 33 233 13 23',        
    }))
    teaching_subject = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Example*** Rus tili',                
    }))
    center_or_teacher_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Example*** Learning Center',                
    }))
    about = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'id':'area',
        'style':'height: 130px;',
        'class':'form-control',
        'placeholder':'Example*** Xaqida',
    }))
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id':'name',
        'class':'form-control',
        'placeholder':'Example*** exampleThing',
    }))
    work_type = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id':'type',
        'class':'form-control',
        'placeholder':'Example*** Benzapila Xizmati',
    }))
    campany_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id':'cam_name',
        'class':'form-control',
        'placeholder':'Example*** "exampleCampany"',
    }))
    ijara_turi = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'id':'iname',
        'class':'form-control',
        'placeholder':'Example*** Avtomobile',
    }))
    class Meta:
        model = ItemName
        fields = ['name', 'ijara_turi','campany_name','category', 'work_type', 'narx', 'image', 'region', 'contact_person', 'contact_number','contact_person1', 'contact_number1', 'about', 'teaching_subject', 'center_or_teacher_name', ]
        widgets = {
            'narx':forms.TextInput(attrs={
                'id':'narx',
                'class':'form-control',
                'placeholder':'Example*** 800 000',
            }),
            'image':forms.FileInput(attrs={
                'id':'img',
                'class':'form-control',
            }),
            'category':forms.Select(attrs={
                'id':'group',
                'class':'form-select',
            }),
            'region':forms.TextInput(attrs={
                'id':'region',
                'class':'form-control',
                'placeholder':'Example*** Andijon',
            }),
            'contact_person':forms.TextInput(attrs={
                'id':'person',
                'class':'form-control',
                'placeholder':'Example*** Murod',
            }),
            'contact_number':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Example*** 91 626 16 76',
            }),
        }

class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id':'fname',
        'placeholder':'name',
        'class':'form-control',
    }) , max_length=150)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id':'lname',
        'class':'form-control',
        'placeholder':'name2',
    }) , max_length=150)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'id':'email',
        'class':'form-control',
        'placeholder':'email',
    }) , max_length=150)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'id':'area',
        'class':'form-control',
        'placeholder':'messages',
        'style':'height:150px;'
    }), max_length=2000)