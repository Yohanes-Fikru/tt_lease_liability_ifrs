# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx
from openerp.exceptions import Warning

class PartnerXlsx(ReportXlsx):
    def generate_xlsx_report(self, workbook, datas, partners):
        pass

PartnerXlsx("report.MODEL_NAME.xlsx", "MODEL_NAME")

# PartnerXlsx REPORTNAMEXLSX

class REPORTNAMEREPORT(models.TransientModel):
    _name = "module_name.report"

    @api.multi
    def print_report(self):
        return {
            "type": "ir.actions.report.xml",
            "report_type": "xlsx",
            "report_name": "MODEL_NAME.xlsx",
            "model": "MODEL_NAME",
            "datas": None
        }
