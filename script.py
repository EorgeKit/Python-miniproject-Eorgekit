#!usr/bin/env python
import os
global path1
path1 = 'None'

def inf():
    chain = ''
    global chain_list 
    chain_list = []
    chain3 = ''
    for l in myfile:
        if l.startswith('COMPND'):
            if 'CHAIN:'in l[11:17]:
                # print(l)
                chain += l[18:79].strip().replace(' ','').replace(';',',')
                chain2 = chain[:-1]
                # print(chain)
                # print(chain2)
                chain_list = chain2.split(',')
                # print(chain_list)
                chain3 = chain2.replace(',',' and ')
    for i,x in enumerate(chain_list):
        n = '\n'.ljust(15)
        print(' -Chain ',chain_list[i])
        print('   Number of amino acids: ',amino_acid_no()[chain_list[i]])
        print('   Number of helix:',f'{no_of_helix()[chain_list[i]]}'.rjust(10))
        print('   Number of sheet:',f'{no_of_sheet()[chain_list[i]]}'.rjust(10))
        print(f"{'   Sequence:  '}{n.join([(sequence()[chain_list[i]][y:y+50]) for y in range(0,len(sequence()[chain_list[i]]),50)])}")
        
def no_of_sheet():
        nsheet = {}
        for chain in chain_list:
            # print(chain_list)
            for l in myfile:
                if l.startswith('SHEET'):
                    if chain in l[21]:
                        # print(l[21])
                        if nsheet.get(chain):
                            # print(nsheet)
                            nsheet[chain] += 1

                        else:
                            nsheet[chain] = 1
        for chain in chain_list:
            if nsheet.get(chain):
                pass
            else:
                nsheet[chain] = 0
        return nsheet
        
def no_of_helix():
        nhelix = {}
        for chain in chain_list:
            # print(chain_list)
            for l in myfile:
                if l.startswith('HELIX'):
                    if chain in l[19]:
                        # print(l[19])
                            if nhelix.get(chain):
                                nhelix[chain] += 1

                            else:
                                    nhelix[chain] = 1
    
        for chain in chain_list:
            if nhelix.get(chain):
                pass
            else:
                nhelix[chain] = 0
            if l.startswith('HELIX'):
                for i in chain_list1:
                    # print(i)
                    if i in l[19]:
                        # print(l[19])
                        nh.append(l[19])
                        nh_count += 1
        return nhelix
        
def amino_acid_no():
    chain = ''
    chain_list = []
    chain3 = ''
    for l in myfile:
        if l.startswith('COMPND'):
            if 'CHAIN:'in l[11:17]:
                # print(l)
                chain += l[18:79].strip().replace(' ','').replace(';',',')
                chain2 = chain[:-1]
                # print(chain)
                # print(chain2)
                chain_list = chain2.split(',')
    aa = {}
    for l in myfile:
        if l.startswith('SEQRES'):
            # print(l)
            # print(chain_list1)
            for i in chain_list:
                # print(i)
                # print(l[11])
                if i in l[11]:
                    # print('done')
                    # print(i)
                    aa[i] = l[14:17]  
    return aa
        
def sequence():
    chain = ''
    chain_list = []
    chain3 = ''
    for l in myfile:
        if l.startswith('COMPND'):
            if 'CHAIN:'in l[11:17]:
                # print(l)
                chain += l[18:79].strip().replace(' ','').replace(';',',')
                chain2 = chain[:-1]
                chain_list = chain2.split(',')
    d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    seq = []
    for line in myfile:
        if line.startswith('SEQRES'):
            seq.append({line[11]:line.split()[4:]})
    seq_dict={}
    for l in seq:
        # print(l)
        for j,i in l.items():
            if seq_dict.get(j):
                seq_dict[j] += i

            else:
                seq_dict[j] = i
    a=''
    chain_res = {}
    for chain in chain_list:
        b = seq_dict.get(chain)
        for p in b:
            a+=d.get(p)
        chain_res[chain] = a
        a=''
    return chain_res
        
def information():
    if path1 == 'None':
        print('PDB file not loaded')
        print('\n')
        menu()
    else:
        title='Title: '
        for l in myfile:
            if l.startswith('TITLE'):
                title += l[10:80].strip()
        for x in range(0,len(title),80):
            print(title[x:x+80])
        chain = ''
        chain_list = []
        chain3 = ''
        for l in myfile:
            if l.startswith('COMPND'):
                if 'CHAIN:'in l[11:17]:
                    # print(l)
                    chain += l[18:79].strip().replace(' ','').replace(';',',')
                    chain2 = chain[:-1]
                    chain_list = chain2.split(',')
                    chain3 = chain2.replace(',',' and ')
        # print(chain_list)
        print('CHAINS:',chain3)
        inf()
        print('\n')
    menu()

    
