# Flask App Factory - Project Structure Demo

This project demonstrates how to organize files and responsibilities using Flask's **App Factory** pattern. The purpose is to showcase best practices in setting up a scalable and maintainable project, without focusing on specific functionalities.

## Project Structure

```bash
flask-app-factory-demo/
├── app/
│   ├── __init__.py          # Contains the create_app function
│   ├── routes.py            # Blueprint for API routes
│   └── models.py            # Database models (optional)
├── tests/
│   ├── test_routes.py        # Unit tests for routes
├── .env                      # Environment variables
├── config.py                 # Configuration classes (development, production, etc.)
├── requirements.txt          # Project dependencies
└── wsgi.py                   # Entry point for the application (e.g., Gunicorn)
```


# Flask App Factory Implementation:

The Flask's Application Factory is a recommended pattern to create and configure the Flask application in different scenarios ensuring flexibility, modularity and tests. Using this pattern we can create multiple instances of application with different configurations.

## App Context:

Flask's Application Context is a concept to encapsulates all the information required for a specific application instance. Including differents application's configuration, database connection, blueprints creations, etc. The App Context ensures that these resources are accessible only within the correct scope, so you can deal with multiple applications instances.
- [The Application Context](https://flask.palletsprojects.com/en/2.3.x/appcontext/)

## App Factories:

The App Factory pattern involves defining a create_app function that initializes and configures a Flask application instance. This function allows you to specify different configurations by passing the appropriate configuration class as a parameter.
- [Application Factories](https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/)

## Configuration Handle:

Flask provides a system of managing application configurations. You can define different configuration classes ('DevelopmentConfig', 'ProductionConfig', 'TestingConfig') that specify environment-specific settings. These configurations includes database URIs, secret keys, debug, testing, cookies managments, and more.
- [Configuration Handling](https://flask.palletsprojects.com/en/3.0.x/config/)

## Test Coverage:

For last but not least, testing in Flask. We can create a test instance of the application with specific testing configurations, ensuring isolation from the production environment.
- [Test Coverage](https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/)