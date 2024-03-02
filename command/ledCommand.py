# TODO: insert robot code here
import wpilib 

class LightLED(wpilib.TimedRobot):
    def ledInit(self):
        
        self.m_led = wpilib.AddressableLED()
        self.m_ledBuffer = wpilib.AddressableLEDBuffer()
        self.m_led.setLength(self.m_ledBuffer.getLength())
        self.m_led.setData(self.m_ledBuffer)
        self.m_led.start()




    def ledPeriodic(self):
        color = input("r, g, b, rb?")
        
        if color == "r":
            print("Red light")
            for i in range(self.m_ledBuffer.getLength()):
                self.m_ledBuffer.setRGB(i, 255, 0, 0)
            self.m_led.setData(self.m_ledBuffer)
        elif color == "g":
            for i in range(self.m_ledBuffer.getLength()):
                self.m_ledBuffer.setRGB(i, 0, 255, 0)
            self.m_led.setData(self.m_ledBuffer)
        elif color == "b":
            for i in range(self.m_ledBuffer.getLength()):
                self.m_ledBuffer.setRGB(i, 0, 0, 255)
            self.m_led.setData(self.m_ledBuffer)
        #elif color == "rb":
          #  for i in range(self.m_ledBuffer.getLength()):
           # hue = (self.m_rainbowFirstPixelHue + (i * 180 / self.m_ledBuffer.getLength())) % 180
          #  self.m_ledBuffer.setHSV(i, hue, 255, 128)
          #  self.m_rainbowFirstPixelHue += 3
           # self.m_rainbowFirstPixelHue %= 180
        print("your color is "+ color)


if __name__ == "__main__":
    wpilib.run(LightLED)