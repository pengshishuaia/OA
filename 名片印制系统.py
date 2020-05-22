#名片印制系统可以增删改查
#思路：新建一个列表，列表中的数据为字典
#新建列表
list =[{"姓名":'彭帅',"手机号码":"18910503484","QQ号码":"381833187"},
       {"姓名":'王欣欣',"手机号码":"17801239596","QQ号码":"381833186"}]
list.append({"姓名":'彭小二',"手机号码":"18910508888","QQ号码":"381836666"})
while True:
    print('***********************')
    print("名片印制管理系统")
    print("1:新增名片")
    print("2:删除名片")
    print("3:修改名片")
    print("4:查询所有名片")
    print("5:退出！！！")
    print('***********************')
    while True:
        try:
            temp = input("请输入要选择的操作（输入数字即可）：")
            temp = int(temp)
            break
        except:
            print("输入为无效字符，请从新输入")
    if temp == 1:
        # 新建字典
        arr = {}
        user = input("请输入姓名:")
        phone = input("请输入手机号码:")
        number = input("请输入QQ号码:")
        arr['姓名'] = user
        arr['手机号码'] = phone
        arr['QQ号码'] = user
        print(arr)
        list.append(arr)
        print(list)
    elif temp == 2:
        while True:
            del_user = input("请输入您要删除名片人的姓名:")
            i = 0
            for user_name in list:
                i += 1
                if del_user in user_name['姓名']:
                    print('要删除的名片已经找到')
                    break
                else:
                    print('您输入的用户名不存在，请重新输入（输入数字即可）！')
            # 删除列表中的字典
            del list[(i - 1)]
            print("删除成功")
            print(list)
            break
    elif temp == 3:
        update_user = input("请输入您要修改名片人的姓名:")
        i = 0
        for user_name1 in list:
            i += 1
            if update_user in user_name1['姓名']:
                print('要修改的名片的信息已经找到')
                break
        print(user_name1)

        user = input("请输入姓名:")
        phone = input("请输入手机号码:")
        number = input("请输入QQ号码:")
        user_name1['姓名'] = user
        user_name1['手机号码'] = phone
        user_name1['QQ号码'] = number
        print(user_name1)
        print(list)
    elif temp == 4:
        for value in list:
            for key in value:
                print(key, value[key])
    elif temp == 5:
        print("退出成功，谢谢使用！")
        exit()
    else:
        print("您输入的数字不正确，请重新输入！")



