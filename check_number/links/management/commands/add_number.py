from django.core.management.base import BaseCommand, CommandError

from links.models import Link

import xlrd
import re


class Command(BaseCommand):
    def handle(self, *args, **options):
        excel_data_file = xlrd.open_workbook('./DATA.xlsx')
        sheet = excel_data_file.sheet_by_index(0)
        row_quantity = sheet.nrows

        if row_quantity > 0:
            for row in range(0, row_quantity):
                number = str(sheet.row(row)[0])
                number = str(re.sub('^(\+7)', '8', number))
                number = str(re.sub('(\.0)', '', number))
                number = str(re.sub('[^0-9]', '', number))
                if not Link.objects.filter(number=number):
                    Link.objects.create(number=number)


