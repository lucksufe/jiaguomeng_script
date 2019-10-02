# -*- coding: utf-8 -*-
from config import *
from collections import defaultdict

Commercial = '便利店 五金店 服装店 菜市场 学校 图书城 商贸中心 民食斋 媒体之声'
Residence = '木屋 居民楼 钢结构房 平房 人才公寓 花园洋房 中式小楼 空中别墅'
Industry = '木材厂 食品厂 造纸厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械'


def get_items_weight(items):
    def calculate_comb(buildings):
        build_tuple = buildings[0] + buildings[1] + buildings[2]
        starts = [start[x] for x in build_tuple]
        results = [1] * 9
        for building in build_tuple:
            if building in buffs_100:
                for buffed in buffs_100[building]:
                    if buffed in build_tuple:
                        results[build_tuple.index(buffed)] += star[building]
            if building in buffs_50:
                for buffed in buffs_50[building]:
                    if buffed in build_tuple:
                        results[build_tuple.index(buffed)] += star[building] * 0.5
            if building in buffs_com:
                to_add = buffs_com[building][star[building] - 1]
                results[0] += to_add
                results[1] += to_add
                results[2] += to_add
            if building in buffs_ind:
                to_add = buffs_ind[building][star[building] - 1]
                results[3] += to_add
                results[4] += to_add
                results[5] += to_add
            if building in buffs_res:
                to_add = buffs_res[building][star[building] - 1]
                results[6] += to_add
                results[7] += to_add
                results[8] += to_add
        return [v * results[i] / star_dict[star[build_tuple[i]]] for i, v in enumerate(starts)]

    commercial = Commercial.split()
    residence = Residence.split()
    industry = Industry.split()

    one_s = OneStars.split()
    two_s = TwoStars.split()
    tri_s = TriStars.split()
    qua_s = QuaStars.split()
    pen_s = PenStars.split()

    star = dict()
    for item in one_s:
        star[item] = 1
    for item in two_s:
        star[item] = 2
    for item in tri_s:
        star[item] = 3
    for item in qua_s:
        star[item] = 4
    for item in pen_s:
        star[item] = 5

    star_dict = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

    # 星级 * 政策 * 照片 * 任务
    start = defaultdict(int)
    for item in residence:  # 住宅
        start[item] = (star_dict[star[item]] *
                       (1 + Policy['Global'] + Policy['Online'] + Policy['Residence'] + Policy['JiaGuoZhiGuang']) *
                       (1 + Photos['Global'] + Photos['Online'] + Photos['Residence']) *
                       (1 + QuestsGeneral['Global'] + QuestsGeneral['Online'] + QuestsGeneral[
                           'Residence'] + QuestsGeneral.get(item, 0))
                       )
    for item in commercial:  # 商业
        start[item] = (star_dict[star[item]] *
                       (1 + Policy['Global'] + Policy['Online'] + Policy['Commercial'] + Policy['JiaGuoZhiGuang']) *
                       (1 + Photos['Global'] + Photos['Online'] + Photos['Commercial']) *
                       (1 + QuestsGeneral['Global'] + QuestsGeneral['Online'] + QuestsGeneral[
                           'Commercial'] + QuestsGeneral.get(item, 0))
                       )
    for item in industry:  # 工业
        start[item] = (star_dict[star[item]] *
                       (1 + Policy['Global'] + Policy['Online'] + Policy['Industry'] + Policy['JiaGuoZhiGuang']) *
                       (1 + Photos['Global'] + Photos['Online'] + Photos['Industry']) *
                       (1 + QuestsGeneral['Global'] + QuestsGeneral['Online'] + QuestsGeneral[
                           'Industry'] + QuestsGeneral.get(item, 0))
                       )

    start['花园洋房'] *= 1.022
    start['商贸中心'] *= 1.022
    start['平房'] *= 1.097
    start['电厂'] *= 1.18
    start['企鹅机械'] *= 1.33
    start['人才公寓'] *= 1.4
    start['中式小楼'] *= 1.4
    start['民食斋'] *= 1.52
    start['空中别墅'] *= 1.52
    start['媒体之声'] *= 1.615

    buffs_100 = {
        '木屋': ['木材厂'],
        '居民楼': ['便利店'],
        '钢结构房': ['钢铁厂'],
        '花园洋房': ['商贸中心'],
        '空中别墅': ['民食斋'],
        '便利店': ['居民楼'],
        '五金店': ['零件厂'],
        '服装店': ['纺织厂'],
        '菜市场': ['食品厂'],
        '学校': ['图书城'],
        '图书城': ['学校', '造纸厂'],
        '商贸中心': ['花园洋房'],
        '木材厂': ['木屋'],
        '食品厂': ['菜市场'],
        '造纸厂': ['图书城'],
        '钢铁厂': ['钢结构房'],
        '纺织厂': ['服装店'],
        '零件厂': ['五金店'],
        '企鹅机械': ['零件厂'],
    }

    buffs_50 = {
        '零件厂': ['企鹅机械'],
    }

    buff_list_258 = [.2, .5, .8, 1.1, 1.4]
    buff_list_246 = [.2, .4, .6, .8, 1.0]
    buff_list_015 = [0.75 * x for x in [.2, .4, .6, .8, 1.0]]
    buff_list_010 = [0.5 * x for x in [.2, .4, .6, .8, 1.0]]
    buff_list_005 = [0.25 * x for x in [.2, .4, .6, .8, 1.0]]
    buff_list_035 = [1.75 * x for x in [.2, .4, .6, .8, 1.0]]

    buffs_com = {
        '媒体之声': buff_list_005,
        '企鹅机械': buff_list_015,
        '民食斋': buff_list_246,
        '纺织厂': buff_list_015,
        '人才公寓': buff_list_246,
        '中式小楼': buff_list_246,
        '空中别墅': buff_list_258,
        '电厂': buff_list_258,
    }
    buffs_ind = {
        '媒体之声': buff_list_005,
        '钢铁厂': buff_list_015,
        '中式小楼': buff_list_246,
        '民食斋': buff_list_246,
        '空中别墅': buff_list_258,
        '电厂': buff_list_258,
        '企鹅机械': buff_list_258,
        '人才公寓': buff_list_035,
    }
    buffs_res = {
        '媒体之声': buff_list_005,
        '企鹅机械': buff_list_010,
        '民食斋': buff_list_246,
        '人才公寓': buff_list_246,
        '平房': buff_list_246,
        '空中别墅': buff_list_258,
        '电厂': buff_list_258,
        '中式小楼': buff_list_035,
    }
    return calculate_comb(items)
