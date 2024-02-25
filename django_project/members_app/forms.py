from django import forms


class My_Forms(forms.Form):
	name = forms.CharField(label="Your name", required=False, max_length=20)
	text = forms.CharField(label="Your text", widget=forms.Textarea)
	age = forms.IntegerField(min_value=12, max_value=120, label='Your age')


	# def clean_name(self, name):
	# 	name = self.cleaned_data.get("name")
	# 	if len(name) < 4:
	# 		raise forms.ValidationError("Name must be at least 3 characters long.")
	# 	return name

