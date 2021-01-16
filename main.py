import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import struct
print(struct.calcsize("P") * 8)

def stepPlotNRZU(title, apply_rules_of_encoding, list_of_givenBits):
    apply_rules_of_encoding = apply_rules_of_encoding[:1] + apply_rules_of_encoding
    plt.figure(figsize=(12, 6))
    plt.suptitle(title, fontsize=16)
    encodP = plt.subplot(3, 1, 2)
    encodP.set_xlim(0, len(apply_rules_of_encoding) - 1)
    dim = np.arange(len(apply_rules_of_encoding))
    plt.xticks(dim)
    plt.grid(True, which='both')

    y1 = list(apply_rules_of_encoding)
    x1 = []
    for i in range(len(apply_rules_of_encoding)):
        x1.append(i)

    for counter, bit in enumerate(list_of_givenBits):
        plt.text(counter + 0.5, 1.5, str(bit), weight="bold")

    plt.ylabel('voltage')
    lines = plt.step(x1, y1)
    plt.setp(lines, linewidth=5, color='b')
    plt.show()


def stepPlot(title, apply_rules_of_encoding, list_of_givenBits):
    apply_rules_of_encoding = apply_rules_of_encoding[:1] + apply_rules_of_encoding
    plt.figure(figsize=(12, 6))
    plt.suptitle(title, fontsize=16)
    encodP = plt.subplot(3, 1, 2)
    encodP.set_xlim(0, len(apply_rules_of_encoding) - 1)
    dim = np.arange(len(apply_rules_of_encoding))
    plt.xticks(dim)
    plt.grid(True, which='both')
    plt.axhline(y=0, linewidth=3.5, color='black')

    y1 = list(apply_rules_of_encoding)
    x1 = []
    for i in range(len(apply_rules_of_encoding)):
        x1.append(i)

    for counter, bit in enumerate(list_of_givenBits):
        plt.text(counter + 0.5, 1.5, str(bit), weight="bold")

    plt.ylabel('voltage')
    lines = plt.step(x1, y1)
    plt.setp(lines, linewidth=3.5, color='b')
    plt.show()


def stepPlot2(title, apply_rules_of_encoding, list_of_givenBits):
    apply_rules_of_encoding = apply_rules_of_encoding[:1] + apply_rules_of_encoding
    plt.figure(figsize=(12, 6))
    plt.suptitle(title, fontsize=16)
    encodP = plt.subplot(3, 1, 2)
    encodP.set_xlim(0, len(apply_rules_of_encoding) - 1)
    dim = np.arange(len(apply_rules_of_encoding))
    plt.xticks(dim)
    plt.grid(True, which='both')
    plt.axhline(y=0, linewidth=4, color='black')

    y1 = list(apply_rules_of_encoding)
    x1 = []
    for i in range(len(apply_rules_of_encoding)):
        x1.append(i)

    for counter, bit in enumerate(list_of_givenBits):
        plt.text((counter * 2) + 1, 1.5, str(bit), weight="bold")

    plt.ylabel('voltage')
    lines = plt.step(x1, y1)

    plt.setp(lines, linewidth=5, color='b')
    plt.show()


def nrzUnipolar(list_of_givenBits):
    output = []
    for bit in list_of_givenBits:
        if bit == 0:
            output.append(0)
        else:
            output.append(1)
    return output


def nrzM(list_of_givenBits):
    output = []
    i = 0
    for n in list_of_givenBits:
        if n == 1:
            if (i % 2) == 0:
                output.append(1)
            else:
                output.append(-1)
            i += 1
        else:
            if n == 0:
                if (i % 2) == 0:
                    output.append(-1)
                else:
                    output.append(1)
    return output


def nrzS(list_of_givenBits):
    output = []
    i = 0
    for n in list_of_givenBits:
        if n == 0:
            if (i % 2) == 0:
                output.append(1)
            else:
                output.append(-1)
            i += 1
        else:
            if n == 1:
                if (i % 2) == 0:
                    output.append(-1)
                else:
                    output.append(1)
    return output


def nrzL(list_of_givenBits):
    output = []
    for bit in list_of_givenBits:
        if bit == 0:
            output.append(-1)
        else:
            output.append(1)
    return output


def amiBipolar(list_of_givenBits):
    output = []
    for bit in list_of_givenBits:
        if bit == 1:
            output.append(1)
        else:
            output.append(0)
    return output


def amiBipolar1(list_of_givenBits):
    output = []
    i = 0
    for n in list_of_givenBits:
        if n == 1:
            if (i % 2) == 0:
                output.append(1)
            else:
                output.append(-1)
            i += 1
        else:
            output.append(0)
    return output


def manchester(list_of_givenBits):
    output = []
    i = 0
    for n in list_of_givenBits:
        if n == 1:
            if (i % 2) == 0:
                output.append(-1)
                output.append(1)
            else:
                output.append(-1)
                output.append(1)
            i += 1
        else:
            if n == 0:
                output.append(1)
                output.append(-1)
            else:
                output.append(-1)
                output.append(1)
    return output


