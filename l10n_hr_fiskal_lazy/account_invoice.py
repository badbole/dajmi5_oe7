# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Module: l10n_hr_fiskal_lazy
#    Author: Davor Bojkić
#    mail:   bole@dajmi5.com
#    Copyright (C) 2012- Daj Mi 5, 
#                  http://www.dajmi5.com
#                    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields

class account_invoice(osv.Model):
    _inherit = "account.invoice"
   
    
    def _get_fiskal_broj(self, cr, uid, ids, field_name, field_value, context=None):
        res={}
        for invoice in self.browse(cr, uid, ids):
            rn={}
            # PAZI!! ovo samo ako je prefix %(y)/  dakle 3 znaka!!!
            test = invoice.number and invoice.number[3:] or False
            test = test and test.lstrip('0')
            res[invoice.id]=test #{'fiskal_broj':test}
        return res
        
    _columns = {
                'fiskal_broj':fields.function(_get_fiskal_broj, type="char", string="Fiskalizirani broj", readonly=True , store=True)
                }