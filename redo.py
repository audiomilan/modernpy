class Wrestlers:
    def __init__(self, the_rock, stone_cold, hulk_h):
        self.the_rock = the_rock
        self.stone_cold = stone_cold
        self.hulk = hulk_h
    
    def Rock(self):
        return f"I will Lay the Smackdown: ({self.the_rock}) The Rock "
    
    def Stone_Cold(self):
        return f"Get my fucking beer : ({self.stone_cold}) Stone Cold"
    
    def Hulk1(self):
        return "Im real good with math , with numbers like my dad was. Im pretty muched dialed in ({self.hulk_h}) Hulk Hogan"

class Old_Wrestlers:
    def __init__(self, hardy_boys, undertaker, Cane):
        self.hardy_boys = hardy_boys
        self.undertaker = undertaker
        self.Cane = Cane

    def Hardy(self):
        return f"Off the ropes with the twist of fate ({self.hardy_boys}) Hardy Boys"
    
    def Undertaker1(self):
        return f"I am about to send you to the morgue ({self.undertaker}) The Undertaker"

    def Cane1(self):
        return f"Ask what happen to my brother Able ({self.Cane}) Cane"

ins = Wrestlers(
    {'move' : 'peoples elbow' , 'hometown' : 'miami' , 'ratings' : 'five star'},
    ['shit talking' , 'beer can smashing' 'stone cold stunna'],
    ('wrestle mania' , 'royal rumble')
)

ins2 = Old_Wrestlers(
        {'name' : 'Matt Hardy' , 'style' : 'flyers' , 'measures taken' : 'drastic'},
        ['chokeslam' , 'very tall', 'dangerous' , 'mute'],
        ('chokeslam' , 'very tall' , 'dangerous' , 'mute' )

)

print(ins.Rock())
print(ins.Stone_Cold())
print(ins.Hulk1())
print(ins2.Hardy())
print(ins2.Undertaker1())
print(ins2.Cane1())


