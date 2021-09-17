# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter


class FighterspiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        adapter['name'] = adapter['name'].strip()
        adapter['record'] = adapter['record'].replace('Record: ', '').strip()


        adapter['DoB'] = adapter['DoB'].replace(',', '').strip()

        if adapter['height'] is not None:
            adapter['height'] = adapter['height'].strip()

        if adapter['weight'] is not None:
            adapter['weight'] = adapter['weight'].replace('lbs.', '').strip()

        if adapter['reach'] is not None:
            adapter['reach'] = adapter['reach'].replace('"', '').strip()

        if adapter['stance'] is not None:
            adapter['stance'] = adapter['stance'].strip()

        # the structure of the rows are pretty similar
        columns = ['SLpM', 'strAcc', 'SApM', 'strDef', 'tdAvg', 'tdAcc', 'tdDef', 'subAvg']
        for row in columns:
            adapter[row] = adapter[row].strip()

        return item