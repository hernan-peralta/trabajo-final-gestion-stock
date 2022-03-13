class RepositorioFormaPago:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def buscar_por_nombre(self, forma_pago):
        self.cursor.execute(
            "SELECT * FROM forma_pago WHERE forma_pago.forma_pago LIKE %s",
            (forma_pago.lower(),))
        return self.cursor.fetchone()

    def obtener_por_id(self, id_forma_pago):
        self.cursor.execute(
            "SELECT * FROM forma_pago WHERE forma_pago.id = %s",
            (id_forma_pago,))
        return self.cursor.fetchone()
