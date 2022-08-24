import random
note0_b = 2
note1_b = random.randint(3,7)
note2_b = random.randint(3,7)
note3_b = random.randint(3,7)
note4_b = random.randint(3,7)
note5_b = random.randint(3,7)
note6_b = random.randint(3,7)
note7_b = random.randint(3,7)
note8_b = random.randint(3,7)
note9_b = random.randint(3,7)
note10_b = random.randint(3,7)
note11_b = random.randint(3,7)
note12_b = random.randint(3,7)
note13_b = random.randint(3,7)
note14_b = random.randint(3,7)
note15_b = random.randint(3,7)
hannonlist = []

number_to_note = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'A',8:'B'}

def note_sequencer(note0, note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14, note15, hannonlist,number_to_note):
    hannonlist.append(number_to_note[note0]+ number_to_note[note1] + number_to_note[note2] + number_to_note[note3]
    + number_to_note[note4] + number_to_note[note5] + number_to_note[note6] + number_to_note[note7]+ number_to_note[note8] +
    number_to_note[note9] + number_to_note[note10] + number_to_note[note11] + number_to_note[note12] + number_to_note[note13] +
    number_to_note[note14] + number_to_note[note15])
    return hannonlist
direction = 1
for i in range(0,2):
    bar = 0
    for j in range(0,15):
        note0 = (8+note0_b*direction+bar)%7
        note1 = (8+note1_b*direction+bar)%7
        note2 = (8+note2_b*direction+bar)%7
        note3 = (8+note3_b*direction+bar)%7
        note4 = (8+note4_b*direction+bar)%7
        note5 = (8+note5_b*direction+bar)%7
        note6 = (8+note6_b*direction+bar)%7
        note7 = (8+note7_b*direction+bar)%7
        note8 = (8+note8_b*direction+bar)%7
        note9 = (8+note9_b*direction+bar)%7
        note10 = (8+note10_b*direction+bar)%7
        note11 = (8+note11_b*direction+bar)%7
        note12 = (8+note12_b*direction+bar)%7
        note13 = (8+note13_b*direction+bar)%7
        note14 = (8+note14_b*direction+bar)%7
        note15 = (8+note15_b*direction+bar)%7
        hannonlist = note_sequencer(note0, note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14, note15, hannonlist,number_to_note)
        bar = bar+1
    direction = -1
print hannonlist

