# validation schema for creating a to-do activity
TODO_SCHEMA_POST = {
    'required': ['id', 'todo', 'isodate', 'priority', 'checked'],
    'properties': {
        'id': {'type':'string'},
        'todo': {'type':'string'},
        'isodate': {'type':'string', "pattern": "/(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d)/"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }, 
    'additionalProperties': False
}

# validation schema for editing a to-do activity
TODO_SCHEMA_PATCH = {
    'properties': {
        'todo': {'type':'string'},
        'isodate': {'type':'string', "pattern": "/(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d)|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d)/"},
        'priority': {'type':'integer'},
        'checked': {'type':'boolean'}
    }
}