from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField,SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

# class WatchCreateForm(FlaskForm):
#     categortid=SelectField(label="Categort", validators=[DataRequired('Select Categort')],choices=[
#         ('Latest consignment','Latest conginment'),
#         ('Retro','Retro'),
#         ('Limited edition','Limited edition'),
#         ('Minimalist','Minimalist'),
#         ('Self winding','Self winding'),
#         ('Military','Military'),
#         ('Sport','Sport')
#     ],default='Latest consignment')
#     name=StringField("Product Name", validators=[InputRequired('Enter Product Name')])
