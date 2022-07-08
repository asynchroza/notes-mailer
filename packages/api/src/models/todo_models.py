# validation schema for creating a to-do activity
TODO_SCHEMA_POST = {
    'required': ['todo', 'date', 'priority', 'checked'],
    'properties': {
        'todo': {'type':'string'},
        'date': {'type':'string', "pattern": "^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }, 
    'additionalProperties': False
}

# validation schema for editing a to-do activity
TODO_SCHEMA_PATCH = {
    'properties': {
        'todo': {'type':'string'},
        'date': {'type':'string', "pattern": "^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }
}