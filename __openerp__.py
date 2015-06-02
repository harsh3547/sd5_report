# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2011 Camptocamp SA (http://www.camptocamp.com)
#   @author Nicolas Bessi, Vincent Renaville, Guewen Baconnier
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

{'name': 'SD Reports',
 'version': '0.1',
 'category': 'Reports/Webkit',
 'description': """
    """,
 'author': 'Intellerist',
 'website': 'http://www.intellerist.com',
 'depends': ['base', 'report_webkit','hr_contract'],
 'data': ['report/sd5_report.xml','sodra_report_view.xml','sodra_config.xml','sodra_hr_view.xml','report/report_2_sd.xml','sodra_report_sequence.xml','report/sodra_report3.xml','security/ir.model.access.csv'],
 'demo_xml': [],
 'test': [],
 'installable': True,
 'active': False,
 }
