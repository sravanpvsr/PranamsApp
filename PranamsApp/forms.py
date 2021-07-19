from django import forms
from django.core.validators import EMPTY_VALUES

#from django.utils.safestring import mark_safe
import re

from PranamsApp.models import Member_Category_Master,Institution_Master,Sub_Division_Master,Institution_Sub_Division_Map,Room_Type_Master,Room_Master,Gate_Master,add_demography,add_vehicle,add_maid,add_emergency,add_maintenance
from PranamsApp.serializers import Member_Category_Master_Serializer,Institution_Master_Serializer,Sub_Division_Master_Serializer,Institution_Sub_Division_Map_Serializer,Room_Type_Master_Serializer,Room_Master_Serializer,Gate_Master_Serializer

class add_demography_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Room'].required = False
        # self.fields['Room_Type'].required = False
        # self.fields['Institution_Name'].required = False
        # self.fields['Sub_Division_Name'].required = False
        # self.fields['Staff_Working_Since'].required = False
        # self.fields['Staff_Designation'].required = False
        # self.fields['Staff_Institution_Emp_ID'].required = False
        # self.fields['Member_Whatsapp'].required = False
        # self.fields['Member_DL_No'].required = False
        # self.fields['Member_DL_Validity'].required = False
        # self.fields['Address_Outside_PSN'].required = False

    class Meta:
        model=add_demography
        exclude=["Updated_Date","Updated_By","Status","Member_Occupant",
        "Relationship_With_Primary_Member","Permanent_Resident_Or_Not"]
        #widgets = {'Staff_Working_Since': forms.HiddenInput()}

    CHOICES = (
        ('--','--'),
        ('yes','Yes'),
        ('no','No')
    )
    # class HorizontalRadioRenderer(forms.RadioSelect):
    #     def render(self):
    #         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
    
    Whatsapp_Choice = forms.ChoiceField(label="Does the above no. have Whatsapp?",choices=CHOICES) 
    # DATE_INPUT_FORMATS = ['%d-%m-%Y']
    # DOB = forms.DateField(label='Date of Birth', input_formats= DATE_INPUT_FORMATS)
    # Staff_Working_Since =forms.DateField(input_formats= DATE_INPUT_FORMATS)

    # Staff_Choice = forms.ChoiceField(label="Is the member a Staff?",choices=CHOICES, 
    #         widget=forms.RadioSelect()) 
    # this function will be used for the validation
    def clean(self):
        super(add_demography_form, self).clean()
        
        Member_Name=self.cleaned_data.get('Name')
        Member_Mobile=self.cleaned_data.get('Mobile')
        #Member_Whatsapp=self.cleaned_data.get('Member_Whatsapp') #+,d
        Staff_Designation=self.cleaned_data.get('Staff_Designation')
        Staff_Institution_Emp_ID=self.cleaned_data.get('Staff_Institution_Emp_ID')
        Member_Aadhaar_ID=self.cleaned_data.get('Aadhaar_ID')
        #Member_DL_No=self.cleaned_data.get('Member_DL_No')
        Address_Outside_PSN=self.cleaned_data.get('Address_Outside_PSN')
        Email=self.cleaned_data.get('Email')
        # Emergency_Contact_Name=self.cleaned_data.get('Emergency_Contact_Name')
        # Emergency_Contact_Email=self.cleaned_data.get('Emergency_Contact_Email')
        # #Emergency_Contact_ISD=self.cleaned_data.get('Emergency_Contact_ISD')
        # #Emergency_Contact_Mobile_No=self.cleaned_data.get('Emergency_Contact_Mobile_No')
        # Emergency_Contact_Address=self.cleaned_data.get('Emergency_Contact_Address')
        
        Member_Category=self.cleaned_data['Category']




        # conditions to be met for the username length
        # if len(str(Member_Mobile)) != 10:
        #     self._errors['Member_Mobile'] = self.error_class([
        #         'Mobile Number should contain 10 digits'])
        
        
        # if len(str(Address_Outside_PSN)) < 50:
        #     self._errors['Address_Outside_PSN'] = self.error_class([
        #         'Minimum length is 50 characters'])
        
        # if len(str(Emergency_Contact_Address)) < 50:
        #     self._errors['Emergency_Contact_Address'] = self.error_class([
        #         'Minimum length is 50 characters'])

        # if len(str(Member_Aadhaar_ID)) != 12:
        #     self._errors['Member_Aadhaar_ID'] = self.error_class([
        #         'Aadhaar Number should contain 12 digits'])
        
        if not Member_Name.replace(" ", "").isalpha():
            self._errors['Member_Name'] = self.error_class([
                'Please enter a valid name'])
        # if not Emergency_Contact_Name.replace(" ", "").isalpha():
        #     self._errors['Emergency_Contact_Name'] = self.error_class([
        #         'Please enter a valid name'])
        
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if (not re.search(email_regex, Email)):
            self._errors['Email'] = self.error_class([
                'Please enter a valid Email ID'])
        # if(Staff_Designation):
        #     if not Staff_Designation.replace(" ", "").isalnum():
        #         self._errors['Staff_Designation'] = self.error_class([
        #             'Please enter a valid designation'])
        # if(Staff_Institution_Emp_ID):
        #     if not Staff_Institution_Emp_ID.replace(" ", "").isalnum():
        #         self._errors['Staff_Institution_Emp_ID'] = self.error_class([
        #             'Please enter a valid Employee Number'])
        # if(Member_DL_No):
        #     if not Member_DL_No.replace(" ", "").isalnum():
        #         self._errors['Member_DL_No'] = self.error_class([
        #             'Please enter a valid DL Number'])

                
        # return any errors if found
        return self.cleaned_data

