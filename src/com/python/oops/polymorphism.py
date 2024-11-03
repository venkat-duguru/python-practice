class Professional:
    def tax(self):
        print("collects from working men")

class Gst(Professional):
    def tax(self):
        print("collects from purchases")


professional = Professional()
professional.tax()
gst = Gst()
gst.tax()