def histogram1():
    seqf=[]
    for line in myfile:
        if line.startswith('SEQRES'):
            seqf.append(line.split()[4:])
    s=[]
    b = ''
    for u in seqf:
        # print(i)
        for y in u:
            s.append(y)
            sorted_list = sorted(s)
    c = {}
    lc_list = ' '.join(sorted_list)
    result = lc_list.title()
    lowcase = result.split(' ')
    # print(lowcase)
    for z in lowcase:
        n = '\n'.ljust(16)
        a = lowcase.count(z)
        # print(z+'(%d) : '%(a)+'*'*a)
        c[z] = z.ljust(4)+'(%s)'.rjust(5)%(f'{a:>3}')+ ':'.center(5) +f"{n.join([('*'*a)[y:y+80] for y in range(0,len(('*'*a)),80)])}"
    for value in c.values():
        print(value)
        
def histogram2():
    seqf=[]
    for line in myfile:
        if line.startswith('SEQRES'):
            seqf.append(line.split()[4:])
    s=[]
    b = ''
    for u in seqf:
        # print(i)
        for y in u:
            s.append(y)
            sorted_list = sorted(s)
    # print(sorted_list)
    
    c = {}
    lc_list = ' '.join(sorted_list)
    result = lc_list.title()
    lowcase = result.split(' ')
    lowcase_rev = lowcase[::-1]
    # print(lowcase_rev)
    # print(lowcase)
    for z in lowcase_rev:
        n = '\n'.ljust(16)
        a = lowcase_rev.count(z)
        # print(z+'(%d) : '%(a)+'*'*a)
        c[z] = z.ljust(4)+'(%s)'.rjust(5)%(f'{a:>3}')+ ':'.center(5) +f"{n.join([('*'*a)[y:y+80] for y in range(0,len(('*'*a)),80)])}"
    for value in c.values():
        print(value)
        
def histogram3():
    seqf=[]
    for line in myfile:
        if line.startswith('SEQRES'):
            seqf.append(line.split()[4:])
    s=[]
    b = ''
    for u in seqf:
        # print(i)
        for y in u:
            s.append(y)
            sorted_list = sorted(s)
    # print(sorted_list)
    
    c = {}
    lc_list = ' '.join(sorted_list)
    result = lc_list.title()
    lowcase = result.split(' ')
    lowcase_rev = lowcase[::-1]
    lowcase_rev_count = sorted(lowcase_rev,key = lowcase_rev.count,reverse = True)
    for z in lowcase_rev_count:
        n = '\n'.ljust(16)
        a = lowcase_rev_count.count(z)
        # print(z+'(%d) : '%(a)+'*'*a)
        c[z] = z.ljust(4)+'(%s)'.rjust(5)%(f'{a:>3}')+ ':'.center(5) +f"{n.join([('*'*a)[y:y+80] for y in range(0,len(('*'*a)),80)])}"
    for value in c.values():
        print(value)
        
def histogram4():
    seqf=[]
    for line in myfile:
        if line.startswith('SEQRES'):
            seqf.append(line.split()[4:])
    s=[]
    b = ''
    for u in seqf:
        # print(i)
        for y in u:
            s.append(y)
            sorted_list = sorted(s)
    # print(sorted_list)
    
    c = {}
    lc_list = ' '.join(sorted_list)
    result = lc_list.title()
    lowcase = result.split(' ')
    # lowcase_rev = lowcase[::-1]
    lowcase_count = sorted(lowcase,key = lowcase.count)
    for z in lowcase_count:
        n = '\n'.ljust(16)
        a = lowcase_count.count(z)
        # print(z+'(%d) : '%(a)+'*'*a)
        c[z] = z.ljust(4)+'(%s)'.rjust(5)%(f'{a:>3}')+ ':'.center(5) +f"{n.join([('*'*a)[y:y+80] for y in range(0,len(('*'*a)),80)])}"
    for value in c.values():
        print(value)
        
def histogram_aa():
    if path1 == 'None':
        print('PDB file not loaded')
        print('\n')
        menu()
    else:
        print(f'{"Choose an option to order by: ":>30}')
        print(f'{"number of amino acids - ascending   (an)":>43}')
        print(f'{"number of amino acids - descending  (dn)":>43}')
        print(f'{"alphabetically - ascending          (aa)":>43}')
        print(f'{"alphabetically - descending         (da)":>43}')
        choice = input('order by:')
        select = ('aa','an','dn','da')
        if choice.lower() in select:
            print('\n')
            if choice.lower() == 'aa':
                histogram1()
                print('\n')
                menu()
            elif choice.lower() == 'da':
                histogram2()
                print('\n')
                menu()
            elif choice.lower() == 'dn':
                histogram3()
                print('\n')
                menu()
            elif choice.lower() == 'an':
                histogram4()
                print('\n')
                menu()
        else:
            print('Wrong input,Please type the correct input')
            print('\n')
            histogram_aa()
        

        
