import copy
import functools


# 1. 给定一个无序列表，列表中元素均为不重复的整数。
# 请找出列表中有没有比它前面元素都大，比它后面的元素都小的数.
# 如果不存在则返回-1，存在则显示其索引，存在多个时只显示第一个解的索引


def find_ordered_number_in_list(l):
    ls = copy.deepcopy(l)
    lt = sorted(ls)
    t = 0
    for i in range(len(lt)):
        if ls[i] == lt[i]:
            for j in range(i):
                if ls[j] <= lt[i]:
                    pass
                else:
                    t = 1
                    break
            for k in range(i+1, len(lt)):
                if ls[k] > lt[i]:
                    continue
                else:
                    t = 1
                    break
            if t == 0:
                return i
    return -1


def test_find_ordered_number_in_list():
    l1 = [6, 3, 4, 9, 1]
    l2 = [4, 3, 6, 9, 7]
    print(l1)
    print(l2)
    print(find_ordered_number_in_list(l1))
    print(find_ordered_number_in_list(l2))
    return


# 2. 将list中的重复数据去重，至少使用两种方案。可以尝试结合其他数据结构。不要求保持原list顺序。
def delete_duplication_one(l):
    ls = copy.deepcopy(l)
    lt = list(set(ls))
    return lt


def delete_duplication_two(l):
    ls = copy.deepcopy(l)
    lt = list({}.fromkeys(ls).keys())
    return lt


def delete_duplication_three(l):
    ls = copy.deepcopy(l)
    func = lambda x, y: x if y in x else x + [y]
    lt = functools.reduce(func, [[], ] + ls)
    return lt


# - 创建一个元组，分别进行索引、添加、长度计算、切片操作。

def tuple_practice_one():
    t = (1, 2, 3, 4)
    print('创造元组: t = (1, 2, 3, 4)')
    print(t)
    print('索引:t[1]')
    print(t[1])
    t = t + (5, 6)
    print('添加:t = t + (5, 6)')
    print(t)
    print('长度计算:len(t)')
    print(len(t))
    print('切片操作:t[1:4]')
    print(t[1:4])
    return


def tuple_practice_two():
    s1 = {32, 5, 'c', '32', '11'}
    s2 = set({32, '46', 32, 'aa'})
    s3 = set('4,32,46,11,32')
    s4 = set([1, 2, 3])
    s5 = set((1, 2, 3), )
    s6 = set({'a': 6, 'b': 2, 'c': 3})
    print("s1 = {32, 5, 'c', '32', '11'}")
    print(s1)
    print('s1是列表，相同的元素会保留')
    print("s2 = set({32, '46', 32, 'aa'})")
    print(s2)
    print('s2是元组，相同的元素会去除')
    print("s3 = set('4,32,46,11,32')")
    print(s3)
    print('s3是元组，用字符串生成时，会将字符串拆分成单个字符来生成')
    print("s4 = set([1, 2, 3])")
    print(s4)
    print('s4是元组， 用列表生成时，会将列表视为整体')
    print("s5 = set((1, 2, 3), )")
    print(s5)
    print('s5是元组， 用元组生成时，会将元组视为整体')
    print("s6 = set({'a': 1, 'b': 2, 'c': 3})")
    print(s6)
    print('s6是元组， 用字典生成时，会保留字典中的key, 排序无规律')
    return


# 5. 有如下值集合[11,22,33,44,55,66,77,88,99,100,110,200,230,330]。
# 将所有大于66的值保存至字典的第一个key中，将等于小于66的值保存至第二个key中。
# 即：{‘k1’:大于66的值,‘k2’:小于等于66的值}

def classify_by_66():
    ls = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 200, 230, 330]
    print(ls)
    print("function:  classify_by_66")
    di = {'k1': [], 'k2': []}
    for i in range(len(ls)):
        if ls[i] <= 66:
            lt = di.get('k2')
            lt.append(ls[i])
        else:
            lt = di.get('k1')
            lt.append(ls[i])
    print(di.get('k1'))
    print(di.get('k2'))
    return


def create_dict_by_lists(ls, lt):
    di = {}
    for i, j in zip(ls, lt):
        di[i] = j
    print(di)
    return


def test_create_dict_by_lists():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lt = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_dict_by_lists(ls, lt)
    return


def read_file():
    f = open('hamlet.txt')
    readline = f.readlines()
    word = []  # 存储单词
    l = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.',
         '/', ':', ';', '<', '>', '=', '?', '@', '[', '\\', ']', '^',
         '_', '\'', '{', '|', '}', '~', ',']
    # 得到文章的单词并且存入列表中：
    for line in readline:
        for c in l:
            line = line.replace(c, '')
        line = line.strip()
        wo = line.split(' ')
        for i in range(len(wo)):
            wo[i] = wo[i].lower()
        word.extend(wo)
    return word


def clear_account(lists):
    # 去除重复的值
    words = {}
    di = {}
    words = words.fromkeys(lists)
    word_1 = list(words.keys())
    # 然后统计单词出现的次数,并将它存入一个字典中
    for i in word_1:
        di[i] = lists.count(i)
    return di


def sort_1(words):
    # 删除''字符
    del [words['']]
    # 排序,按values进行排序，如果是按key进行排序用sorted(words.items(),key=lambda d:d[0],reverse=True)
    words_1 = {}
    words_1 = sorted(words.items(), key=lambda d: d[1], reverse=True)
    words_1 = dict(words_1)
    return words_1


def main(words):
    # 输出前10个
    i = 0
    for x, y in words.items():
        if i < 10:
            print('the word is "', '{}'.format(x), '"', ' and its amount is "', '{}'.format(y), '"')
            i += 1
            continue
        else:
            break
    return


def count_english_word_in_paper():
    main(sort_1(clear_account(read_file())))


def compare_strings_by_letter(magazine='aa', ransomnote='aab'):
    arr = [0] * 26

    for x in magazine:
        arr[ord(x) - ord('a')] += 1

    for x in ransomnote:
        if arr[ord(x) - ord('a')] == 0:
            return False
        else:
            arr[ord(x) - ord('a')] -= 1
    return True


if __name__ == "__main__":
    # test_find_ordered_number_in_list()
    # test_create_dict_by_lists()
    # l = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    # print(l)
    # delete_duplication_one(l)
    # delete_duplication_two(l)
    # delete_duplication_three(l)
    # tuple_practice_one()
    # tuple_practice_two()
    # classify_by_66()
    # test_create_dict_by_lists()
    count_english_word_in_paper()
    # print("compare_strings_by_letter(magazine='aa', ransomnote='aab')")
    # print(compare_strings_by_letter())
