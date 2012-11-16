## django-testapp with django-bootstrap-toolkit

This is a basic appengine Django app I built as a demo.  It implements a very simple blog system which has Posts and basic tagging.  There's only support for creating a post with tags, viewing the post list, and filtering the posts by tags.

I've also integrated bootstrap using [django-bootstrap-toolkit](https://github.com/dyve/django-bootstrap-toolkit)

[django-nonrel](https://github.com/django-nonrel/django-nonrel) does not support the use of ManyToMany fields, so to implement tagging I used [ListField](https://gist.github.com/1200165) from [django-toolbox](https://github.com/django-nonrel/djangotoolbox).
	
## Installation

Clone this repository.  Run the `build.sh` script which will use pip to install all the related packages like django-nonrel inside the project directory.  If it doesn't work just take a look at `requirements.txt` and `build.sh` and manually sort it out.

## Reading

* [django-appengine docs](http://www.allbuttonspressed.com/projects/djangoappengine)

* [Using a ListField](https://gist.github.com/1200165)

## Demo

View it live at [jmoztest1.appspot.com](http://jmoztest1.appspot.com/)