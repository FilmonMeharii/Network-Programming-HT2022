import re
print('\n')

txt = "Hanoror bught 5 portions of orange soil for 13.50 EUR."

#print(re.findall("or", txt))#['or', 'or', 'or', 'or', 'or']
#help(re.findall)

#print(re.findall("",txt))#['', '', '', '', '', '', '', ''....]
#print(re.findall("or.", txt)) #['oro', 'ort', 'ora', 'or ']
#print(re.findall("..\.", txt)) #['13.', 'UR.']

#r-prefix

#print("Hello\nWorld")   #Hello
                        #World

#print(r"Hello\nWorld")#Hello\nWorld

#print(re.findall(r"\w", txt)) #['H', 'a', 'n', 'o', 'r', 'o',...] w = word
#print(re.findall(r"\W", txt)) #[' ', ' ', ' ', ' ', ' ', ' ', ' ....]

#print(re.findall(r"\d", txt)) #['5', '1', '3', '5', '0'] d= digit

#print(re.findall(r"\D", txt)) #all txt with space and point.

#print(re.findall(r"\s", txt)) # s= seperator [' ', ' ', ' ', ' ',...]
#print(re.findall(r"\S", txt)) #all txt with space and point.

#re.findall(r"[bcdfghjklmnpqrstvxz]", txt)
#print(re.findall("[0-9a-f]"), txt)

#print(re.findall(r"\d+", txt)) #['5', '13', '50']
#print(re.findall(r"\w+", txt))#['Hanoror', 'bught', '5', 'portions', 'of', 'orange', 'soil', 'for', '13', '50', 'EUR']
#print(re.findall(r"\w*or\w*", txt)) #['Hanoror', 'portions', 'orange', 'for']

#EAger and Gready
#print(re.findall(r"\w*\d", "abc123def456ghi")) #['abc123def456']
#print(re.findall(r"\w*?\d", "abc123def456ghi")) #['abc1', '2', '3', 'def4', '5', '6']

#Warm up
mtxt = "jox r.nohre@jyh.hj.se, bjox@se, adam@example.com, jox@jox@jox.com"

#print(re.findall(r"\w+@\w+", mtxt)) #['nohre@jyh', 'bjox@se', 'adam@example', 'jox@jox']

#Task 1
#print(re.findall(r'\w+(\.\w+)*@\w+', mtxt))
#print( re.findall(r'(\w+(\.\w+)*@\w+)', mtxt))
#print(re.findall(r'\w+(?:\.\w+)*@\w+', mtxt))
print(re.findall(r'\s(\w+(?:\.\w+)*@\w+(?:\.\w+)*\.\w+)', mtxt)) #['r.nohre@jyh.hj.se', 'adam@example.com']

#Task 2 

htmltxt = """bla bla bla 
            <h1> My Rubric      <\h1>
            bla bla bla."""

#print(re.findall(r"<h1>\s*.*\s*</h1>", htmltxt))
#print(re.findall(r"<h1>\s*(.*)\s*</h1>", htmltxt))
#print(re.findall(r"<h1>\s*(.*?)\s*</h1>", htmltxt))

f = open("tabla.html", encoding= "utf-8")
txt = f.read()

#print(re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>', txt))
#['06.00', '06.25', '07.10', '07.35', '08.00', '08.30', '09.00', '09.30', '10.00', '10.30', '11.00', '11.30', '12.30', '13.30', '14.00', '14.30', '15.00', '15.30', '16.00', '16.30', '17.00', '17.30', '18.00', '18.30', '19.00', '19.30', '20.00', '20.30', '21.00', '23.20', '23.50', '00.20', '00.45', '01.10', '01.40', '02.10', '02.30', '02.55', '03.20', '03.40', '04.05', '04.25', '04.50', '05.10', '05.35']

#print(re.findall(r'''<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*(?:<div.*?>\s*)*<p.*?>\s*.*?(Säsong)\s(\d+).*?(\d+).*?(\d+)\.\s(.*?)\..*?\s*(Regi.*?)?\..*?\s*</p>''', txt ))


regResult = re.findall(r'''<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>
\s*(?:<div.*?>\s*)*<p.*?>\s*.*?(Säsong)\s(\d+).*?(\d+).*?(\d+)\.\s(.*?)\..*?\s*(Regi.*?)?\..*?\s*</p>''', txt )
#
#print('    macnora:kodSimpsons nora$ python3 simpsonScrap.py')
for s in regResult:
    print('-----------------------')
    print('Tid: ', s[0])
    print('Säsong: ', s[2])
    print('Avsnitt: ', s[3],'/',s[4])
    print('Handling: ', s[5])

print('\n')
print('\n')
