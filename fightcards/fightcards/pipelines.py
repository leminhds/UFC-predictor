# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re



class FightcardsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        adapter['fight_date'] = adapter['fight_date'].strip().replace(',', '')

        # items to strip
        items = ['fights_location', 'card_name', 'f1', 'f2', 'weight_class', 'winning_method', 'round_fought',
                 'round_format', 'winner']
        for element in items:
            adapter[element] = adapter[element].strip()

        f = re.findall("\d", adapter['round_format'], re.I)
        adapter['round_format'] = f[0]

        f = re.findall("\d+", adapter['f1_sig_strike_total'], re.I)
        adapter['f1_sig_strike_total'] = f[1]

        f = re.findall("\d+", adapter['f2_sig_strike_total'], re.I)
        adapter['f2_sig_strike_total'] = f[1]

        f = re.findall("\d+\%", adapter['f2_sig_strike_per'], re.I)
        adapter['f2_sig_strike_per'] = f[0]

        f = re.findall("\d+\%", adapter['f1_sig_strike_per'], re.I)
        adapter['f1_sig_strike_per'] = f[0]

        f = re.findall("\d+", adapter['f1_td_attempt'], re.I)
        adapter['f1_td_attempt'] = f[1]
        adapter['f1_td_succeed'] = f[0]

        adapter['f2_td_attempt'] = re.findall("\d+", adapter['f2_td_attempt'], re.I)[1]

        adapter['f2_td_succeed'] = re.findall("\d+", adapter['f2_td_succeed'], re.I)[0]




        # items to convert to int
        items_int = ['round_format', 'round_fought', 'f1_sig_strike_total', 'f2_sig_strike_total',
                     'f1_td_attempt', 'f2_td_attempt', 'f1_td_succeed', 'f2_td_succeed']
        for element in items_int:
            adapter[element] = int(adapter[element])

        return item