class add_occupant_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model=add_demography
        exclude=["Updated_Date","Updated_By","Status","Occ_ID",
        "Room_Type","Address_Outside_PSN","Landline_Number"]


    CHOICES = (
        ('yes','Yes'),
        ('no','No')
    )
    # DATE_INPUT_FORMATS = ['%d-%m-%Y']
    # DOB = forms.DateField(label='Date of Birth', 
    #     input_formats= DATE_INPUT_FORMATS)
    # Staff_Working_Since =forms.DateField(input_formats= DATE_INPUT_FORMATS)





    # class HorizontalRadioRenderer(forms.RadioSelect):
    #     def render(self):
    #         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
    
    # Whatsapp_Choice = forms.ChoiceField(label="Does the above no. have Whatsapp?"#,choices=CHOICES
    # ) 

    # Staff_Choice = forms.ChoiceField(label="Is the occupant a Staff?"#,choices=CHOICES 
    #          ) 
    # this function will be used for the validation
    def clean(self):
        super(add_occupant_form, self).clean()
        
        Name=self.cleaned_data.get('Name')
        Mobile=self.cleaned_data.get('Mobile')
        #Member_Whatsapp=self.cleaned_data.get('Member_Whatsapp') #+,d
        Staff_Designation=self.cleaned_data.get('Staff_Designation')
        Staff_Institution_Emp_ID=self.cleaned_data.get('Staff_Institution_Emp_ID')
        Aadhaar_ID=self.cleaned_data.get('Aadhaar_ID')
        #Member_DL_No=self.cleaned_data.get('Member_DL_No')
        Emergency_Contact_Name=self.cleaned_data.get('Emergency_Contact_Name')
        Emergency_Contact_Email=self.cleaned_data.get('Emergency_Contact_Email')
        #Emergency_Contact_ISD=self.cleaned_data.get('Emergency_Contact_ISD')
        #Emergency_Contact_Mobile_No=self.cleaned_data.get('Emergency_Contact_Mobile_No')
        Emergency_Contact_Address=self.cleaned_data.get('Emergency_Contact_Address')



        # conditions to be met for the username length
        # if len(str(Mobile)) != 10:
        #     self._errors['Mobile'] = self.error_class([
        #         'Mobile Number should contain 10 digits'])
        
    
        
        # if len(str(Emergency_Contact_Address)) < 50:
        #     self._errors['Emergency_Contact_Address'] = self.error_class([
        #         'Minimum length is 50 characters'])

        # if len(str(Aadhaar_ID)) != 12:
        #     self._errors['Aadhaar_ID'] = self.error_class([
        #         'Aadhaar Number should contain 12 digits'])
        # if(Name):
        #     if not Name.replace(" ", "").isalpha():
        #         self._errors['Name'] = self.error_class([
        #             'Please enter a valid name'])
        # if(Emergency_Contact_Name):
        #     if not Emergency_Contact_Name.replace(" ", "").isalpha():
        #         self._errors['Emergency_Contact_Name'] = self.error_class([
        #             'Please enter a valid name'])
        
        # email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        # if(Emergency_Contact_Email):
        #     if (not re.search(email_regex, Emergency_Contact_Email)):
        #         self._errors['Emergency_Contact_Email'] = self.error_class([
        #             'Please enter a valid Email ID'])
        # if(Staff_Designation):
        #     if not Staff_Designation.replace(" ", "").isalnum():
        #         self._errors['Staff_Designation'] = self.error_class([
        #             'Please enter a valid designation'])
        # if(Staff_Institution_Emp_ID):
        #     if not Staff_Institution_Emp_ID.replace(" ", "").isalnum():
        #         self._errors['Staff_Institution_Emp_ID'] = self.error_class([
        #             'Please enter a valid Employee Number'])
        # if(Member_DL_No):
        #     if not Member_DL_No.replace(" ", "").isalnum():
        #         self._errors['Member_DL_No'] = self.error_class([
        #             'Please enter a valid DL Number'])

                
        # return any errors if found
        return self.cleaned_data



