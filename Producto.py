class Producto:
    def __init__(self, nombre, precio, cantidad, id):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
        self.__id = id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self):
        return 'nombre: {}\n precio: {}\n cantidad: {}\n id: {}'.format(self.nombre, self.precio, self.cantidad, self.id)
    
    def __repr__(self):
        rep = f'Producto({self.nombre} {self.precio} {self.cantidad} {self.id})'
        return rep