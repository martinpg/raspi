import I2C_LCD_driver
import sys

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string(sys.argv[1], 1) 
mylcd.lcd_display_string(sys.argv[2], 2)
