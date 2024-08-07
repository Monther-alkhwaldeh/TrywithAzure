import time

from behave import *

from Utilites import configReader
from features.pageObject.RegistrationPage import RegistrationPage


@given(u'I Enter The qa.automation.com')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))


@when(u'I enter the name as "{name}"')
def step_impl(context, name):
    context.reg.setName(name)


@when(u'I enter the phone as "{phone}"')
def step_impl(context, phone):
    context.reg.setPhone(phone)


@when(u'I Enter the email as "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)


@when(u'I enter the country as "{country}"')
def step_impl(context, country):
    context.reg.setCountry(country)


@when(u'I enter the city as "{city}"')
def step_impl(context, city):
    context.reg.setCity(city)


@when(u'I enter the username as "{username}"')
def step_impl(context, username):
    context.reg.setUsername(username)


@when(u'I enter the password as "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)


@when(u'I click on the sub,it button')
def step_impl(context):
    context.reg.submitForm()

@given(u'I click on login button')
def step_impl(context):
    context.reg.clicklogin()

@given(u'I enter the usern as "{usern}"')
def step_impl(context,usern):
    context.reg.enterusername(usern)

@given(u'I enter the passw as "{passw}"')
def step_impl(context, passw):
    context.reg.enterpassword(passw)
@given(u'I click on submit login')
def step_impl(context):
    context.reg.submitLogin()