def biphaseM(list_of_givenBits):
    input = list(list_of_givenBits)
    output, lock, pre = [], False, ''
    for i in range(len(input)):
        if input[i] == 1 and not lock:
            output.append(1)
            output.append(-1)
            lock = True
            pre = 'S'
        elif input[i] == 0 and not lock:
            output.append(1)
            output.append(1)
            lock = True
            pre = 'Z'
        else:
            if input[i] == 1:
                if pre == 'S':
                    output.append(1);
                    output.append(-1)
                else:
                    output.append(-1);
                    output.append(1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    output.append(-1);
                    output.append(-1)
                else:
                    pre = 'Z'
                    output.append(1);
                    output.append(1)

    return output


def biphaseS(list_of_givenBits):
    input = list(list_of_givenBits)
    output, lock, pre = [], False, ''
    for i in range(len(input)):
        if input[i] == 0 and not lock:
            output.append(1)
            output.append(-1)
            lock = True
            pre = 'S'
        elif input[i] == 1 and not lock:
            output.append(1)
            output.append(1)
            lock = True
            pre = 'Z'
        else:
            if input[i] == 0:
                if pre == 'S':
                    output.append(1);
                    output.append(-1)
                else:
                    output.append(-1);
                    output.append(1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    output.append(-1);
                    output.append(-1)
                else:
                    pre = 'Z'
                    output.append(1);
                    output.append(1)

    return output


def manchesterDiff(list_of_givenBits):
    input = list(list_of_givenBits)
    output, lock, pre = [], False, ''
    for i in range(len(input)):
        if input[i] == 1 and not lock:
            output.append(-1)
            output.append(1)
            lock = True
            pre = 'S'
        elif input[i] == 0 and not lock:
            output.append(1)
            output.append(-1)
            lock = True
            pre = 'Z'
        else:
            if input[i] == 0:
                if pre == 'S':
                    output.append(-1);
                    output.append(1)
                else:
                    output.append(1);
                    output.append(-1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    output.append(-1);
                    output.append(1)
                else:
                    pre = 'Z'
                    output.append(1);
                    output.append(-1)

    return output


def pseudoternar(list_of_givenBits):
    output = []
    i = 0
    for bit in list_of_givenBits:
        if bit == 0:
            if (i % 2) == 0:
                output.append(1)
            else:
                output.append(-1)
            i += 1
        else:
            output.append(0)
    return output


def mlt33(list_of_givenBits):
    output = [0]
    last_changed = 0

    for bit in list_of_givenBits:
        if bit == 1 and (output[-1] == 1 or (output[-1] == 0 and output[-1] < last_changed)):
            last_changed = output[-1]
            output.append(output[-1] - 1)
        elif bit == 1:
            last_changed = output[-1]
            output.append(output[-1] + 1)
        elif bit == 0:
            output.append(output[-1])

    return output[1:]

def hdb333(list_of_givenBits):
    output = []
    sign = 0
    numberOfZeros = 0
    even = True
    for bit in list_of_givenBits:
        if bit == 1:
            sign = 1 if sign <= 0 else -1
            even = False if even else True
            output.append(sign)
            numberOfZeros = 0
        else:
            numberOfZeros += 1
            if numberOfZeros < 4:
                output.append(bit)
            else:
                numberOfZeros = 0
                if even:
                    sign = 1 if sign <= 0 else -1
                    output[-3] = sign
                even = True
                output.append(sign)
    return output


def b8z5(list_of_givenBits):
    output = []
    counter = 0
    previousPulse = 0
    print(list_of_givenBits)
    for bit in list_of_givenBits:
        if bit == 1:
            counter = 0
            if previousPulse == 1:
                output.append(-1)
                previousPulse = -1
            elif previousPulse == -1:
                output.append(1)
                previousPulse = 1
            elif previousPulse == 0:
                output.append(bit)
                previousPulse = bit
        elif bit == 0:
            counter = counter + 1
            if counter == 8:
                output = output[:len(output) - 7]
                if previousPulse == 1:
                    output.extend([0, 0, 0, 1, -1, 0, -1, 1])
                elif previousPulse == -1:
                    output.extend([0, 0, 0, -1, 1, 0, 1, -1])
                counter = 0
            else:
                output.append(0)
    print(output)
    return output


def b4B5B(list_of_givenBits):
    # make a dictionary with all the possible 4 bit binary and there transposition in 5 bit
    encodingTable = {
        "0000": "11110",
        "0001": "01001",
        "0010": "10100",
        "0011": "10101",
        "0100": "01010",
        "0101": "01011",
        "0110": "01110",
        "0111": "01111",
        "1000": "10010",
        "1001": "10011",
        "1010": "10110",
        "1011": "10111",
        "1100": "11010",
        "1101": "11011",
        "1110": "11100",
        "1111": "11101"
    }

    #  make an empty string that will be populated by the 5 bit conversion
    output = ""

    # iterate to every 4 postion of the string
    for i in range(0, len(list_of_givenBits) - 1, 4):
        # add the 5bit translation to the new string
        output += encodingTable[list_of_givenBits[i:i + 4]]
    return output


master = Tk()
master.configure(bg='grey')
master.title("Data Encoding")
label = tk.Text(master, height=1, width=31,font='arial 12 bold',bg='white',foreground='black')
label.grid(row=0,column=2)


def nrzU():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = nrzUnipolar(list_of_givenBits)
    stepPlotNRZU("NRZ-Unipolar Encoding", apply_rules_of_encoding, list_of_givenBits)


b1 = tk.Button(master, text="NRZ Unipolar", command=nrzU,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b1.grid(row=1,column=0)



def nrZL():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = nrzL(list_of_givenBits)
    stepPlot("NRZ-L Encoding", apply_rules_of_encoding, list_of_givenBits)


b2 = tk.Button(master, text="NRZ-L", command=nrZL,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b2.grid(row=1,column=1)



def nrzMM():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = nrzM(list_of_givenBits)
    stepPlot("NRZ-M Encoding", apply_rules_of_encoding, list_of_givenBits)


b3 = tk.Button(master, text="NRZ-M", command=nrzMM,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b3.grid(row=1,column=2)



def nrzSS():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = nrzS(list_of_givenBits)
    stepPlot("NRZ-S Encoding", apply_rules_of_encoding, list_of_givenBits)


b4 = tk.Button(master, text="NRZ-S", command=nrzSS,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b4.grid(row=1,column=3)



def manchesterr():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = manchester(list_of_givenBits)
    stepPlot2("BIPHASE-L(MANCHESTER) Encoding", apply_rules_of_encoding, list_of_givenBits)


b5 = tk.Button(master, text="Biphase-L(MANCHESTER)", command=manchesterr,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b5.grid(row=1,column=4)


def biphaseMM():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = biphaseM(list_of_givenBits)
    stepPlot2("BIPHASE-M Encoding", apply_rules_of_encoding, list_of_givenBits)


b6 = tk.Button(master, text="Biphase-M", command=biphaseMM,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b6.grid(row=2,column=0)


def biphaseSS():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = biphaseS(list_of_givenBits)
    stepPlot2("BIPHASE-S Encoding", apply_rules_of_encoding, list_of_givenBits)


b7 = tk.Button(master, text="Biphase-S", command=biphaseSS,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b7.grid(row=2,column=1)


def manchesterDiffer():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = manchesterDiff(list_of_givenBits)
    stepPlot2("Manchester Differential Encoding", apply_rules_of_encoding, list_of_givenBits)


b8 = tk.Button(master, text="Manchester Differential", command=manchesterDiffer,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b8.grid(row=2,column=2)


def amiBipolarr():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    first_apply_rules_of_encoding = amiBipolar(list_of_givenBits)
    second_apply_rules_of_encoding = amiBipolar1(first_apply_rules_of_encoding)
    stepPlot("AMI-Bipolar Encoding", second_apply_rules_of_encoding, list_of_givenBits)


b9 = tk.Button(master, text="AMI-Bipolar", command=amiBipolarr,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b9.grid(row=2,column=3)


def pseudoternarr():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = pseudoternar(list_of_givenBits)
    stepPlot("AMI-Pseudoternar Encoding", apply_rules_of_encoding, list_of_givenBits)


b10 = tk.Button(master, text="AMI-Pseudoternar", command=pseudoternarr,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b10.grid(row=2,column=4)

def B8Z5():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = b8z5(list_of_givenBits)
    stepPlot("B8Z5 Encoding", apply_rules_of_encoding, list_of_givenBits)


b11 = tk.Button(master, text="B8Z5", command=B8Z5,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b11.grid(row=3,column=0)

def MLT3():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = mlt33(list_of_givenBits)
    stepPlot("MLT3 Encoding", apply_rules_of_encoding, list_of_givenBits)


b12 = tk.Button(master, text="MLT3", command=MLT3,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b12.grid(row=3,column=1)

def B4B5():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int,boxInput))
    if len(list_of_givenBits) % 4 != 0 or len(list_of_givenBits) < 4:
        messagebox.showwarning("Warning !", "The number of bits must be a multiple of 4 !" )
    else:
        first_apply_rules_of_encoding = b4B5B(boxInput)
        list_first_apply_rules_of_encoding = list(map(int,first_apply_rules_of_encoding))
        second_apply_rules_of_encoding = nrzM(list_first_apply_rules_of_encoding)
        stepPlot("4B5B Encoding", second_apply_rules_of_encoding, list_first_apply_rules_of_encoding)

b13 = tk.Button(master, text="4B5B", command=B4B5,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b13.grid(row=3,column=2)


def HDB3():
    boxInput = label.get("1.0", "end-1c")
    list_of_givenBits = list(map(int, boxInput))
    apply_rules_of_encoding = hdb333(list_of_givenBits)
    stepPlot("HDB3 Encoding", apply_rules_of_encoding, list_of_givenBits)


b14 = tk.Button(master, text="HDB3", command=HDB3,height = 2, width = 23,font=('helvetica', 16),bg='grey30')
b14.grid(row=3,column=3)


master.mainloop()
