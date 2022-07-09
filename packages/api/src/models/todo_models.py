# validation schema for creating a to-do activity
TODO_SCHEMA_POST = {
    'required': ['todo', 'date', 'priority', 'checked'],
    'properties': {
        'todo': {'type':'string'},
        'date': {'type':'string', "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }, 
    'additionalProperties': False
}

# validation schema for editing a to-do activity
TODO_SCHEMA_PATCH = {
    'properties': {
        'todo': {'type':'string'},
        'date': {'type':'string', "pattern": "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }
}