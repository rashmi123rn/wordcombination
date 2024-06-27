from django.shortcuts import render




# Create your views here.
def home(request):
    
    list1=perm3("EAT")
    list2=perm4("FAST")
    list3=perm5("SMILE")
    return render(request,'myapp/combinations.html',{'param1':list1,'param2':list2,'param3':list3})


def perm3(str3):
    
    list3=[]
    c1=str3[0:1]
    c2=str3[1:2]
    c3=str3[2:3]

    list3.append(c1+c2+c3)
    list3.append(c2+c1+c3)
    list3.append(c1+c3+c2)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    list3.append(c2+c3+c1)

    return list3



def perm4(str4):
    c1=str4[0:1]
    c2=str4[1:2]
    c3=str4[2:3]
    c4=str4[3:4]
    list4=[]
    part1=c1
    part2=c2+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
                   list4.append(part1+temp[i])

    

    part1=c2
    part2=c1+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
                   list4.append(part1+temp[i])

   


    part1=c3
    part2=c2+c1+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
                   list4.append(part1+temp[i])

   

    part1=c4
    part2=c2+c3+c1
    temp=perm3(part2)
    for i in range(0,len(temp),1):
                   list4.append(part1+temp[i])

    return list4



def perm5(str5):
    c1=str5[0:1]
    c2=str5[1:2]
    c3=str5[2:3]
    c4=str5[3:4]
    c5=str5[4:5]
    list5=[]
    part1=c1
    part2=c2+c3+c4+c5
    temp1=perm4(part2)
    for i in range(0,len(temp1),1):
                   list5.append(part1+temp1[i])


    part1=c2
    part2=c1+c3+c4+c5
    temp1=perm4(part2)
    for i in range(0,len(temp1),1):
                   list5.append(part1+temp1[i])

   


    part1=c3
    part2=c2+c1+c4+c5
    temp1=perm4(part2)
    for i in range(0,len(temp1),1):
                   list5.append(part1+temp1[i])

   

    part1=c4
    part2=c2+c3+c1+c5
    temp1=perm4(part2)
    for i in range(0,len(temp1),1):
                   list5.append(part1+temp1[i])

    part1=c5
    part2=c2+c3+c1+c4
    temp1=perm4(part2)
    for i in range(0,len(temp1),1):
                   list5.append(part1+temp1[i])

    return list5
    return results