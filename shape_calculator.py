class Rectangle:

    def __init__(self,width,height):
        self.width = width   
        self.height = height 
         
    def set_width(self,width):
        self.width = width
        
    def set_height(self,height):
        self.height = height  
          
    def get_area (self):
        area =  (self.width * self.height)
        return area
    def get_perimeter (self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            string = ""
            for i in range (self.height):
                string = string + ("*" *  self.width) + "\n"
            return string
    def get_amount_inside (self,passed):
        maximo_horizontal  = self.width // passed.width
        maximo_vertical = self.height // passed.height
        total = maximo_horizontal * maximo_vertical
        return total
    def __str__(self):
        return "Rectangle(width="+ str(self.width) +", height="+ str(self.height) +")"
  
  
class Square (Rectangle):
    
    def __init__(self, side ):
        self.width = side    
        self.height = side  
    def set_side (self,side):
        self.width = side    
        self.height = side                  
    def __str__(self):
        return "Square(side="+str(self.height)+")"
    
    def set_width(self,width):
        self.width = width
        self.height = width
        
    def set_height(self,height):
        self.height = height  
        self.width = height
