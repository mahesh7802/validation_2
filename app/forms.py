from django import forms

def validate_name(value):
    if not value[0].isupper():
        raise forms.ValidationError('name should startwith capitals')
    
def validation_length(value):
    if len(value)<5:
        raise forms.validationError('length is to short')
    
def validate_age(value):
    if value<18:
        raise forms.ValidationError('age should be greate than 18')

class Student_Form(forms.Form):
    sname=forms.CharField(max_length=100)   
    sage=forms.IntegerField()
    semail=forms.EmailField()

    
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']

        if e != re:
            raise forms.ValidationError('emails not matched')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')

