

# Projetodjango

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/projetodjango.git
    $ cd projetodjango
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    
In some cases it may give the error "SyntaxError: Generator expression must be parenthesized"
being solved with code:

    $ pip install django==1.11.17
    

You can now run the development server:

    $ python manage.py runserver