class add_vehicle_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

    class Meta:
        model=add_vehicle
        fields='__all__'
        exclude=["Updated_Date","Updated_By","Status"]

    # DATE_INPUT_FORMATS = ['%d-%m-%Y']
    # DL_Validity = forms.DateField(input_formats= DATE_INPUT_FORMATS)
    # RC_Valid_Upto =forms.DateField(input_formats= DATE_INPUT_FORMATS)
    # Insurance_Valid_Upto =forms.DateField(input_formats= DATE_INPUT_FORMATS)
    # CHOICES = (
    #     ('yes','Yes'),
    #     ('no','No')
    # )

    # MEMBER_CHOICES=(
    # ('member','Member'),
    # ('occupant','Occupant')
    # )
    
    # class HorizontalRadioRenderer(forms.RadioSelect):
    #     def render(self):
    #         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
    
    # Vehicle_Available = forms.ChoiceField(label="Is there a vehicle associated with the room?",choices=CHOICES,
    #     widget=forms.RadioSelect()) 
    
    # Member_Occupant = forms.ChoiceField(label="Vehicle belongs to Member or the Occupant?",choices=MEMBER_CHOICES, 
    #         widget=forms.RadioSelect())
    Gate_Name=forms.ModelMultipleChoiceField(queryset=Gate_Master.objects.all(),
            widget=forms.CheckboxSelectMultiple)
    
    

    # this function will be used for the validation
    def clean(self):
        super(add_vehicle_form, self).clean()
        
        # Name=self.cleaned_data.get('Name')
        # Mobile=self.cleaned_data.get('Mobile')
        # #Member_Whatsapp=self.cleaned_data.get('Member_Whatsapp') #+,d
        # Staff_Designation=self.cleaned_data.get('Staff_Designation')
        # Staff_Institution_Emp_ID=self.cleaned_data.get('Staff_Institution_Emp_ID')
        # Aadhaar_ID=self.cleaned_data.get('Aadhaar_ID')
        # #Member_DL_No=self.cleaned_data.get('Member_DL_No')
        # Emergency_Contact_Name=self.cleaned_data.get('Emergency_Contact_Name')
        # Emergency_Contact_Email=self.cleaned_data.get('Emergency_Contact_Email')
        # #Emergency_Contact_ISD=self.cleaned_data.get('Emergency_Contact_ISD')
        # #Emergency_Contact_Mobile_No=self.cleaned_data.get('Emergency_Contact_Mobile_No')
        # Emergency_Contact_Address=self.cleaned_data.get('Emergency_Contact_Address')



        # # conditions to be met for the username length
        # # if len(str(Mobile)) != 10:
        # #     self._errors['Mobile'] = self.error_class([
        # #         'Mobile Number should contain 10 digits'])
        
    
        
        # # if len(str(Emergency_Contact_Address)) < 50:
        # #     self._errors['Emergency_Contact_Address'] = self.error_class([
        # #         'Minimum length is 50 characters'])

        # # if len(str(Aadhaar_ID)) != 12:
        # #     self._errors['Aadhaar_ID'] = self.error_class([
        # #         'Aadhaar Number should contain 12 digits'])
        # if(Name):
        #     if not Name.replace(" ", "").isalpha():
        #         self._errors['Name'] = self.error_class([
        #             'Please enter a valid name'])
        # if(Emergency_Contact_Name):
        #     if not Emergency_Contact_Name.replace(" ", "").isalpha():
        #         self._errors['Emergency_Contact_Name'] = self.error_class([
        #             'Please enter a valid name'])
        
        # email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        # if(Emergency_Contact_Email):
        #     if (not re.search(email_regex, Emergency_Contact_Email)):
        #         self._errors['Emergency_Contact_Email'] = self.error_class([
        #             'Please enter a valid Email ID'])
        # if(Staff_Designation):
        #     if not Staff_Designation.replace(" ", "").isalnum():
        #         self._errors['Staff_Designation'] = self.error_class([
        #             'Please enter a valid designation'])
        # if(Staff_Institution_Emp_ID):
        #     if not Staff_Institution_Emp_ID.replace(" ", "").isalnum():
        #         self._errors['Staff_Institution_Emp_ID'] = self.error_class([
        #             'Please enter a valid Employee Number'])
        # # if(Member_DL_No):
        # #     if not Member_DL_No.replace(" ", "").isalnum():
        # #         self._errors['Member_DL_No'] = self.error_class([
        # #             'Please enter a valid DL Number'])

                
        # return any errors if found
        return self.cleaned_data


class add_maid_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model=add_maid
        fields='__all__'
        exclude=["Updated_Date","Updated_By","Status"]
  
    def clean(self):
        super(add_maid_form, self).clean()        
        # return any errors if found
        return self.cleaned_data


class add_emergency_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model=add_emergency
        fields='__all__'
        exclude=["Updated_Date","Updated_By","Status"]
  
    def clean(self):
        super(add_emergency_form, self).clean()        
        # return any errors if found
        return self.cleaned_data

class add_maintenance_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model=add_maintenance
        fields='__all__'
        exclude=["Updated_Date","Updated_By","Status"]
        
    def clean(self):
        super(add_maintenance_form, self).clean()        
        # return any errors if found
        return self.cleaned_data