def structure():
    print('Secondary Structure of the PDB id %s: '%(os.path.basename(path1.split('.')[0])))
    if path1 == 'None':
        print('PDB file not loaded')
        print('\n')
        menu()
    else:
        chain = ''
        chain_list = []
        chain3 = ''
        for l in myfile:
            if l.startswith('COMPND'):
                if 'CHAIN:'in l[11:17]:
                    # print(l)
                    chain += l[18:79].strip().replace(' ','').replace(';',',')
                    chain2 = chain[:-1]
                    # print(chain)
                    # print(chain2)
                    chain_list = chain2.split(',')
        # print(chain_list)
        for a,c in enumerate(chain_list):
            # print(a,c)
            n = '\n'
            print('Chain',c+':')
            print('(1)')
            structure_rep_list = list('-'*len(sequence()[c]))
            # print(structure_rep_list)
            tag_list = list('-'*len(sequence()[c]))
            for line in myfile:
                if line.startswith('HELIX'):
                    if c == line[19]:
                        start_pos = int(line[21:25].strip())
                        end_pos = int(line[33:37].strip())
                        helix_tag = line[7:10].strip()
                        # print(start_pos)
                        for i,j in enumerate(structure_rep_list, start=1):
                            if i >= start_pos and i <= end_pos:
                                structure_rep_list[i-1] = '/'
                            if i == start_pos:
                                tag_list[i-1] = helix_tag
                if line.startswith('SHEET'):
                    if c == line[21]:
                        start_pos = int(line[22:26].strip())
                        end_pos = int(line[33:37].strip())
                        tag1 =  line[7:10].strip()
                        tag2 = line[11:14].strip()
                        sheet_tag = tag1 + tag2
                        for i,j in enumerate(structure_rep_list, start=1):
                            if i >= start_pos and i <= end_pos:
                                structure_rep_list[i-1] = '|'
                            if i == start_pos:
                                if sheet_tag==1:
                                    tag_list[i-1]=sheet_tag
                                else:
                                    tag_list[i-1:i+1]=sheet_tag
            structure_rep = ''.join(structure_rep_list)
            tag = ''.join(tag_list)
            for n in range(0,len(sequence()[c]),80):
                line = sequence()[c][n:n+80]
                print(line)
                print(structure_rep[n:n+80])
                print(tag[n:n+80].replace('-', ' '))
            print(f"({amino_acid_no()[c]})")
            print('\n')
    menu()

def file_path():
    global path1 
    global myfile
    myfile = None
    if path1 == 'None':
        # path1 = 'None'
        fpath = input("Enter a Valid PATH for a PDB File:")
        if fpath.endswith('.pdb'):
            if os.path.exists(fpath):
                with open(fpath,'r') as file:
                    myfile = file.readlines()
                    print('The File ' + os.path.basename(fpath) + ' has been successfully loaded')
                    path1=fpath
                    print('\n')
                    menu()
            else:
                print('File ' + os.path.basename(fpath) + ' not found')
                file_path()
        else:
            print('Path not found')
            file_path()
    else:
        replace_choice = input(f'Do you want to replace {os.path.basename(path1)} (yes/no)? ')
        if replace_choice.lower() in ('yes', 'y', 'no', 'n'):
            if replace_choice.lower() == 'yes' or replace_choice.lower() == 'y':
                fpath = input("Enter a Valid PATH for a PDB File:")
                if fpath.endswith('.pdb'):
                    if os.path.exists(fpath):
                        with open(fpath,'r') as file:
                            myfile = file.readlines()
                            print('The File ' + os.path.basename(fpath) + ' has been successfully loaded')
                            path1=fpath
                            print('\n')
                            menu()
                    else:
                        print('File ' + os.path.basename(fpath) + ' not found')
                        file_path()
                else:
                    print('Path not found')
                    file_path()
            else:
                menu()
        else:
            menu()
def inp3():
    choice = input(':')
    selection = ("O","I","H","S","Q",'1','2','3','4','5')
    if choice.upper() in selection:
        if choice.upper() == ("O") or choice == '1':
            file_path()
        elif choice.upper() == ("I") or choice == '2':
            print("PDB File:",os.path.basename(path1))
            information()
        elif choice.upper() == ("H") or choice == '3':
            histogram_aa()
        elif choice.upper() == ("S") or choice == '4':
            structure()
        elif choice.upper() == ("Q") or choice == '5':
            exit()
    else:
        print("Invalid choice.Please input a valid choice")
        print('\n')
        menu()

def exit():
    import sys
    quit = input('Do you want to exit(E) or do you want go back to the menu (M):')
    if quit.upper() == 'E':
        sys.exit()
    elif quit.upper() == 'M':
        print('\n')
        menu()
    else:
        exit()

def menu():
    print('*' * 80)
    print('*', 'PDB FILE ANALYZER',' ' * 58,'*') 
    print('*' * 80)
    print('*', 'Select an option from below:',' ' * 47,'*')
    print('*',' ' * 76, '*')
    print('*',' '*4, '1)', 'Open a PDB File',' '*15, '(O)',' '*32,'*')
    print('*',' '*4, '2)', 'Information',' '*19, '(I)',' '*32,'*')
    print('*',' '*4, '3)', 'Show histogram of amino acids',' ','(H)',' '*32,'*')
    print('*',' '*4, '4)', 'Display Secondary Structure',' '*3, '(S)',' '*32,'*')
    print('*',' '*4, '5)', 'Exit',' '*26,'(Q)',' '*32,'*')
    print('*',' '*76, '*')
    print('*', ('Current PDB:%3s'%os.path.basename(path1)).rjust(76), '*')
    print('*'*80)
    inp3()
    
menu()