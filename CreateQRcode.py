from distutils.log import info
from re import A
from textwrap import indent
import qrcode

def Info():
    name = ('Akane Sei')
    Location = ('Osaka, Japan')
    Birthdate = ('October 26, 2002')
    Age= ('19 years old')
    Date = ('04/05/2022')
    return (f'Name:{name}    Location: {Location}    Birthdate: {Birthdate}     Age: {Age}     Date today: {Date}     ')

data =qrcode.make(Info())
data.save('Profile.jpg')