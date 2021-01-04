from abc import ABC, abstractmethod


class Factory(ABC):
    """
        Фабрика производит Product_A and Product_B
    """

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class FactoryOSX(Factory):
    """
         Поставщик Product_А and Product_B
    """

    def create_product_a(self):
        return WindowOSX()

    def create_product_b(self):
        return MenuOSX()


class FactorySolaris(Factory):
    """
         Поставщик Product_А and Product_B
    """

    def create_product_a(self):
        return WindowSolaris()

    def create_product_b(self):
        return MenuSolaris()


class InterfaceWindow(ABC):
    """
         Способ изготовления Product_A
    """

    @abstractmethod
    def product_a_mode(self):
        pass


class WindowOSX(InterfaceWindow):
    """
         У поставщика А свой способ изготвления Product_A
    """

    def product_a_mode(self):
        return 'FactoryOSX window'


class WindowSolaris(InterfaceWindow):
    """
         У поставщика В свой способ изготовления Product_A
    """

    def product_a_mode(self):
        return 'FactorySolaris window'


class InterfaceMenu(ABC):
    """
         Способ изготовления Product_B
    """

    @abstractmethod
    def product_b_mode(self):
        pass


class MenuOSX(InterfaceMenu):
    """
         У поставщика А свой способ изготвления Product_B
    """

    def product_b_mode(self):
        return 'FactoryOSX menu'


class MenuSolaris(InterfaceMenu):
    """
         У поставщика А свой способ изготвления Product_B
    """

    def product_b_mode(self):
        return 'FactorySolaris menu'


a = FactoryOSX()
print(a.create_product_a().product_a_mode())

# def client_code(factory: Factory) -> None:
#     product_a = factory.create_window()
#     product_b = factory.create_menu()
#     print(f"{product_b.create_menu()}")
#     print(f"{product_a.create_window()}", end="")
#
# if __name__ == "__main__":
#
#     print("Client: Testing client code with the first factory type:")
#     client_code(FactoryOSX())
#
#     print("\n")
#
#     print("Client: Testing the same client code with the second factory type:")
#     client_code(FactorySolaris())
