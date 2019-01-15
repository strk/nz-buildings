# -*- coding: utf-8 -*-
"""
################################################################################
#
# Copyright 2018 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the 3 clause BSD license. See the
# LICENSE file for more information.
#
################################################################################

    Tests: Reference Data GUI setup confirm default settings

 ***************************************************************************/
"""

import unittest

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QLineEdit
from qgis.utils import plugins


class SetUpReferenceData(unittest.TestCase):
    """Test Reference Data GUI initial setup confirm default settings"""

    def setUp(self):
        """Runs before each test."""
        self.building_plugin = plugins.get('buildings')
        self.building_plugin.main_toolbar.actions()[0].trigger()
        self.dockwidget = self.building_plugin.dockwidget
        sub_menu = self.dockwidget.lst_sub_menu
        sub_menu.setCurrentItem(sub_menu.findItems(
            'Reference Data', Qt.MatchExactly)[0])
        self.reference_frame = self.dockwidget.current_frame

    def tearDown(self):
        """Runs after each test."""
        self.reference_frame.btn_exit.click()

    def test_disabled_on_start(self):
        """Test ui options disabled on opening as there is a current dataset"""
        self.assertFalse(self.reference_frame.le_key.isEnabled())
        self.assertFalse(self.reference_frame.grbx_topo.isEnabled())
        self.assertFalse(self.reference_frame.grbx_admin.isEnabled())
        self.assertFalse(self.reference_frame.chbx_canals.isEnabled())
        self.assertFalse(self.reference_frame.chbx_lagoons.isEnabled())
        self.assertFalse(self.reference_frame.chbx_lakes.isEnabled())
        self.assertFalse(self.reference_frame.chbx_ponds.isEnabled())
        self.assertFalse(self.reference_frame.chbx_rivers.isEnabled())
        self.assertFalse(self.reference_frame.chbx_swamps.isEnabled())
        self.assertFalse(self.reference_frame.chbx_suburbs.isEnabled())
        self.assertFalse(self.reference_frame.chbx_town.isEnabled())
        self.assertFalse(self.reference_frame.chbx_ta.isEnabled())
        self.assertFalse(self.reference_frame.chbx_ta_grid.isEnabled())
        self.assertFalse(self.reference_frame.btn_ok.isEnabled())
        self.assertTrue(self.reference_frame.btn_exit.isEnabled())

    def test_lineedit_key(self):
        """Check line edit is in password mode to hide key"""
        self.reference_frame.le_key.setText('testing')
        self.assertEqual(self.reference_frame.le_key.echoMode(), QLineEdit.Password)

    def test_groupbx_check(self):
        self.reference_frame.grbx_topo.setChecked(True)
        self.assertTrue(self.reference_frame.chbx_canals.isChecked())
        self.assertTrue(self.reference_frame.chbx_lagoons.isChecked())
        self.assertTrue(self.reference_frame.chbx_lakes.isChecked())
        self.assertTrue(self.reference_frame.chbx_ponds.isChecked())
        self.assertTrue(self.reference_frame.chbx_rivers.isChecked())
        self.assertTrue(self.reference_frame.chbx_swamps.isChecked())
        self.reference_frame.grbx_topo.setChecked(False)
        self.assertFalse(self.reference_frame.chbx_canals.isChecked())
        self.assertFalse(self.reference_frame.chbx_lagoons.isChecked())
        self.assertFalse(self.reference_frame.chbx_lakes.isChecked())
        self.assertFalse(self.reference_frame.chbx_ponds.isChecked())
        self.assertFalse(self.reference_frame.chbx_rivers.isChecked())
        self.assertFalse(self.reference_frame.chbx_swamps.isChecked())
        self.reference_frame.grbx_admin.setChecked(True)
        self.assertTrue(self.reference_frame.chbx_suburbs.isChecked())
        self.assertTrue(self.reference_frame.chbx_town.isChecked())
        self.assertTrue(self.reference_frame.chbx_ta.isChecked())
        self.assertTrue(self.reference_frame.chbx_ta_grid.isChecked())
        self.reference_frame.grbx_admin.setChecked(False)
        self.assertFalse(self.reference_frame.chbx_suburbs.isChecked())
        self.assertFalse(self.reference_frame.chbx_town.isChecked())
        self.assertFalse(self.reference_frame.chbx_ta.isChecked())
        self.assertFalse(self.reference_frame.chbx_ta_grid.isChecked())
