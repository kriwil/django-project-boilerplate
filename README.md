django-project-boilerplate
==========================

This is my personal django project boilerplate.

* uses django 1.4
* custom test root dir and runner ([http://carljm.github.com/django-testing-slides/]())

The project structure:

    project/ (this is main project, where app modules located)

        project/
            __init__.py

            settings/ (the settings module)
                __init__.py (base shared settings)
                development.py (development shared settings)
                local.py (your personal settings. this shouldn't be in your repository)
                production.py (production settings)

        manage.py (I updated to use settings.local by default)

        contrib (my personal contrib modules)
        templates (project wide template dir)
        tests (custom tests root dir)
        staticfiles (projecet wide staticfiles dir)

    requirements.pip (the pip's requirements file -- for pip install -r file)
