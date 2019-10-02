# -*- coding: utf-8 -*-
from item_weight import get_items_weight, Commercial, Residence, Industry
from collections import namedtuple
import itertools

building = namedtuple('building', ['pay', 'income'])

'''
粗糙拟合一下 800级为例
蓝卡收入倍增大概25.4级 升级开销倍增大概20级
史诗和稀有参数 25.4 21.3
实际可按照当前等级情况重新拟合
'''
common = building(20., 25.4)
rare_epic = building(21.3, 25.4)

Quality = {
    'common': '便利店 五金店 服装店 菜市场 学校 木屋 居民楼 钢结构房 平房 木材厂 食品厂 造纸厂 电厂',
    'uncommon': '图书城 商贸中心 民食斋 媒体之声 人才公寓 花园洋房 中式小楼 空中别墅 钢铁厂 纺织厂 零件厂 企鹅机械'
}


def delta_income(income, pay, weight, level_delta):
    return weight * (2. ** (1. / pay) / 2. ** (1. / income)) ** level_delta


def pay_total(pay, level_delta):
    q = 2. ** (1. / pay)
    return (1. - q ** level_delta) / (1. - q)


def generate_quality_array(combo_tuple):
    result, idx = [None] * 9, 0
    for sub_tuple in combo_tuple:
        for b in sub_tuple:
            result[idx] = b in Quality.get('common') and common or rare_epic
            idx += 1
    return result


def analyze(weight_array, quality_array, level_delta=100):
    array = []
    for w, q in zip(weight_array, quality_array):
        array.append(delta_income(q.income, q.pay, w, level_delta) / pay_total(q.pay, level_delta))
    return array


if __name__ == '__main__':
    search_space = itertools.product(itertools.combinations(Residence.split(), 3),
                                     itertools.combinations(Commercial.split(), 3),
                                     itertools.combinations(Industry.split(), 3))
    best_combo, best_score = None, 0
    for combo in search_space:
        weights = get_items_weight(combo)
        qualities = generate_quality_array(combo)
        score = sum(analyze(weights, qualities, 200))
        if best_score < score:
            best_score = score
            best_combo = combo
    print(best_combo, best_score)
    # for s in best_combo:
    #     for b in s:
    #         print b.decode('utf-8').encode('gbk'),

# 人才公寓 中式小楼 空中别墅 服装店 菜市场 民食斋 食品厂 电厂 纺织厂