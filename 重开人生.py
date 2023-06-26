#导入模块
import sys

print("异界入侵，生灵涂炭，百姓民不聊生...")
print("你以一己之力，击退异界生灵，遂觉索然无味，进行转生....")
c = input ("\n转生开始！你转生到了修仙世界！\n请输入你的名称：\n")
print("命名成功！你的名称为："+str(c))
y=input("请选择你的性别：1、男；2、女\n")
if int(y) == 2:
    print("你的性别为 女！") 
else:
    print("你的性别为 男！")
input("输入任意字符继续：")
q = 20   #可分配的点数上限
print("请分配你的六项属性值：20(创世神降下怜悯，分配完后全属性-1)")

b = input("\n1、智力：")
#若输入的值小于0（负数），则执行if语句
if int(b) < 0:
    print("输入数值不可小于0，请重新输入：")
    r = input()
    #若输入还是小于0，则结束程序
    if int(r) < 0:
        print("还乱输？滚滚滚！！")
        sys.exit(0)
    else:
        b = r #将输入的值r，赋予b

#若输入的值大于等于0，则程序正常执行
if q-int(b) >=0:
    q = q - int(b)
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if q < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")
        qq = input()
        q = q - int(qq)
        if q-int(b) >=0:
            print("剩余可分配点数："+str(q))

d = input("\n2、体质：")
if int(d) <0:
    print("输入数值不可小于0，请重新输入：")
    t = input()
    if int(t) < 0:
        print("唔~ 你乱输！不跟你玩了！")
        sys.exit(0)
    else:
        d = t
q = q - int(d)
if q >=0:
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if int(q) < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")
        qqqq = input()
        if int(qqqq) < 0:
            print(" ... ")
            sys.exit(0)
        if int(qqqq) > 20:
            print(" ... ")
            sys.exit(0) 
        q = (q + int(d)) - qqqq
e = input("\n3、魅力：")
if int(e) >= 0:
    q = q - int(e)
else:
    print("输入的数值不可小于0，请重新输入：")
    qqq = input()
    if int(qqq) >= 0:
        q = q - int(qqq)
    else:
        print("胡乱输入？ 你去找别人玩吧！")
        sys.exit(0)
if q >=0:
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if q < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")

f = input("\n4、家境：")
if int(f) >= 0:
    q = q - int(f)
else:
    print("输入的数值不可小于0，请重新输入：")
    ff = input()
    if int(ff) >= 0:
        q = q - int(ff)
    else:
        print(" ... ")
        sys.exit(0)
if q >=0:
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if q < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")

g = input("\n5、气运：")
if int(g) >= 0:
    q = q - int(g)
else:
    print("输入的数值不可小于0，请重新输入：")
    gg = input()
    if int(gg) >= 0:
        q = q - int(gg)
    else:
        print("我可能不是人，但是你真的狗！")
        sys.exit(0)
if q >=0:
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if q < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")

h = input("\n6、精神：")
if int(h) >= 0:
    q = q - int(h)
else:
    print("输入的数值不可小于0，请重新输入：")
    hh = input()
    if int(hh) >= 0:
        q = q - int(hh)
    else:
        print(" ... ")
        sys.exit(0)
if q >=0:
    print("剩余可分配点数："+str(q))
if q <= 0:
    print("可用点数已分配完！")
    if q < 0:
        print("所分配的点数超过了20点数上限，请重新分配：")

print("\n\n\n分配完毕，你的属性为 ..... 加载失败！调用默认值！\n\n你的属性 为：\n智力：1\n体质：2\n魅力：0\n家境：2\n气运：-99\n精神：7")
input("输入任意字符继续：")
print(input("即将触发‘创世神的怜悯’，是否触发：\n是/否\n"))
print("创世神对你很失望，全属性-10")
input("输入任意字符继续：")
input("在这充满危机的世界中，请选择你要降生的人家：\n1、普通人家（20%） 2、山野世家（0.1%） 3、财阀门户（0.001%） 4、贵族子弟（0.0000001） 5、流浪者（79.89899999999999）\n")
print("恭喜你！出生成为了‘贵族子弟’！")
input("输入任意字符继续：")
print("\n0岁。你出生了，由于体质过低，即将胎死腹中。")
input("输入任意字符继续：")
print("\n0岁。你门中老祖为你求来一颗大还丹。")
input("输入任意字符继续：")
print("\n0岁。你因体质过低，承受不住药力，成为死婴，但保留着一丝神智。")
input("输入任意字符继续：")
print("\n0岁。你出生了，家中长辈被你的模样吓了一跳，称你为妖魔，会带来无穷厄运，欲要诛杀。")
input("输入任意字符继续")
print("\n你的母亲带病下床，跪地求情，方保你一命!")
input("输入任意字符继续：")
print("\n翌日，朝廷带兵血洗了此地，你看着族人一个个倒在面前，眸中尽是不解，含着不甘死于剑下！\n")
input("你死了！获得成就： “大还丹！” \n模拟结束！")
import sys
sys.exit(0)
#  print(str(b))





















































