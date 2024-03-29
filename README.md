# django_unittest_image_helper
An open source package for helping the django unittest journey

## Description
A Python library to facilitate the django unittesting journey.
## Installation
```
pip install django-unittest-helper

```
## Usage

#### For getting dummy form-data images for payload during unittesting 

```python
from django_unittest_helper import form_image_helper
payload = form_image_helper(caption_list=['photo', 'map'], image_suffix=".jpg")

```

The above code will return dummy images for api testing.


There are 2 parameters for this method-

1. ```caption_list``` : Provide caption titles for the payload in list.
2. ```image_suffix``` : Provide the extension of the images as per your need. 


#### For generating random phone number
```python
from django_unittest_helper import generate_random_phone_no

phone_no = generate_random_phone_no(prefix="013", total_digit=11)
```
The above code will return a dummy phone number based on random digits

There are 2 parameters for this method-

1. ```prefix``` : Provide the prefix of the operator of phone no
2. ```total_digit```: Provide the total digits of the phone number you need
