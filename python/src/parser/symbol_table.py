class SymbolTable:
    def __init__(self):
        self.table = {}

    def set_value(self, id, value, type, context):
        self.table[id] = {
            'value': value,
            'type': type,
            'context': context,
        }

    def get_value(self, id):
        return self.table[id]['value'] if id in self.table else None

    def set_context(self, id, context):
        if id in self.table:
            self.table[id]['context'] = context

    def get_context(self, id):
        return self.table[id]['context'] if id in self.table else None
    
    def __str__(self):
        text = ''
        for key, data in self.table.items():
            value = data['value']
            type = data['type']
            context = data['context']
            text += f'+ {key} ({type},{context}) => {value}\n'
        return text