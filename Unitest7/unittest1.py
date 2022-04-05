import unittest
import cart
#import carte

class CarTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up for a test")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after a test")

    def setUp(self):
        self.car = cart.Car(1, "volvo", "c30", 2011, "red", 12000)

  #      self.car=cart.Car("Volvo", "Red", "c30", 1054)

    def test_get_car_price(self):
        self.assertEqual(self.car1.getPrice, '10000')

  #  def test_get_model_car(self):
   #     self.assertGreater(cart.car6.get_model_car(), cart.car4.get_model_car())


    def test_how_old_car(self):
        self.assertEqual(self.car1.setYear, '2020')

    def test_show_car_info(self):
        self.assertMultiLineEqual("hatchback", cart.car8.model)

    def test_current_year_car(self):
        self.assertEqual(cart.car1.current_year_car(), 2022)

#def test_get_number(self):
      #  self.assertEqual(self.car1.setRegNumber, '1054')

if __name__ == '__main__':
    unittest.main()