
start django project with command:

django-admin startproject **projectname** .

create django app:

python manage.py startapp **appname**

click on ‘use this template’ and  create our repository from it.
Then we can open it up in  Gitpod with the Gitpod button.
Now that we’re in our IDE, let’s  install Django from the terminal.
Let’s start our project,  call it drf_api
and follow it up with a dot, to  initialize it in the current directory.
Next, in order to connect our  Django project to Cloudinary,
we need to install a library called Django  Cloudinary storage.
We have another dependency we need to install  called Pillow, this library adds image processing
capabilities that we need for this project.  Note that it’s name starts with a capital P.
Once that’s done, we’ll have to add the  newly installed apps to settings.py,
it’s important to get your  app names in this order here,
with django.contrib.staticfiles between  cloudinary_storage and Cloudinary.
Next, we need to set up the  Cloudinary environment variable.
I’ll create the env.py file in the top  directory. Inside, I’ll import the os module,
then we need to grab our Cloudinary  API key from the Cloudinary website.
We’ll copy that, and then paste in the key and  set it to os.environ CLOUDINARY_URL like this.
Then back in our settings.py file, we can  load our environment variable with the
Cloudinary credentials, so I’ll import the  os module and import env.py if it exists.
The Cloudinary library we installed needs us to  set a variable called CLOUDINARY_STORAGE like this.
And we will use the environment variable  we set in the env.py file to declare that value.
Then we need to define a setting called MEDIA_URL,  which is the standard Django folder to store media
files like images. We’ll set that to ‘/media/’ so  the settings know where to put our image files.
And finally, we also need to set  a DEFAULT_FILE_STORAGE variable to
MediaCloudinaryStorage.
Now we have all our settings in  place, well done! In this video,





##############################################


In this video, we’ll create the  profiles app and write a Profile model.
So let’s create our profiles app with the startapp command.
And we need to make sure that we  add it to the installed apps, too!
Now, inside models.py, I’ll  import the standard Django User Model,
so we can reference it in our custom models.
First, we’ll create our Profile model.
It will have a number of fields. Owner will be  a one-to-one field pointing to a User instance.
I’ll set on_delete to cascade.
I’ll also add the created_at  and updated_at timestamps.
The ‘name’ CharField will be optional  and have a max length of 255.
The ‘content’ TextField will be optional, too.
Now, to store images in our database, we need  a different kind of model field called an
ImageField, for this field we need  to define parameters for upload_to,
the value is a folder name called images.  Don’t forget the slash at the end here.
And we want to provide a default image  for when the user hasn’t provided one yet.
So we’ll grab the whole file name, including the  hash, from the Cloudinary website and paste it in here.
We also need to start the file path  with ../ so it works with the file structure
that Cloudinary will create when we migrate our models.
Inside our Profile model, I’m going to  create a Meta class that will return
our Profile instances in reverse order,  so the most recently created is first.
This bit relates  to this field name. And the minus sign at
the beginning of the string, indicates  that we want our results in reverse.
And in the dunder string method, I’ll return  information about who the profile owner is.
All good so far, now we need to ensure that a  profile is created every time a user is created.
We can do that with a Django  feature called signals.
You can think of signals as notifications that  get triggered by an event. We can listen for
such Model events and have some code, usually a  function, run each time that signal is received.
In our case, we would want to be notified when a
user is created so that a profile can  automatically be created alongside it.
Examples of built-in Model signals include:  pre_save, post_save, pre_delete and post_delete.
So, I’ll import post_save at  the top from Django’s signals.
Now I’ll listen for the post_save signal coming  from the User model by calling the connect function.
Inside, I’ll pass ‘create_profile’,  which is the function I’d like to run every time
and specify User as the model we’re  expecting to receive the signal from.
Now we have to define the create_profile function  before we pass it as an argument. Because we are
passing this function to the post_save.connect  method, it requires the following arguments:
the sender model, its instance, created  - which is a boolean value of whether or
not the instance has just been created, and  kwargs. Inside the create_profile function,
if created is True, we’ll create a profile  whose owner is going to be that user.
Great, now every time a user is  created, a signal will
trigger the Profile model to be created.  We’ll make sure it works in a minute.
Now we need to register our Profile  model in admin.py so that it will
show up in our admin panel. So, I’ll import  our Profile model and register it to view.
Now, in order to access our admin  panel, we need to create our superuser.
We don’t need to provide an email, but we do need a password.
Now, if we run our server,
and go to /admin,
we see that our first user was created.
And their corresponding profile was  created with a working image, well done!
Before we finish, let’s create  a file with our dependencies.
Now we can add, commit and push all the changes.



## important Cheat Sheet to check it for django:

#### https://docs.google.com/document/d/1i4ZZcV5B9g-a0gXZoxgmt7mhrqdizVOjXuT3-NGxiHg/edit#heading=h.juhzxg1uv26f