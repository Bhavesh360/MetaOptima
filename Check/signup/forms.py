from django import forms
import re

inputname_re = re.compile('^[A-Za-z]+$')  # should contain characters from a-z,A-Z and 0-9 and should be 3-20 characters long.


def valid_name(name):
    return name and inputname_re.match(name)


class NameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required = True)
    inputstring = forms.CharField(label = 'Input String' , max_length = 100, required= True)

    #adding further validations to check if the characters are only lower case and upper case alphabets:
    def clean_name(self):
        cd = self.cleaned_data

        name = cd.get('name')
        if not valid_name(name):
            raise forms.ValidationError("Please enter only uppercase and lowercase alphabets")
        return name

    def clean_inputstring(self):
        cd = self.cleaned_data

        inputstring = cd.get('inputstring')
        if not valid_name(inputstring):
            raise forms.ValidationError("Please enter only uppercase and lowercase alphabets")
        return inputstring

    def clean(self):
        cd = self.cleaned_data
        return cd