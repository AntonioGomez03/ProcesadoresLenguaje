class SymbolTable:
    def __init__(self):
        self.table = {}
        
    def set_value(self, id, value, type, context):
        if id in self.table:
            raise ValueError(f"Identificador duplicado '{id}' detectado.")
        
        self.table[id] = {
            'value': value,
            'type': type,
            'context': context,
            }

    def get_value(self, id):
        if id in self.table:
            return self.table[id]['value']
        else:
            raise KeyError(f"Identificador '{id}' no declarado.")

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

# class SymbolTable:
#     def __init__(self):
#         self.table = {}

#     def set_value(self, id, value, type, context):
#         key = (id, type)
#         if key in self.table:
#             raise ValueError(f"El identificador '{id}' con tipo '{type}' ya existe.")
#         self.table[key] = {
#             'value': value,
#             'context': context
#         }

#     def get_value(self, id, type):
#         key = (id, type)
#         if key in self.table:
#             return self.table[key]
#         else:
#             raise KeyError(f"Identificador '{id}' con tipo '{type}' no encontrado.")
        
#     def set_context(self, id, context):
#         if id in self.table:
#             self.table[id]['context'] = context
            
#     def get_context(self, id):
#         return self.table[id]['context'] if id in self.table else None

#     def __str__(self):
#         text = ''
#         for (id, type), data in self.table.items():
#             value = data['value']
#             context = data['context']
#             text += f'+ {id} ({type}, {context}) => {value}\n'
#         return text